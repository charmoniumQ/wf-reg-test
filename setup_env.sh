#!/usr/bin/env sh

curl -output view.tar.xz http://storage.googleapis.com/data234/view.tar.xz
tar --extract --file=view.tar.xz
source view/activate.sh
