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
                        "index.md" = ./ncsa_delta_proposal.md;
                        "main.bib" = ./main.bib;
                        "predictive_maintenance.png" = ./predictive_maintenance.png;
                      };
                    };
                    name = "ncsa_delta_proposal.pdf";
                    outputFormat = "pdf";
                    date = 1665609977; # date +%s
                  })
                  (nix-documents-lib.markdownDocument {
                    src = nix-utils-lib.mergeDerivations {
                      packageSet = {
                        "index.md" = ./icse_nier.md;
                        "main.bib" = ./main.bib;
                        "predictive_maintenance.png" = ./predictive_maintenance.png;
                      };
                    };
                    name = "icse_nier.pdf";
                    outputFormat = "pdf";
                    date = 1665609977; # date +%s
                  })
                ]);
            };
          };
        });
}
