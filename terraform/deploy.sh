#!/usr/bin/env bash

set -e -x -o nounset

cd $(dirname $(dirname $0))

#terraform -chdir=terraform apply -auto-approve

terraform -chdir=terraform output --raw developer_ssh_key > terraform/key
chmod 0600 terraform/key

cat <<EOF > terraform/ssh_config
Host manager
    HostName $(terraform -chdir=terraform output --raw manager_ip)
    IdentityFile ${PWD}/terraform/key
    User azureuser

EOF
ssh-keygen -R "manager"

worker_count=$(terraform -chdir=terraform output --raw worker_count)

for worker in $(seq 0 $((worker_count - 1))); do
    cat <<EOF >> terraform/ssh_config
Host worker-${worker}
    HostName worker-${worker}
    IdentityFile ${PWD}/terraform/key
    User azureuser
    ProxyJump manager

EOF
    ssh-keygen -R "worker-${worker}"
done

for host in manager $(seq 0 $((worker_count - 1)) | xargs -I% echo 'worker-%'); do
    ssh -o StrictHostKeyChecking=no -F terraform/ssh_config $host <<EOF
    set -x
    $(cat spack/setup_env.sh)
    set +x ; source spack/activate.sh ; set -x
    rm -rf wf-reg-test
    git clone https://github.com/charmoniumQ/wf-reg-test

EOF
done
