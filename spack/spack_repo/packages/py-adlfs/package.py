# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyAdlfs(PythonPackage):
    """Filesystem interface to Azure-Datalake Gen1 and Gen2 Storage"""

    pypi = "adlfs/adlfs-2022.11.2.tar.gz"

    maintainers = ["charmoniumQ"]

    version("2022.11.2", sha256="920dba10468f186037ca394dcabcba113532d80f52b315211c8e771be40475ea")

    depends_on("py-fsspec")
    depends_on("py-aiohttp")
    depends_on("py-azure-storage-blob")
    depends_on("py-azure-datalake-store")
