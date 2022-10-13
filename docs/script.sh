#!/usr/bin/env sh

set -e -x

nix build --print-build-logs
cp result/*.pdf .
chmod 664 *.pdf
unlink result
