sudo apt-get install -y gfortran
# Spack assumes libgfortram.so.5 exists, since it existed on the machine which built the env.
rm -f spack.tar.gz
wget https://wfregtest.blob.core.windows.net/deployment/spack.tar.gz
tar --extract --gunzip --file=spack.tar.gz
