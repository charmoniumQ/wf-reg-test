# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyUniversalPathlib(PythonPackage):
    """Universal Pathlib is a python library that aims to extend
    Python's built-in pathlib.Path api to use a variety of backend
    filesystems using fsspec."""

    homepage = "https://github.com/fsspec/universal_pathlib"
    pypi = "universal_pathlib/universal_pathlib-0.0.21.tar.gz"

    maintainers = ["charmoniumQ"]

    version("0.0.21", sha256="ed18290f2ded33481a754aac3da94fb6bf78f628027b10c3e95ceb6075415e69")

    # https://github.com/fsspec/universal_pathlib/blob/v0.0.21/pyproject.toml#L19
    depends_on("python@3.7:", type=("build", "run"))

    # https://github.com/fsspec/universal_pathlib/blob/v0.0.21/pyproject.toml#L3
    depends_on("py-flit-core@2:3", type="build")

    # https://github.com/fsspec/universal_pathlib/blob/v0.0.21/pyproject.toml#L18
    depends_on("py-fsspec", type=("build", "run"))
