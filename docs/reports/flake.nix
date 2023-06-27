{
  inputs = {
    flake-utils = {
      url = "github:numtide/flake-utils";
    };
    nix-utils = {
      url = "github:charmoniumQ/nix-utils";
    };
    nix-documents = {
      url = "github:charmoniumQ/nix-documents";
    };
  };
  outputs = { self, nixpkgs, flake-utils, nix-utils, nix-documents }:
    flake-utils.lib.eachDefaultSystem
      (system:
        let
          pkgs = nixpkgs.legacyPackages.${system};
          nix-lib = nixpkgs.lib;
          nix-utils-lib = nix-utils.lib.${system};
          nix-documents-lib = nix-documents.lib.${system};
        in
        {
          packages = nix-utils-lib.packageSetRec (self: [
            (nix-documents-lib.markdownDocument {
              src = ./.;
              main = "ncsa_delta_proposal.md";
              name = "ncsa_delta_proposal";
              outputFormat = "pdf";
              date = 1665609977; # date +%s
            })
            (pkgs.stdenv.mkDerivation {
              name = "acm_rep_pres";
              src = ./.;
              buildPhase = ''
                ${pkgs.pandoc}/bin/pandoc \
                  --citeproc \
                  --bibliography=main.bib \
                  --csl=${nix-documents.packages.${system}.citation-style-language-styles}/acm-sig-proceedings.csl \
                  --standalone \
                  --slide-level=2 \
                  --to=revealjs \
                  --output=$out \
                  $src/acm_rep_pres.md
              '';
              installPhase = "true";
            })
          ]);
        });
}
