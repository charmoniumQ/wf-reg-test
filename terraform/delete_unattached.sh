#!/usr/bin/env bash

# https://learn.microsoft.com/en-us/azure/virtual-machines/linux/find-unattached-disks
unattachedDiskIds="$(az disk list --query '[?managedBy==`null`].[id]' -o tsv)"
for id in ${unattachedDiskIds[@]}; do
    az disk delete --ids $id --yes
	echo $id
done | tqdm --total=${#unattachedDiskIds[@]}
