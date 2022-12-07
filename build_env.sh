#!/usr/bin/env bash

set -e -x

#activate=.spack-env/view/activate.sh
#spack env create --dir . spack.yaml
#spack env activate --sh --dir . > $activate
#set +x
#source .spack-env/view/activate.sh
#set -x
#spack concretize
#spack spec > spack.spec
#spack install

## Spack appends the current env to the activate script, so I will create the activate script in a clean env to avoid leaking unrelated local env vars to the remote.
#TMP_PATH=$(dirname $(/usr/bin/which spack)):$(dirname $(spack python --path))
#env - PATH=$TMP_PATH spack env activate --sh --dir . > $activate
#P=$(realpath --no-symlinks $(dirname $activate))
## Sed is tricky because . means "match any character", but '.' appears in $SPACK_ROOT and $P.
## It would be annoying to escape.
#python -c "import pathlib; p = pathlib.Path('$activate'); p.write_text('P=\$(dirname \$0)\n' + p.read_text().replace('$P', '\$P').replace('$SPACK_ROOT', '\$SPACK_ROOT')).replace('$(dirname $0)', '/does-not-exist')"
#total=$(du --dereference --summarize --bytes .spack-env/view | cut -f1)
total=3871515062
tar --directory=.spack-env --create --dereference view --file=- | tqdm --total $total --bytes | xz --compress > view.tar.xz
