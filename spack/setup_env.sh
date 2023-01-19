if ! which tmux; then
    sudo apt-get update
    sudo apt-get install --assume-yes gfortran tmux less nano perl
    # Spack assumes libgfortram.so.5 exists, since it existed on the machine which built the env.
fi

curl --HEAD https://wfregtest.blob.core.windows.net/deployment/spack.tar.gz | grep -v x-ms-request-id | grep -v Date > spack.tar.gz.headers.1
if ! diff spack.tar.gz.headers.1 spack.tar.gz.headers; then
    rm --force spack.tar.gz
    wget https://wfregtest.blob.core.windows.net/deployment/spack.tar.gz
    tar --extract --gunzip --file=spack.tar.gz
    rm spack.tar.gz
    mv spack.tar.gz.headers.1 spack.tar.gz.headers
fi
mv spack.tar.gz.headers.1 spack.tar.gz.headers
