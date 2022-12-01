#!/usr/bin/env sh

set -e -x

export LD_LIBRARY_PATH=""
nix build --print-build-logs
cp result/*.pdf .
chmod 664 *.pdf
unlink result
