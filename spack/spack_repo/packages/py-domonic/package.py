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

    # pypi = "domonic/domonic-0.9.11.tar.gz"
    # The PyPI release does not have `requirements.txt`, which `setup.py` wants to read.
    url = "https://github.com/byteface/domonic/archive/0.9.11.tar.gz"

    maintainers = ["charmoniumQ"]

    version("0.9.11", sha256="05fcc95b10fd4f15438159b7b7f47cc72851bdabfcfc3fd52f359bbc909b4faf")

    # https://github.com/byteface/domonic/blob/0.9.11/setup.py
    depends_on("py-setuptools", type="build")

    # https://github.com/byteface/domonic/blob/0.9.11/requirements.txt
    depends_on("py-elementpath@2.5.2:2.5", type=("build", "run"))
    depends_on("py-python-dateutil@2.8.2", type=("build", "run"))
    depends_on("py-requests@2.28", type=("build", "run"))
    depends_on("py-urllib3@1.26.9:1.26", type=("build", "run"))
    depends_on("py-html5lib@1.1:1", type=("build", "run"))
    depends_on("py-cssselect@1.1", type=("build", "run"))
