{
  inputs = {
    flake-utils = {
      url = "github:numtide/flake-utils";
    };
    nixpkgs = {
      url = "github:NixOS/nixpkgs";
    };
    poetry2nix = {
      url = "github:nix-community/poetry2nix";
    };
    gitignore = {
      url = "github:hercules-ci/gitignore.nix";
      # Use the same nixpkgs
      inputs = {
        nixpkgs = {
          follows = "nixpkgs";
        };
      };
    };
  };

  outputs = { self, nixpkgs, flake-utils, poetry2nix, gitignore }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        inherit (gitignore.lib) gitignoreSource;
        pkgs = nixpkgs.legacyPackages.${system};
        pyproject = builtins.fromTOML(builtins.readFile(./pyproject.toml));
        name = pyproject.tool.poetry.name;
        name-pure-shell = "${name}-pure-shell";
        name-shell = "${name}-shell";
        name-test = "${name}-test";
        default-python = pkgs.python310;
        nix-dev-dependencies = [
          # Alternative Pythons for Tox
          (pkgs.python310.withPackages(ps: [ps.scipy ps.numpy ps.matplotlib]))
          pkgs.poetry
          pkgs.hwloc
          pkgs.graphviz
          pkgs.singularity
        ];
      in {
        packages.${name} = pkgs.poetry2nix.mkPoetryApplication {
          projectDir = gitignoreSource ./.;
          python = default-python;
        };

        # There are two approaches to make a poetry project work in Nix:
        # 1. Use Nix to install dependencies in poetry.lock.
        # 2. Use Nix to install Poetry and use Poetry to install dependencies in poetry.lock.
        # Option 2 is less elegant, because it uses a package manager to install a package manager.
        # For example, to effectively cache the environment in CI, I have to cache the Nix store and the Poetry venv.
        # But at the time of writing poetry2nix DOES NOT WORK with Python's cryptography.
        # Cryptography is a core dependency, so it won't work at all.
        # ${name-pure-shell} is option 1, ${name-shell} is option 2.
        packages.${name-pure-shell} = pkgs.mkShell {
          buildInputs = nix-dev-dependencies ++ [
            (pkgs.poetry2nix.mkPoetryEnv {
              projectDir = gitignoreSource ./.;
              # default Python for shell
              python = default-python;
            })
          ];
          # TODO: write a check expression (`nix flake check`)
        };

        packages.${name-shell} = pkgs.mkShell {
          buildInputs = nix-dev-dependencies ++ [default-python];
          shellHook = ''
            if [ ! -f poetry.lock ] || [ ! -f build/poetry-$(sha1sum poetry.lock | cut -f1 -d' ') ]; then
                poetry install --remove-untracked
                if [ ! -d build ]; then
                    mkdir build
                fi
                touch build/poetry-$(sha1sum poetry.lock | cut -f1 -d' ')
            fi
            export PREPEND_TO_PS1="(${name}) "
            export PYTHONNOUSERSITE=true
            export VIRTUAL_ENV=$(poetry env info --path)
            export PATH=$VIRTUAL_ENV/bin:$PATH
            export LD_LIBRARY_PATH=${pkgs.lapack}/lib:${pkgs.blas}/lib:${pkgs.gcc-unwrapped.lib}/lib
          '';
          # TODO: write a check expression (`nix flake check`)
        };

        devShell = self.packages.${system}.${name-shell};

        defaultPackage = self.packages.${system}.${name};
      });
}
