#!/usr/bin/env bash

set -e -x

terraform output --raw developer_ssh_key > key

cat <<EOF > ssh_config
Host manager
    HostName $(terraform output --raw manager_ip)
    IdentityFile ~/box/wf-reg-test/terraform/key
    User azureuser

Host worker-0
    HostName worker-0
    IdentityFile ~/box/wf-reg-test/terraform/key
    User azureuser
    ProxyJump manager
EOF
ssh-keygen -f "/home/sam/.ssh/known_hosts" -R "worker-0"
ssh-keygen -f "/home/sam/.ssh/known_hosts" -R "manager"
ssh -F ssh_config manager "if [ -f ~/.ssh/known_hosts ]; then ssh-keygen -f /home/sam/.ssh/known_hosts -R worker-0; fi"

dir=$(mktemp --directory)

terraform output --raw manager_ssh_key > $dir/manager_ssh_key
scp -F ssh_config $dir/manager_ssh_key manager:.ssh/id_rsa
ssh -F ssh_config manager chmod 0600 .ssh/id_rsa

scp -F ssh_config ../spack/setup_env.sh manager:
ssh -F ssh_config manager "if [ ! -d spack ]; then bash setup_env.sh; fi"
scp -F ssh_config ../spack/setup_env.sh worker-0:
ssh -F ssh_config worker-0 "if [ ! -d spack ]; then bash setup_env.sh; fi"

count=$(terraform output --raw worker_count)
python3 -c "print('export PARSL_WORKERS=' + ','.join(f'worker-{i}' for i in range($count)))" > $dir/parsl-worker.sh
scp -F ssh_config $dir/parsl-worker.sh manager:parsl-worker.sh

rm -rf $dir
