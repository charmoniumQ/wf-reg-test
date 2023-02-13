#!/usr/bin/env bash

set -e -x

# See spack requirements here:
# https://spack.readthedocs.io/en/latest/getting_started.html
sudo apt-get update && sudo apt-get install -y build-essential ca-certificates coreutils curl environment-modules gfortran git gpg lsb-release python3 python3-distutils python3-venv python3-pip unzip zip tmux rustc cargo golang-go

# Install spack
if [ ! -d spack ]; then
    git clone -c feature.manyFiles=true https://github.com/spack/spack.git
fi
git -C spack fetch
git -C spack checkout develop
git -C spack pull origin develop
set +x; source ~/spack/share/spack/setup-env.sh; set -x

# Spack takes too long to build Rust.
spack external find go
spack external find rust
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
spack concretize
# To update packages, add --fresh to the previous line
# Otherwise, Spack defaults to reusing packages that have already been built on this machine.
# Sometimes these spuriously fail due to race conditions
set +e
for i in $(seq 1 $(nproc)); do
    spack install --yes &
done
wait $(jobs -p)
set -e
spack install --yes

if spack spec | grep 'singularityce+suid' ; then
	singularity_conf=$(dirname $(dirname $(readlink $(which singularity))))/etc/singularity/singularity.conf
    stat $singularity_conf | grep Uid
    sudo $(which spack_perms_fix.sh)
    stat $singularity_conf | grep Uid
    grep 'mount tmp' $singularity_conf
fi
