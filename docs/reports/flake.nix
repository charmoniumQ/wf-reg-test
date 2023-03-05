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
    {
      templates = {
        default = {
          path = ./templates;
          description = "Template for making documents as a Nix Flake";
        };
      };
    } // flake-utils.lib.eachDefaultSystem
      (system:
        let
          pkgs = nixpkgs.legacyPackages.${system};
          nix-lib = nixpkgs.lib;
          nix-utils-lib = nix-utils.lib.${system};
          nix-documents-lib = nix-documents.lib.${system};
        in
        {
          packages = {
            default = nix-utils-lib.mergeDerivations {
              packageSet = nix-utils-lib.packageSetRec
                (self: [
                  /*
                  (nix-documents-lib.markdownDocument {
                    src = ./.;
                    main = "ncsa_delta_proposal.md";
                    name = "ncsa_delta_proposal.pdf";
                    outputFormat = "pdf";
                    date = 1665609977; # date +%s
                  })
                  (nix-documents-lib.markdownDocument {
                    src = ./.;
                    main = "icse_nier.md";
                    name = "icse_nier.pdf";
                    pandocArgs = ["--template=template.latex"];
                    texlivePackages = nix-documents-lib.pandocTexlivePackages // {
                      inherit (pkgs.texlive)
                        mathspec
                        ieeetran
                        biblatex
                        xkeyval
                        supertabular
                      ;
                    };
                    outputFormat = "pdf";
                    date = 1665609977; # date +%s
                  })
                  */
                  (nix-documents-lib.latexDocument {
                    src = ./.;
                    main = "poster.tex";
                    name = "poster.pdf";
                    texEngine = "pdflatex";
                    texlivePackages = {
                      inherit (pkgs.texlive)
                        adjustbox
                        xcolor
                        xkeyval
                        collectbox
                        anyfontsize
                        framed
                        hyphenat
                        lipsum
                        vwcol
                        environ
                        ragged2e
                        paralist
                        sfmath
                        pgf
                      ;
                    };
                  })
                ]);
            };
          };
        });
}
