#!/usr/bin/env bash

set -e -x

spack env create wf-reg-test spack.yaml --dir .
spacktivate --dir .
spack concretize
spack install
spacktivate --sh --dir . > .spack-env/view/activate.sh
env --chdir=.spack-env sed -i r/$PWD/\$PWD/g .spack-env/view/activate.sh
tar --directory=.spack-env --create --xz --dereference view --file=../view.tar.xz
gsutil cp env.tar.xz gs://data234/view.tar.xz
