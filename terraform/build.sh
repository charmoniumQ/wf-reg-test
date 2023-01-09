cd $(dirname $(dirname $0))

terraform output --raw developer_ssh_key > key

cat <<EOF > terraform/ssh_config
Host builder
    HostName $(terraform -chdir=terraform output --raw builder_ip)
    IdentityFile ~/box/wf-reg-test/terraform/key
    User azureuser

EOF
ssh -o StrictHostKeyChecking=no -R "builder" curl https://raw.githubusercontent.com/charmoniumQ/wf-reg-test/main/spack/build_env.sh | bash
