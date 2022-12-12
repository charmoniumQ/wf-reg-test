#!/usr/bin/env bash

set -e

# See spack requirements here:
# https://spack.readthedocs.io/en/latest/getting_started.html
sudo apt-get update && sudo apt-get install -y build-essential ca-certificates coreutils curl environment-modules gfortran git gpg lsb-release python3 python3-distutils python3-venv python3-pip unzip zip tmux

# Install spack
if [ ! -d spack ]; then
	git clone -c feature.manyFiles=true https://github.com/charmoniumQ/spack.git
fi
git -C spack checkout develop-merge
source ~/spack/share/spack/setup-env.sh

# Spack takes too long to build Rust.
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
spack external find rust

# Install this environment.
if [ ! -d wf-reg-test ]; then
	git clone https://github.com/charmoniumQ/wf-reg-test
fi
spack repo add wf-reg-test/spack/spack_repo
spack env create wf-reg-test wf-reg-test/spack/spack.yaml
spack env activate wf-reg-test
spack concretize --fresh --force
for i in $(seq $(nproc)); do
	spack install --yes &
done
wait $(jobs -p)

# Create install script:
spack env deactivate
spack env activate wf-reg-test --sh > spack/activate.sh
source spack/activate.sh

# Minimize installation:
# See https://github.com/spack/spack/issues/14695
spack-python <<EOF
from spack.package_base import PackageStillNeededError
from spack.cmd.uninstall import dependent_environments
import spack.store
installed = spack.store.db.query()
for spec in installed:
    if not dependent_environments([spec]):
        print("Removing", spec.name, spec.version)
        try:
            spec.package.do_uninstall()
        except PackageStillNeededError:
            pass
EOF
spack clean --all

# Upload to container archive:
total=$(du --summarize --bytes spack | cut -f1)
tar --create --file=- spack | tqdm --total $total --bytes | gzip - > spack.tar
# Unfortunately, azure-cli in Spack is too old.
pip install azure-cli
export PATH=$PATH:$HOME/.local/bin
az login
az storage blob upload --account-name wfregtest2 --container-name deployment --name spack.tar.gz --file spack.tar.gz --overwrite
