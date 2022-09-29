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
                  (nix-documents-lib.markdownDocument {
                    src = nix-utils-lib.mergeDerivations {
                      packageSet = {
                        "." = ./ncsa_delta_proposal;
                      } // nix-utils-lib.packageSet [
                        #self."graphviz.svg"
                      ];
                    };
                    name = "ncsa_delta_proposal.pdf";
                    pdfEngine = "xelatex";
                    outputFormat = "pdf";
                    date = 1664238411; # `date +%s`
                    texlivePackages = nix-documents-lib.pandocTexlivePackages // {
                      inherit (pkgs.texlive)
                        #fancyhdr
                      ;
                    };
                    nixPackages = [ ];
                  })
                ]);
            };
          };
        });
}
