# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyCharmoniumFreeze(PythonPackage):
    """FIXME: Put a proper description of your package here."""

    pypi = "charmonium.freeze/charmonium.freeze-0.5.8.tar.gz"

    maintainers = ["charmoniumQ"]

    version("0.6.0", sha256="7e804c6753f13827df480498d6858e051914d8a4a020b0cb1190af06e90ad4e0")

    depends_on("python@3.7:", type=("build", "run"))
    depends_on("py-psutil@5.7:", type=("build", "run"))
    depends_on("py-poetry-core@0.12:", type="build")
