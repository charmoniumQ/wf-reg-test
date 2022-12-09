#!/usr/bin/env bash

set -e -x

# See spack requirements here
# https://spack.readthedocs.io/en/latest/getting_started.html
sudo apt-get update
sudo apt-get install -y build-essential ca-certificates coreutils curl environment-modules gfortran git gpg lsb-release python3 python3-distutils python3-venv unzip zip tmux

rm -rf spack
git clone -c feature.manyFiles=true https://github.com/charmoniumQ/spack.git
git -C spack checkout develop-merge
set +x
source ~/spack/share/spack/setup-env.sh
set -x
rm -rf wf-reg-test
git clone https://github.com/charmoniumQ/wf-reg-test
spack repo add wf-reg-test/spack_repo
set -x
spack env create wf-reg-test wf-reg-test/spack/spack.lock
spack env activate wf-reg-test
set +x
spack concretize
for i in $(seq $(nproc)); do
	spack install --yes &
done
wait $(jobs -p)
spack env activate wf-reg-test --sh > spack/activate.sh
total=$(du --summarize --bytes spack | cut -f1)
tar --create --file=- spack | tqdm --total $total --bytes > spack.tar
# python -c <<EOF
# from azure.identity import DefaultAzureCredential
# from azure.storage.blob import BlobClient
# cred = azure.identity.DefaultAzureCredential()
# with open("spack.tar.gz", "rb") as f:
#     blob = BlobClient("https://wfregtest2.blob.core.windows.net", "deployment", "spack.tar.xz", credential=cred)
#     blob.upload_blob(f, overwrite=True)'
# EOF
