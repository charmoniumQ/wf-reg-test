# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install py-charmonium-time-block
#
# You can edit this file again by typing:
#
#     spack edit py-charmonium-time-block
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class PyCharmoniumTimeBlock(PythonPackage):
    """Time a block of code."""

    pypi = "charmonium.time-block/charmonium.time_block-0.3.0.tar.gz"

    maintainers = ["charmoniumQ"]

    version("0.3.0", sha256="805e93c746c93b8b6cbd5d64dcfd1742ffe06617653677031b917a898a931828")
    version("0.3.1", sha256="19da973fa1f8e450f61743a8f80e04fba3d18e1d79bc9c16b00791b186990116")
    version("0.3.2", sha256="dbd15cf34e753117f25c404594ad984d91d658552a647ea680b1affd2b6374ce")

    patch("fix_poetry.patch", when="@:0.3.1")

    depends_on("python@3.7:", type=("build", "run"))
    depends_on("py-psutil@5.7:", type=("build", "run"))
    depends_on("py-poetry-core@0.12:", type="build")
