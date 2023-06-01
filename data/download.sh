#!/usr/bin/env sh
set -ex
cd $(dirname $(dirname $0))
rm -f data/*.{yaml,pkl,html}
az storage blob download-batch --account-name wfregtest --pattern '*.yaml' --source index3 --destination data
az storage blob download-batch --account-name wfregtest --pattern '*.pkl' --source index3 --destination data
az storage blob download-batch --account-name wfregtest --pattern '*.html' --source index3 --destination data
