#!/usr/bin/env bash

set -e -x -o nounset

cd $(dirname $(dirname $0))

terraform output --raw developer_ssh_key > key

cat <<EOF > terraform/ssh_config
Host manager
    HostName $(terraform -chdir=terraform output --raw manager_ip)
    IdentityFile ~/box/wf-reg-test/terraform/key
    User azureuser
    StrictHostKeyChecking no

EOF
ssh-keygen -R "manager"

worker_count=$(terraform -chdir=terraform output --raw worker_count)

for worker in $(seq 0 $((worker_count - 1))); do
    cat <<EOF >> terraform/ssh_config
Host worker-${worker}
    HostName worker-${worker}
    IdentityFile ~/box/wf-reg-test/terraform/key
    User azureuser
    ProxyJump manager
    StrictHostKeyChecking no

EOF
    ssh-keygen -R "worker-${worker}"
done

for host in manager $(seq 0 $((worker_count - 1)) | xargs -I% echo 'worker-%'); do
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
