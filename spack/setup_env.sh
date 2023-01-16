set -e -x
sudo apt-get update
sudo apt-get install --assume-yes gfortran tmux
# Spack assumes libgfortram.so.5 exists, since it existed on the machine which built the env.
rm --force spack.tar.gz
wget https://wfregtest.blob.core.windows.net/deployment/spack.tar.gz
tar --extract --gunzip --file=spack.tar.gz
rm spack.tar.gz
