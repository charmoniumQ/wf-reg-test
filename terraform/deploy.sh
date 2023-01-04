#!/usr/bin/env bash

set -e -x -o nounset

cd $(dirname $(dirname $0))

terraform output --raw developer_ssh_key > key
cat <<EOF > terraform/ssh_config
Host manager
    HostName $(terraform -chdir=terraform output --raw manager_ip)
    IdentityFile ~/box/wf-reg-test/terraform/key
    User azureuser

Host worker-0
    HostName worker-0
    IdentityFile ~/box/wf-reg-test/terraform/key
    User azureuser
    ProxyJump manager
EOF
ssh-keygen -R "worker-0"
ssh-keygen -R "manager"

for host in manager worker-0; do
    ssh -F terraform/ssh_config $host <<EOF
    set -e -x
    if [ ! -d spack ]; then
        wget https://raw.githubusercontent.com/charmoniumQ/wf-reg-test/main/spack/setup_env.sh
        bash setup_env.sh
    fi
    set +x ; source spack/activate.sh ; set -x
    if [ ! -d wf-reg-test ]; then
        git clone https://github.com/charmoniumQ/wf-reg-test
    else
        git -C wf-reg-test pull
    fi
EOF
done
