#!/usr/bin/env bash

set -e -x -o nounset

cd $(dirname $(dirname $0))

terraform -chdir=terraform output --raw developer_ssh_key > terraform/key
chmod 0600 terraform/key

cat <<EOF > terraform/ssh_config
Host manager
    HostName $(terraform -chdir=terraform output --raw manager_ip)
    IdentityFile ~/box/wf-reg-test/terraform/key
    User azureuser

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

EOF
    ssh-keygen -R "worker-${worker}"
done

for host in manager $(seq 0 $((worker_count - 1)) | xargs -I% echo 'worker-%'); do
    ssh -o StrictHostKeyChecking=no -F terraform/ssh_config $host <<EOF
    set -e -x
    # rm -rf spack spack.tar.gz
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
