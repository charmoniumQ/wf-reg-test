#!/usr/bin/env bash

set -e -x

git clone -c feature.manyFiles=true https://github.com/spack/spack.git
set +x
source ~/spack/share/spack/setup-env.sh
set -x
git clone https://github.com/charmoniumQ/wf-reg-test
spack repo add wf-reg-test/spack_repo
set -x
spack env create wf-reg-test wf_reg_test/spack.lock
spack env activate wf-reg-test
set +x
spack concretize
for i in $(seq $(nproc)); do
	spack install &
done
wait $(nproc)
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
