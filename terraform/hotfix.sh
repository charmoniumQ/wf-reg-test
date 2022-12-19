#!/usr/bin/env bash

set -e -x -o nounset

cd $(dirname $(dirname $0))

git add -A
git commit -m --amend
git push

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

ssh -F terraform/ssh_config manager 'source spack/activate.sh && git -C wf-reg-test pull'
ssh -F terraform/ssh_config worker-0 'source spack/activate.sh && git -C wf-reg-test pull'
