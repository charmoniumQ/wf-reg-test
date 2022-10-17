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
                        "template.latex" = ./template.latex;
                      };
                    };
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
                    name = "icse_nier.pdf";
                    outputFormat = "pdf";
                    date = 1665609977; # date +%s
                  })
                ]);
            };
          };
        });
}
# pandoc --to=latex --output=icse_nier.tex icse_nier.md --csl=/nix/store/0ybr8rd2g6kmqyp436cwhg1v18ag23v9-citation-style-language-styles/ieee-with-url.csl --lua-filter=/nix/store/r79wajcz3kkn7j18spxhn6n36ghbvp1z-pandoc-lua-filters-2021-11-05/share/pandoc/filters/abstract-to-meta.lua --lua-filter=/nix/store/r79wajcz3kkn7j18spxhn6n36ghbvp1z-pandoc-lua-filters-2021-11-05/share/pandoc/filters/pagebreak.lua --lua-filter=/nix/store/r79wajcz3kkn7j18spxhn6n36ghbvp1z-pandoc-lua-filters-2021-11-05/share/pandoc/filters/cito.lua --filter=/nix/store/a0pinsq304hk5zmr3xddbhw7r4n7qlw0-pandoc-crossref-0.3.13.0/bin/pandoc-crossref --verbose --template=template.tex
