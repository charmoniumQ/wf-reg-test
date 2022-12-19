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


class PyElementpath(PythonPackage):
    """XPath 1.0/2.0/3.0 parsers and selectors for ElementTree and lxml"""

    pypi = "elementpath/elementpath-3.0.2.tar.gz"

    maintainers = ["charmoniumQ"]

    version("3.0.2", sha256="cca18742dc0f354f79874c41a906e6ce4cc15230b7858d22a861e1ec5946940f")
    version("2.5.3", sha256="b8aeb6f27dddc10fb9201b62090628a846cbae8577f3544cb1075fa38d0817f6")

    # https://github.com/sissaschool/elementpath/blob/v3.0.2/setup.py
    depends_on("py-setuptools", type="build")
