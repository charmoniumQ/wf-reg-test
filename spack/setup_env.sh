set -e
echo "$(hostname): setting up"

sudo rm -rf /etc/update-motd.d /var/run/motd.dynamic ~/tmp ~/.singularity /tmp/conda ~/.conda /tmp/bundle-temp-* /tmp/build-temp-*

if ! which tmux > /dev/null; then
	echo "$(hostname): needs to apt-get"
    sudo apt-get update > /dev/null
    sudo apt-get install --assume-yes gfortran tmux > /dev/null
    # Spack assumes libgfortram.so.5 exists, since it existed on the machine which built the env.
    # TODO: move tmux less nano perl to spack build
fi

curl --silent --HEAD https://wfregtest.blob.core.windows.net/deployment/spack.tar.gz | grep Last-Modified > spack.tar.gz.headers.1
if ! diff spack.tar.gz.headers.1 spack.tar.gz.headers > /dev/null; then
	echo "$(hostname): needs to curl spack"
    wget --quiet https://wfregtest.blob.core.windows.net/deployment/spack.tar.gz --output-document=spack.tar.gz
    # Must remove old spack because otherwise tar will overlay
    sudo rm -rf spack
    # sudo, because the singularity config needs to be owned by root.
    sudo tar --extract --gunzip --file=spack.tar.gz
    rm spack.tar.gz
fi
mv spack.tar.gz.headers.1 spack.tar.gz.headers

source spack/activate.sh

if [ -d wf-reg-test ]; then
    git -C wf-reg-test fetch --quiet
    if [ -n "$(git -C wf-reg-test diff main origin/main)" ]; then
        echo "$(hostname): updating git commit for wf-reg-test"
        git -C wf-reg-test reset --hard --quiet @{u}
    fi
else
    echo "$(hostname): git clone wf-reg-test"
    git clone --quiet https://github.com/charmoniumQ/wf-reg-test
fi
