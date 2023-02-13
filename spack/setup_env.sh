if ! which tmux > /dev/null; then
    sudo apt-get update
    sudo apt-get install --assume-yes gfortran tmux
    # Spack assumes libgfortram.so.5 exists, since it existed on the machine which built the env.
    # TODO: move tmux less nano perl to spack build
fi

curl --silent --HEAD https://wfregtest.blob.core.windows.net/deployment/spack.tar.gz | grep Last-Modified > spack.tar.gz.headers.1
if ! diff spack.tar.gz.headers.1 spack.tar.gz.headers; then
    wget --no-verbose https://wfregtest.blob.core.windows.net/deployment/spack.tar.gz --output-document=spack.tar.gz
    # Must remove old spack because otherwise tar will overlay
    sudo rm -rf spack
    # sudo, because the singularity config needs to be owned by root.
    sudo tar --extract --gunzip --file=spack.tar.gz
    rm spack.tar.gz
fi

mv spack.tar.gz.headers.1 spack.tar.gz.headers
