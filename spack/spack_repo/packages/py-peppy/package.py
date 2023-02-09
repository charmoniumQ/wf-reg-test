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


class PyPeppy(PythonPackage):
    """The official python package for reading Portable Encapsulated Projects or PEPs in Python."""

    pypi = "peppy/peppy-0.35.4.tar.gz"

    maintainers = ["charmoniumQ"]

    version("0.35.4", sha256="04338a1b53852c1b30d84d9d333185485725b0097462045397f84c721bab59cd")

    # https://github.com/pepkit/peppy/blob/v0.35.4/setup.py
    depends_on("py-setuptools", type="build")

    # https://github.com/pepkit/peppy/blob/v0.35.4/requirements/requirements-all.txt
    depends_on("py-attmap@0.13.2:", type=("build", "run"))
    depends_on("py-logmuse@0.2:", type=("build", "run"))
    depends_on("py-pandas@0.24.2:", type=("build", "run"))
    depends_on("py-pyyaml", type=("build", "run"))
    depends_on("py-rich@10.3:", type=("build", "run"))
    depends_on("py-ubiquerg@0.6.2:", type=("build", "run"))
