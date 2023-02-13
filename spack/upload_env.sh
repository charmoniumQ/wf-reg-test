#!/usr/bin/env bash

set -x -e

# Create install script:
spack env deactivate --sh > spack/deactivate.sh
set +x; source spack/deactivate.sh; set -x
spack env activate wf-reg-test --sh > spack/activate.sh
set +x; source spack/activate.sh; set -x

# Minimize installation:
# See https://github.com/spack/spack/issues/14695
spack-python <<EOF
from spack.cmd.uninstall import dependent_environments
import spack.store
from spack.package_base import PackageStillNeededError
installed = spack.store.db.query()
for spec in installed:
    if not dependent_environments([spec]):
        print("Uninstalling", spec.name, spec.version)
        try:
            spec.package.do_uninstall()
        except PackageStillNeededError as e:
            pass
EOF
spack gc --yes-to-all
spack clean --all

# Singularity fun hacks; very inelegant, but I think necessary.
# https://github.com/nf-core/eager/issues/894#issuecomment-1428611633
#sudo spack_perms_fix.sh
#sudo sed -i '/^mount tmp = .*/mount tmp = no/' $(dirname $(dirname $(readlink $(which singularity))))/etc/singularity/singularity.conf

# Upload to container archive:
total=$(du --summarize --bytes spack | cut --fields=1)
tar --create --file=- spack | tqdm --total $total --bytes | gzip - > spack.tar.gz
# Unfortunately, azure-cli in Spack is too old.
export PATH=$PATH:$HOME/.local/bin
if ! which az > /dev/null; then
	pip install --user azure-cli
fi
if ! az ad signed-in-user show; then
	az login
fi
az storage blob upload --account-name wfregtest --container-name deployment --name spack.tar.gz --file spack.tar.gz --overwrite
curl --silent --HEAD https://wfregtest.blob.core.windows.net/deployment/spack.tar.gz | grep Last-Modified > spack.tar.gz.headers
