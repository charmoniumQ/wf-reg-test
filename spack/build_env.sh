#!/usr/bin/env bash

set -e

# See spack requirements here:
# https://spack.readthedocs.io/en/latest/getting_started.html
sudo apt-get update && sudo apt-get install -y build-essential ca-certificates coreutils curl environment-modules gfortran git gpg lsb-release python3 python3-distutils python3-venv python3-pip unzip zip tmux cmake rustc cargo perl

# Install spack
if [ ! -d spack ]; then
    git clone -c feature.manyFiles=true https://github.com/spack/spack.git
fi
git -C spack fetch
git -C spack checkout develop
git -C spack pull origin develop
source ~/spack/share/spack/setup-env.sh

# Spack takes too long to build Rust.
spack external find rust
spack external find perl
spack external find cmake
# Note, `spack external find` will NOT work for run-time deps,
# as the workers will not have this package.
# For reproducibility's sake, I try not to overuse it on build-time deps either.

# Install this environment.
if [ ! -d wf-reg-test ]; then
    git clone https://github.com/charmoniumQ/wf-reg-test
fi
git -C wf-reg-test pull origin
if ! spack repo list | grep spack_repo; then
    spack repo add wf-reg-test/spack/spack_repo
fi

if [ -d spack/var/spack/environments/wf-reg-test/ ]; then
    echo y | spack env remove wf-reg-test
fi
spack env create wf-reg-test wf-reg-test/spack/spack.yaml
spack env activate wf-reg-test
spack concretize --fresh --force
# Sometimes these spuriously fail due to race conditions
set +e
for i in $(seq 1 $(nproc)); do
    spack install --yes &
done
wait $(jobs -p)
set -e
spack install --yes

# Create install script:
spack env deactivate --sh > spack/deactivate.sh
source spack/deactivate.sh
spack env activate wf-reg-test --sh > spack/activate.sh
source spack/activate.sh

# Minimize installation:
# spack gc
# See https://github.com/spack/spack/issues/14695
spack-python <<EOF
from spack.cmd.uninstall import dependent_environments
import spack.store
from spack.package import PackageStillNeededError
installed = spack.store.db.query()
for spec in installed:
    if not dependent_environments([spec]):
        print("Uninstalling", spec.name, spec.version)
        try:
            spec.package.do_uninstall()
        except PackageStillNeededError as e:
            pass
EOF
spack clean --all

# Upload to container archive:
total=$(du --summarize --bytes spack | cut -f1)
tar --create --file=- spack | tqdm --total $total --bytes | gzip - > spack.tar.gz
# Unfortunately, azure-cli in Spack is too old.
export PATH=$PATH:$HOME/.local/bin
pip install --user azure-cli
az login
az storage blob upload --account-name wfregtest --container-name deployment --name spack.tar.gz --file spack.tar.gz --overwrite
