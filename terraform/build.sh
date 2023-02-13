#!/usr/bin/env bash

set -e -x -o nounset

cd $(dirname $(dirname $0))

terraform -chdir=terraform output --raw developer_ssh_key > terraform/key
chmod 0600 terraform/key

cat <<EOF > terraform/ssh_config
Host manager
    HostName $(terraform -chdir=terraform output --raw manager_ip)
    IdentityFile ${PWD}/terraform/key
    User azureuser

Host builder
    HostName $(terraform -chdir=terraform output --raw builder_ip)
    IdentityFile ~/box/wf-reg-test/terraform/key
    User azureuser

EOF

ssh -o StrictHostKeyChecking=no -F terraform/ssh_config builder "$(cat spack/build_env.sh)"
