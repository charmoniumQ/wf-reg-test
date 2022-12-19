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


class PyDomonic(PythonPackage):
    """Generate html with python 3. DOM API, Javascript API and more..."""

    pypi = "domonic/domonic-0.9.11.tar.gz"

    maintainers = ["charmoniumQ"]

    depends_on("py-setuptools", type="build")

    #
    depends_on("py-poetry-core@0.12:", type="build")
