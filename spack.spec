Input spec
--------------------------------
coreutils

Concretized
--------------------------------
coreutils@9.1%gcc@12.2.0~gprefix build_system=autotools patches=8f50e8a arch=linux-rhel7-x86_64_v4

Input spec
--------------------------------
hwloc

Concretized
--------------------------------
hwloc@2.8.0%gcc@12.2.0~cairo~cuda~gl~libudev+libxml2~netloc~nvml~oneapi-level-zero~opencl+pci~rocm libs=shared,static arch=linux-rhel7-x86_64_v4
    ^libpciaccess@0.16%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^libtool@2.4.7%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
            ^m4@1.4.19%gcc@12.2.0+sigsegv patches=9dc5fbd,bfdffa7 arch=linux-rhel7-x86_64_v4
                ^diffutils@3.8%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
                ^libsigsegv@2.13%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^util-macros@1.19.3%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^libxml2@2.10.1%gcc@12.2.0~python arch=linux-rhel7-x86_64_v4
        ^libiconv@1.16%gcc@12.2.0 libs=shared,static arch=linux-rhel7-x86_64_v4
        ^xz@5.2.5%gcc@12.2.0~pic libs=shared,static arch=linux-rhel7-x86_64_v4
        ^zlib@1.2.12%gcc@12.2.0+optimize+pic+shared patches=0d38234 arch=linux-rhel7-x86_64_v4
    ^ncurses@6.3%gcc@12.2.0~symlinks+termlib abi=none arch=linux-rhel7-x86_64_v4
    ^pkgconf@1.8.0%gcc@12.2.0 arch=linux-rhel7-x86_64_v4

Input spec
--------------------------------
java

Concretized
--------------------------------
openjdk@11.0.15_10%gcc@12.2.0 arch=linux-rhel7-x86_64_v4

Input spec
--------------------------------
miniconda3

Concretized
--------------------------------
miniconda3@4.10.3%gcc@12.2.0 build_system=generic arch=linux-rhel7-x86_64_v4

Input spec
--------------------------------
nextflow

Concretized
--------------------------------
nextflow@22.04.4%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^openjdk@11.0.15_10%gcc@12.2.0 arch=linux-rhel7-x86_64_v4

Input spec
--------------------------------
py-charmonium-freeze@0.6.0

Concretized
--------------------------------
py-charmonium-freeze@0.6.0%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^py-pip@22.1.2%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^py-poetry-core@1.2.0%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^py-psutil@5.8.0%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^py-setuptools@65.0.0%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^py-wheel@0.37.1%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^python@3.10.6%gcc@12.2.0+bz2+ctypes+dbm~debug+libxml2+lzma~nis~optimizations+pic+pyexpat+pythoncmd+readline+shared+sqlite3+ssl~tix~tkinter~ucs4+uuid+zlib patches=0d98e93,7d40923,f2fd060 arch=linux-rhel7-x86_64_v4
        ^bzip2@1.0.8%gcc@12.2.0~debug~pic+shared arch=linux-rhel7-x86_64_v4
            ^diffutils@3.8%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^expat@2.4.8%gcc@12.2.0+libbsd arch=linux-rhel7-x86_64_v4
            ^libbsd@0.11.5%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
                ^libmd@1.0.4%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^gdbm@1.19%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^gettext@0.21%gcc@12.2.0+bzip2+curses+git~libunistring+libxml2+tar+xz arch=linux-rhel7-x86_64_v4
            ^libiconv@1.16%gcc@12.2.0 libs=shared,static arch=linux-rhel7-x86_64_v4
            ^libxml2@2.10.1%gcc@12.2.0~python arch=linux-rhel7-x86_64_v4
            ^tar@1.34%gcc@12.2.0 zip=pigz arch=linux-rhel7-x86_64_v4
                ^pigz@2.7%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
                ^zstd@1.5.2%gcc@12.2.0+programs compression=none libs=shared,static arch=linux-rhel7-x86_64_v4
        ^libffi@3.4.2%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^ncurses@6.3%gcc@12.2.0~symlinks+termlib abi=none arch=linux-rhel7-x86_64_v4
        ^openssl@1.1.1q%gcc@12.2.0~docs~shared certs=mozilla patches=3fdcf2d arch=linux-rhel7-x86_64_v4
            ^ca-certificates-mozilla@2022-07-19%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
            ^perl@5.34.1%gcc@12.2.0+cpanm+shared+threads arch=linux-rhel7-x86_64_v4
                ^berkeley-db@18.1.40%gcc@12.2.0+cxx~docs+stl patches=26090f4,b231fcc arch=linux-rhel7-x86_64_v4
        ^pkgconf@1.8.0%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^readline@8.1.2%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^sqlite@3.39.2%gcc@12.2.0+column_metadata+dynamic_extensions+fts~functions+rtree arch=linux-rhel7-x86_64_v4
        ^util-linux-uuid@2.37.4%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^xz@5.2.5%gcc@12.2.0~pic libs=shared,static arch=linux-rhel7-x86_64_v4
        ^zlib@1.2.12%gcc@12.2.0+optimize+pic+shared patches=0d38234 arch=linux-rhel7-x86_64_v4

Input spec
--------------------------------
py-charmonium-time-block patches=2ca26cf

Concretized
--------------------------------
py-charmonium-time-block@0.3.0%gcc@12.2.0 build_system=python_pip patches=2ca26cf arch=linux-rhel7-x86_64_v4
    ^py-pip@22.1.2%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^py-poetry-core@1.2.0%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^py-psutil@5.8.0%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^py-setuptools@65.0.0%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^py-wheel@0.37.1%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^python@3.10.6%gcc@12.2.0+bz2+ctypes+dbm~debug+libxml2+lzma~nis~optimizations+pic+pyexpat+pythoncmd+readline+shared+sqlite3+ssl~tix~tkinter~ucs4+uuid+zlib patches=0d98e93,7d40923,f2fd060 arch=linux-rhel7-x86_64_v4
        ^bzip2@1.0.8%gcc@12.2.0~debug~pic+shared arch=linux-rhel7-x86_64_v4
            ^diffutils@3.8%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^expat@2.4.8%gcc@12.2.0+libbsd arch=linux-rhel7-x86_64_v4
            ^libbsd@0.11.5%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
                ^libmd@1.0.4%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^gdbm@1.19%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^gettext@0.21%gcc@12.2.0+bzip2+curses+git~libunistring+libxml2+tar+xz arch=linux-rhel7-x86_64_v4
            ^libiconv@1.16%gcc@12.2.0 libs=shared,static arch=linux-rhel7-x86_64_v4
            ^libxml2@2.10.1%gcc@12.2.0~python arch=linux-rhel7-x86_64_v4
            ^tar@1.34%gcc@12.2.0 zip=pigz arch=linux-rhel7-x86_64_v4
                ^pigz@2.7%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
                ^zstd@1.5.2%gcc@12.2.0+programs compression=none libs=shared,static arch=linux-rhel7-x86_64_v4
        ^libffi@3.4.2%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^ncurses@6.3%gcc@12.2.0~symlinks+termlib abi=none arch=linux-rhel7-x86_64_v4
        ^openssl@1.1.1q%gcc@12.2.0~docs~shared certs=mozilla patches=3fdcf2d arch=linux-rhel7-x86_64_v4
            ^ca-certificates-mozilla@2022-07-19%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
            ^perl@5.34.1%gcc@12.2.0+cpanm+shared+threads arch=linux-rhel7-x86_64_v4
                ^berkeley-db@18.1.40%gcc@12.2.0+cxx~docs+stl patches=26090f4,b231fcc arch=linux-rhel7-x86_64_v4
        ^pkgconf@1.8.0%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^readline@8.1.2%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^sqlite@3.39.2%gcc@12.2.0+column_metadata+dynamic_extensions+fts~functions+rtree arch=linux-rhel7-x86_64_v4
        ^util-linux-uuid@2.37.4%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^xz@5.2.5%gcc@12.2.0~pic libs=shared,static arch=linux-rhel7-x86_64_v4
        ^zlib@1.2.12%gcc@12.2.0+optimize+pic+shared patches=0d38234 arch=linux-rhel7-x86_64_v4

Input spec
--------------------------------
py-click

Concretized
--------------------------------
py-click@8.1.3%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^py-pip@22.1.2%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^py-setuptools@59.4.0%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^py-wheel@0.37.1%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^python@3.10.6%gcc@12.2.0+bz2+ctypes+dbm~debug+libxml2+lzma~nis~optimizations+pic+pyexpat+pythoncmd+readline+shared+sqlite3+ssl~tix~tkinter~ucs4+uuid+zlib patches=0d98e93,7d40923,f2fd060 arch=linux-rhel7-x86_64_v4
        ^bzip2@1.0.8%gcc@12.2.0~debug~pic+shared arch=linux-rhel7-x86_64_v4
            ^diffutils@3.8%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^expat@2.4.8%gcc@12.2.0+libbsd arch=linux-rhel7-x86_64_v4
            ^libbsd@0.11.5%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
                ^libmd@1.0.4%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^gdbm@1.19%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^gettext@0.21%gcc@12.2.0+bzip2+curses+git~libunistring+libxml2+tar+xz arch=linux-rhel7-x86_64_v4
            ^libiconv@1.16%gcc@12.2.0 libs=shared,static arch=linux-rhel7-x86_64_v4
            ^libxml2@2.10.1%gcc@12.2.0~python arch=linux-rhel7-x86_64_v4
            ^tar@1.34%gcc@12.2.0 zip=pigz arch=linux-rhel7-x86_64_v4
                ^pigz@2.7%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
                ^zstd@1.5.2%gcc@12.2.0+programs compression=none libs=shared,static arch=linux-rhel7-x86_64_v4
        ^libffi@3.4.2%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^ncurses@6.3%gcc@12.2.0~symlinks+termlib abi=none arch=linux-rhel7-x86_64_v4
        ^openssl@1.1.1q%gcc@12.2.0~docs~shared certs=mozilla patches=3fdcf2d arch=linux-rhel7-x86_64_v4
            ^ca-certificates-mozilla@2022-07-19%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
            ^perl@5.34.1%gcc@12.2.0+cpanm+shared+threads arch=linux-rhel7-x86_64_v4
                ^berkeley-db@18.1.40%gcc@12.2.0+cxx~docs+stl patches=26090f4,b231fcc arch=linux-rhel7-x86_64_v4
        ^pkgconf@1.8.0%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^readline@8.1.2%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^sqlite@3.39.2%gcc@12.2.0+column_metadata+dynamic_extensions+fts~functions+rtree arch=linux-rhel7-x86_64_v4
        ^util-linux-uuid@2.37.4%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^xz@5.2.5%gcc@12.2.0~pic libs=shared,static arch=linux-rhel7-x86_64_v4
        ^zlib@1.2.12%gcc@12.2.0+optimize+pic+shared patches=0d38234 arch=linux-rhel7-x86_64_v4

Input spec
--------------------------------
py-dask

Concretized
--------------------------------
py-dask@2022.10.2%gcc@12.2.0+array+bag+dataframe+delayed~diagnostics~distributed+yaml build_system=python_pip arch=linux-rhel7-x86_64_v4
    ^py-cloudpickle@1.6.0%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^py-fsspec@2022.11.0%gcc@12.2.0~http build_system=python_pip arch=linux-rhel7-x86_64_v4
    ^py-numpy@1.23.3%gcc@12.2.0+blas+lapack patches=873745d arch=linux-rhel7-x86_64_v4
        ^openblas@0.3.20%gcc@12.2.0~bignuma~consistent_fpcsr~ilp64+locking+pic+shared patches=9f12903 symbol_suffix=none threads=none arch=linux-rhel7-x86_64_v4
            ^perl@5.34.1%gcc@12.2.0+cpanm+shared+threads arch=linux-rhel7-x86_64_v4
                ^berkeley-db@18.1.40%gcc@12.2.0+cxx~docs+stl patches=26090f4,b231fcc arch=linux-rhel7-x86_64_v4
        ^py-cython@0.29.32%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^py-pandas@1.5.1%gcc@12.2.0 build_system=python_pip arch=linux-rhel7-x86_64_v4
        ^py-bottleneck@1.3.5%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
            ^py-versioneer@0.26%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^py-numexpr@2.8.3%gcc@12.2.0 build_system=python_pip arch=linux-rhel7-x86_64_v4
            ^py-packaging@21.3%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
                ^py-pyparsing@3.0.9%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
                    ^py-flit-core@3.7.1%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^py-python-dateutil@2.8.2%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
            ^py-setuptools-scm@7.0.5%gcc@12.2.0+toml arch=linux-rhel7-x86_64_v4
                ^py-tomli@2.0.1%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
                ^py-typing-extensions@4.3.0%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
            ^py-six@1.16.0%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^py-pytz@2022.2.1%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^py-partd@1.1.0%gcc@12.2.0 build_system=python_pip arch=linux-rhel7-x86_64_v4
        ^py-locket@0.2.0%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^py-pip@22.1.2%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^py-pyyaml@6.0%gcc@12.2.0+libyaml arch=linux-rhel7-x86_64_v4
        ^libyaml@0.2.5%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^py-cython@0.29.32%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^py-setuptools@65.0.0%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^py-setuptools@59.4.0%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^py-toolz@0.12.0%gcc@12.2.0 build_system=python_pip arch=linux-rhel7-x86_64_v4
    ^py-wheel@0.37.1%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^python@3.10.6%gcc@12.2.0+bz2+ctypes+dbm~debug+libxml2+lzma~nis~optimizations+pic+pyexpat+pythoncmd+readline+shared+sqlite3+ssl~tix~tkinter~ucs4+uuid+zlib patches=0d98e93,7d40923,f2fd060 arch=linux-rhel7-x86_64_v4
        ^bzip2@1.0.8%gcc@12.2.0~debug~pic+shared arch=linux-rhel7-x86_64_v4
            ^diffutils@3.8%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^expat@2.4.8%gcc@12.2.0+libbsd arch=linux-rhel7-x86_64_v4
            ^libbsd@0.11.5%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
                ^libmd@1.0.4%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^gdbm@1.19%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^gettext@0.21%gcc@12.2.0+bzip2+curses+git~libunistring+libxml2+tar+xz arch=linux-rhel7-x86_64_v4
            ^libiconv@1.16%gcc@12.2.0 libs=shared,static arch=linux-rhel7-x86_64_v4
            ^libxml2@2.10.1%gcc@12.2.0~python arch=linux-rhel7-x86_64_v4
            ^tar@1.34%gcc@12.2.0 zip=pigz arch=linux-rhel7-x86_64_v4
                ^pigz@2.7%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
                ^zstd@1.5.2%gcc@12.2.0+programs compression=none libs=shared,static arch=linux-rhel7-x86_64_v4
        ^libffi@3.4.2%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^ncurses@6.3%gcc@12.2.0~symlinks+termlib abi=none arch=linux-rhel7-x86_64_v4
        ^openssl@1.1.1q%gcc@12.2.0~docs~shared certs=mozilla patches=3fdcf2d arch=linux-rhel7-x86_64_v4
            ^ca-certificates-mozilla@2022-07-19%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^pkgconf@1.8.0%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^readline@8.1.2%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^sqlite@3.39.2%gcc@12.2.0+column_metadata+dynamic_extensions+fts~functions+rtree arch=linux-rhel7-x86_64_v4
        ^util-linux-uuid@2.37.4%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^xz@5.2.5%gcc@12.2.0~pic libs=shared,static arch=linux-rhel7-x86_64_v4
        ^zlib@1.2.12%gcc@12.2.0+optimize+pic+shared patches=0d38234 arch=linux-rhel7-x86_64_v4

Input spec
--------------------------------
py-dask@2022.10.2~distributed

Concretized
--------------------------------
py-dask@2022.10.2%gcc@12.2.0+array+bag+dataframe+delayed~diagnostics~distributed+yaml build_system=python_pip arch=linux-rhel7-x86_64_v4
    ^py-cloudpickle@1.6.0%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^py-fsspec@2022.11.0%gcc@12.2.0~http build_system=python_pip arch=linux-rhel7-x86_64_v4
    ^py-numpy@1.23.3%gcc@12.2.0+blas+lapack patches=873745d arch=linux-rhel7-x86_64_v4
        ^openblas@0.3.20%gcc@12.2.0~bignuma~consistent_fpcsr~ilp64+locking+pic+shared patches=9f12903 symbol_suffix=none threads=none arch=linux-rhel7-x86_64_v4
            ^perl@5.34.1%gcc@12.2.0+cpanm+shared+threads arch=linux-rhel7-x86_64_v4
                ^berkeley-db@18.1.40%gcc@12.2.0+cxx~docs+stl patches=26090f4,b231fcc arch=linux-rhel7-x86_64_v4
        ^py-cython@0.29.32%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^py-pandas@1.5.1%gcc@12.2.0 build_system=python_pip arch=linux-rhel7-x86_64_v4
        ^py-bottleneck@1.3.5%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
            ^py-versioneer@0.26%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^py-numexpr@2.8.3%gcc@12.2.0 build_system=python_pip arch=linux-rhel7-x86_64_v4
            ^py-packaging@21.3%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
                ^py-pyparsing@3.0.9%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
                    ^py-flit-core@3.7.1%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^py-python-dateutil@2.8.2%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
            ^py-setuptools-scm@7.0.5%gcc@12.2.0+toml arch=linux-rhel7-x86_64_v4
                ^py-tomli@2.0.1%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
                ^py-typing-extensions@4.3.0%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
            ^py-six@1.16.0%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^py-pytz@2022.2.1%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^py-partd@1.1.0%gcc@12.2.0 build_system=python_pip arch=linux-rhel7-x86_64_v4
        ^py-locket@0.2.0%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^py-pip@22.1.2%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^py-pyyaml@6.0%gcc@12.2.0+libyaml arch=linux-rhel7-x86_64_v4
        ^libyaml@0.2.5%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^py-cython@0.29.32%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^py-setuptools@65.0.0%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^py-setuptools@59.4.0%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^py-toolz@0.12.0%gcc@12.2.0 build_system=python_pip arch=linux-rhel7-x86_64_v4
    ^py-wheel@0.37.1%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^python@3.10.6%gcc@12.2.0+bz2+ctypes+dbm~debug+libxml2+lzma~nis~optimizations+pic+pyexpat+pythoncmd+readline+shared+sqlite3+ssl~tix~tkinter~ucs4+uuid+zlib patches=0d98e93,7d40923,f2fd060 arch=linux-rhel7-x86_64_v4
        ^bzip2@1.0.8%gcc@12.2.0~debug~pic+shared arch=linux-rhel7-x86_64_v4
            ^diffutils@3.8%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^expat@2.4.8%gcc@12.2.0+libbsd arch=linux-rhel7-x86_64_v4
            ^libbsd@0.11.5%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
                ^libmd@1.0.4%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^gdbm@1.19%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^gettext@0.21%gcc@12.2.0+bzip2+curses+git~libunistring+libxml2+tar+xz arch=linux-rhel7-x86_64_v4
            ^libiconv@1.16%gcc@12.2.0 libs=shared,static arch=linux-rhel7-x86_64_v4
            ^libxml2@2.10.1%gcc@12.2.0~python arch=linux-rhel7-x86_64_v4
            ^tar@1.34%gcc@12.2.0 zip=pigz arch=linux-rhel7-x86_64_v4
                ^pigz@2.7%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
                ^zstd@1.5.2%gcc@12.2.0+programs compression=none libs=shared,static arch=linux-rhel7-x86_64_v4
        ^libffi@3.4.2%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^ncurses@6.3%gcc@12.2.0~symlinks+termlib abi=none arch=linux-rhel7-x86_64_v4
        ^openssl@1.1.1q%gcc@12.2.0~docs~shared certs=mozilla patches=3fdcf2d arch=linux-rhel7-x86_64_v4
            ^ca-certificates-mozilla@2022-07-19%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^pkgconf@1.8.0%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^readline@8.1.2%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^sqlite@3.39.2%gcc@12.2.0+column_metadata+dynamic_extensions+fts~functions+rtree arch=linux-rhel7-x86_64_v4
        ^util-linux-uuid@2.37.4%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^xz@5.2.5%gcc@12.2.0~pic libs=shared,static arch=linux-rhel7-x86_64_v4
        ^zlib@1.2.12%gcc@12.2.0+optimize+pic+shared patches=0d38234 arch=linux-rhel7-x86_64_v4

Input spec
--------------------------------
py-fasteners

Concretized
--------------------------------
py-fasteners@0.18%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^py-pip@22.1.2%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^py-setuptools@59.4.0%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^py-wheel@0.37.1%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^python@3.10.6%gcc@12.2.0+bz2+ctypes+dbm~debug+libxml2+lzma~nis~optimizations+pic+pyexpat+pythoncmd+readline+shared+sqlite3+ssl~tix~tkinter~ucs4+uuid+zlib patches=0d98e93,7d40923,f2fd060 arch=linux-rhel7-x86_64_v4
        ^bzip2@1.0.8%gcc@12.2.0~debug~pic+shared arch=linux-rhel7-x86_64_v4
            ^diffutils@3.8%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^expat@2.4.8%gcc@12.2.0+libbsd arch=linux-rhel7-x86_64_v4
            ^libbsd@0.11.5%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
                ^libmd@1.0.4%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^gdbm@1.19%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^gettext@0.21%gcc@12.2.0+bzip2+curses+git~libunistring+libxml2+tar+xz arch=linux-rhel7-x86_64_v4
            ^libiconv@1.16%gcc@12.2.0 libs=shared,static arch=linux-rhel7-x86_64_v4
            ^libxml2@2.10.1%gcc@12.2.0~python arch=linux-rhel7-x86_64_v4
            ^tar@1.34%gcc@12.2.0 zip=pigz arch=linux-rhel7-x86_64_v4
                ^pigz@2.7%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
                ^zstd@1.5.2%gcc@12.2.0+programs compression=none libs=shared,static arch=linux-rhel7-x86_64_v4
        ^libffi@3.4.2%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^ncurses@6.3%gcc@12.2.0~symlinks+termlib abi=none arch=linux-rhel7-x86_64_v4
        ^openssl@1.1.1q%gcc@12.2.0~docs~shared certs=mozilla patches=3fdcf2d arch=linux-rhel7-x86_64_v4
            ^ca-certificates-mozilla@2022-07-19%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
            ^perl@5.34.1%gcc@12.2.0+cpanm+shared+threads arch=linux-rhel7-x86_64_v4
                ^berkeley-db@18.1.40%gcc@12.2.0+cxx~docs+stl patches=26090f4,b231fcc arch=linux-rhel7-x86_64_v4
        ^pkgconf@1.8.0%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^readline@8.1.2%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^sqlite@3.39.2%gcc@12.2.0+column_metadata+dynamic_extensions+fts~functions+rtree arch=linux-rhel7-x86_64_v4
        ^util-linux-uuid@2.37.4%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^xz@5.2.5%gcc@12.2.0~pic libs=shared,static arch=linux-rhel7-x86_64_v4
        ^zlib@1.2.12%gcc@12.2.0+optimize+pic+shared patches=0d38234 arch=linux-rhel7-x86_64_v4

Input spec
--------------------------------
py-gitpython

Concretized
--------------------------------
py-gitpython@3.1.24%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^py-gitdb@4.0.9%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^py-smmap@5.0.0%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^py-pip@22.1.2%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^py-setuptools@65.0.0%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^py-typing-extensions@4.3.0%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^py-flit-core@3.7.1%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^py-wheel@0.37.1%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^python@3.10.6%gcc@12.2.0+bz2+ctypes+dbm~debug+libxml2+lzma~nis~optimizations+pic+pyexpat+pythoncmd+readline+shared+sqlite3+ssl~tix~tkinter~ucs4+uuid+zlib patches=0d98e93,7d40923,f2fd060 arch=linux-rhel7-x86_64_v4
        ^bzip2@1.0.8%gcc@12.2.0~debug~pic+shared arch=linux-rhel7-x86_64_v4
            ^diffutils@3.8%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^expat@2.4.8%gcc@12.2.0+libbsd arch=linux-rhel7-x86_64_v4
            ^libbsd@0.11.5%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
                ^libmd@1.0.4%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^gdbm@1.19%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^gettext@0.21%gcc@12.2.0+bzip2+curses+git~libunistring+libxml2+tar+xz arch=linux-rhel7-x86_64_v4
            ^libiconv@1.16%gcc@12.2.0 libs=shared,static arch=linux-rhel7-x86_64_v4
            ^libxml2@2.10.1%gcc@12.2.0~python arch=linux-rhel7-x86_64_v4
            ^tar@1.34%gcc@12.2.0 zip=pigz arch=linux-rhel7-x86_64_v4
                ^pigz@2.7%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
                ^zstd@1.5.2%gcc@12.2.0+programs compression=none libs=shared,static arch=linux-rhel7-x86_64_v4
        ^libffi@3.4.2%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^ncurses@6.3%gcc@12.2.0~symlinks+termlib abi=none arch=linux-rhel7-x86_64_v4
        ^openssl@1.1.1q%gcc@12.2.0~docs~shared certs=mozilla patches=3fdcf2d arch=linux-rhel7-x86_64_v4
            ^ca-certificates-mozilla@2022-07-19%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
            ^perl@5.34.1%gcc@12.2.0+cpanm+shared+threads arch=linux-rhel7-x86_64_v4
                ^berkeley-db@18.1.40%gcc@12.2.0+cxx~docs+stl patches=26090f4,b231fcc arch=linux-rhel7-x86_64_v4
        ^pkgconf@1.8.0%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^readline@8.1.2%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^sqlite@3.39.2%gcc@12.2.0+column_metadata+dynamic_extensions+fts~functions+rtree arch=linux-rhel7-x86_64_v4
        ^util-linux-uuid@2.37.4%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^xz@5.2.5%gcc@12.2.0~pic libs=shared,static arch=linux-rhel7-x86_64_v4
        ^zlib@1.2.12%gcc@12.2.0+optimize+pic+shared patches=0d38234 arch=linux-rhel7-x86_64_v4

Input spec
--------------------------------
py-ipython

Concretized
--------------------------------
py-ipython@8.5.0%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^py-backcall@0.2.0%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^py-flit-core@3.7.1%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^py-decorator@5.1.1%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^py-setuptools@65.0.0%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^py-jedi@0.18.1%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^py-parso@0.8.2%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^py-matplotlib-inline@0.1.3%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^py-pexpect@4.8.0%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^py-ptyprocess@0.7.0%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^py-pickleshare@0.7.5%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^py-pip@22.1.2%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^py-prompt-toolkit@3.0.29%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^py-wcwidth@0.2.5%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^py-pygments@2.13.0%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^py-setuptools@59.4.0%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^py-stack-data@0.2.0%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^py-asttokens@2.0.8%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
            ^py-six@1.16.0%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^py-executing@1.1.0%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^py-pure-eval@0.2.2%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^py-setuptools-scm@7.0.5%gcc@12.2.0+toml arch=linux-rhel7-x86_64_v4
            ^py-packaging@21.3%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
                ^py-pyparsing@3.0.9%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
            ^py-tomli@2.0.1%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
            ^py-typing-extensions@4.3.0%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^py-traitlets@5.3.0%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^py-hatchling@1.10.0%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
            ^py-editables@0.3%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
            ^py-pathspec@0.10.1%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
            ^py-pluggy@1.0.0%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^py-wheel@0.37.1%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^python@3.10.6%gcc@12.2.0+bz2+ctypes+dbm~debug+libxml2+lzma~nis~optimizations+pic+pyexpat+pythoncmd+readline+shared+sqlite3+ssl~tix~tkinter~ucs4+uuid+zlib patches=0d98e93,7d40923,f2fd060 arch=linux-rhel7-x86_64_v4
        ^bzip2@1.0.8%gcc@12.2.0~debug~pic+shared arch=linux-rhel7-x86_64_v4
            ^diffutils@3.8%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^expat@2.4.8%gcc@12.2.0+libbsd arch=linux-rhel7-x86_64_v4
            ^libbsd@0.11.5%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
                ^libmd@1.0.4%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^gdbm@1.19%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^gettext@0.21%gcc@12.2.0+bzip2+curses+git~libunistring+libxml2+tar+xz arch=linux-rhel7-x86_64_v4
            ^libiconv@1.16%gcc@12.2.0 libs=shared,static arch=linux-rhel7-x86_64_v4
            ^libxml2@2.10.1%gcc@12.2.0~python arch=linux-rhel7-x86_64_v4
            ^tar@1.34%gcc@12.2.0 zip=pigz arch=linux-rhel7-x86_64_v4
                ^pigz@2.7%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
                ^zstd@1.5.2%gcc@12.2.0+programs compression=none libs=shared,static arch=linux-rhel7-x86_64_v4
        ^libffi@3.4.2%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^ncurses@6.3%gcc@12.2.0~symlinks+termlib abi=none arch=linux-rhel7-x86_64_v4
        ^openssl@1.1.1q%gcc@12.2.0~docs~shared certs=mozilla patches=3fdcf2d arch=linux-rhel7-x86_64_v4
            ^ca-certificates-mozilla@2022-07-19%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
            ^perl@5.34.1%gcc@12.2.0+cpanm+shared+threads arch=linux-rhel7-x86_64_v4
                ^berkeley-db@18.1.40%gcc@12.2.0+cxx~docs+stl patches=26090f4,b231fcc arch=linux-rhel7-x86_64_v4
        ^pkgconf@1.8.0%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^readline@8.1.2%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^sqlite@3.39.2%gcc@12.2.0+column_metadata+dynamic_extensions+fts~functions+rtree arch=linux-rhel7-x86_64_v4
        ^util-linux-uuid@2.37.4%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^xz@5.2.5%gcc@12.2.0~pic libs=shared,static arch=linux-rhel7-x86_64_v4
        ^zlib@1.2.12%gcc@12.2.0+optimize+pic+shared patches=0d38234 arch=linux-rhel7-x86_64_v4

Input spec
--------------------------------
py-mypy

Concretized
--------------------------------
py-mypy@0.961%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^py-mypy-extensions@0.4.3%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^py-setuptools@65.0.0%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^py-pip@22.1.2%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^py-setuptools@59.4.0%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^py-tomli@2.0.1%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^py-typing-extensions@4.3.0%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^py-flit-core@3.7.1%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^py-wheel@0.37.1%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^python@3.10.6%gcc@12.2.0+bz2+ctypes+dbm~debug+libxml2+lzma~nis~optimizations+pic+pyexpat+pythoncmd+readline+shared+sqlite3+ssl~tix~tkinter~ucs4+uuid+zlib patches=0d98e93,7d40923,f2fd060 arch=linux-rhel7-x86_64_v4
        ^bzip2@1.0.8%gcc@12.2.0~debug~pic+shared arch=linux-rhel7-x86_64_v4
            ^diffutils@3.8%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^expat@2.4.8%gcc@12.2.0+libbsd arch=linux-rhel7-x86_64_v4
            ^libbsd@0.11.5%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
                ^libmd@1.0.4%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^gdbm@1.19%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^gettext@0.21%gcc@12.2.0+bzip2+curses+git~libunistring+libxml2+tar+xz arch=linux-rhel7-x86_64_v4
            ^libiconv@1.16%gcc@12.2.0 libs=shared,static arch=linux-rhel7-x86_64_v4
            ^libxml2@2.10.1%gcc@12.2.0~python arch=linux-rhel7-x86_64_v4
            ^tar@1.34%gcc@12.2.0 zip=pigz arch=linux-rhel7-x86_64_v4
                ^pigz@2.7%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
                ^zstd@1.5.2%gcc@12.2.0+programs compression=none libs=shared,static arch=linux-rhel7-x86_64_v4
        ^libffi@3.4.2%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^ncurses@6.3%gcc@12.2.0~symlinks+termlib abi=none arch=linux-rhel7-x86_64_v4
        ^openssl@1.1.1q%gcc@12.2.0~docs~shared certs=mozilla patches=3fdcf2d arch=linux-rhel7-x86_64_v4
            ^ca-certificates-mozilla@2022-07-19%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
            ^perl@5.34.1%gcc@12.2.0+cpanm+shared+threads arch=linux-rhel7-x86_64_v4
                ^berkeley-db@18.1.40%gcc@12.2.0+cxx~docs+stl patches=26090f4,b231fcc arch=linux-rhel7-x86_64_v4
        ^pkgconf@1.8.0%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^readline@8.1.2%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^sqlite@3.39.2%gcc@12.2.0+column_metadata+dynamic_extensions+fts~functions+rtree arch=linux-rhel7-x86_64_v4
        ^util-linux-uuid@2.37.4%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^xz@5.2.5%gcc@12.2.0~pic libs=shared,static arch=linux-rhel7-x86_64_v4
        ^zlib@1.2.12%gcc@12.2.0+optimize+pic+shared patches=0d38234 arch=linux-rhel7-x86_64_v4

Input spec
--------------------------------
py-parsl

Concretized
--------------------------------
py-parsl@1.1.0%gcc@12.2.0 build_system=python_pip arch=linux-rhel7-x86_64_v4
    ^py-dill@0.3.4%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^py-setuptools@65.0.0%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^py-globus-sdk@3.10.1%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^py-cryptography@38.0.1%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
            ^git@2.37.0%gcc@12.2.0+man+nls+perl+subtree~svn~tcltk arch=linux-rhel7-x86_64_v4
                ^autoconf@2.69%gcc@12.2.0 patches=35c4492,7793209,a49dd5b arch=linux-rhel7-x86_64_v4
                ^automake@1.16.5%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
                ^curl@7.85.0%gcc@12.2.0~gssapi~ldap~libidn2~librtmp~libssh~libssh2~nghttp2 libs=shared,static tls=openssl arch=linux-rhel7-x86_64_v4
                ^libidn2@2.3.0%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
                    ^libunistring@0.9.10%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
                ^libtool@2.4.7%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
                ^m4@1.4.19%gcc@12.2.0+sigsegv patches=9dc5fbd,bfdffa7 arch=linux-rhel7-x86_64_v4
                    ^libsigsegv@2.13%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
                ^openssh@9.0p1%gcc@12.2.0+gssapi arch=linux-rhel7-x86_64_v4
                    ^krb5@1.19.3%gcc@12.2.0+shared arch=linux-rhel7-x86_64_v4
                        ^bison@3.8.2%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
                    ^libedit@3.1-20210216%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
                ^pcre2@10.39%gcc@12.2.0~jit+multibyte arch=linux-rhel7-x86_64_v4
            ^py-setuptools-rust@1.2.0%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
                ^py-semantic-version@2.10.0%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
                ^py-setuptools-scm@7.0.5%gcc@12.2.0+toml arch=linux-rhel7-x86_64_v4
            ^rust@1.60.0%gcc@12.2.0+analysis+clippy~rls+rustfmt+src extra_targets=none arch=linux-rhel7-x86_64_v4
                ^cmake@3.24.2%gcc@12.2.0~doc+ncurses+ownlibs~qt build_type=Release arch=linux-rhel7-x86_64_v4
                ^gmake@4.3%gcc@12.2.0~guile+nls arch=linux-rhel7-x86_64_v4
                    ^texinfo@6.5%gcc@12.2.0 patches=12f6edb,1732115 arch=linux-rhel7-x86_64_v4
                ^libgit2@1.3.1%gcc@12.2.0~curl~ipo+mmap+ssh build_type=RelWithDebInfo https=system arch=linux-rhel7-x86_64_v4
                ^libssh2@1.10.0%gcc@12.2.0~ipo+shared build_type=RelWithDebInfo crypto=openssl arch=linux-rhel7-x86_64_v4
                ^ninja@1.11.0%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^py-pyjwt@2.4.0%gcc@12.2.0+crypto arch=linux-rhel7-x86_64_v4
    ^py-paramiko@2.12.0%gcc@12.2.0~invoke build_system=python_pip arch=linux-rhel7-x86_64_v4
        ^py-bcrypt@3.2.0%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^py-pynacl@1.5.0%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^py-six@1.16.0%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^py-pip@22.1.2%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^py-psutil@5.8.0%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^py-pyzmq@22.3.0%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^libzmq@4.3.4%gcc@12.2.0~docs~drafts+libbsd+libsodium~libunwind patches=310b8aa,edca864 arch=linux-rhel7-x86_64_v4
            ^libbsd@0.11.5%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
                ^libmd@1.0.4%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
            ^libsodium@1.0.18%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^py-cffi@1.15.0%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
            ^py-pycparser@2.20%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^py-cython@0.29.32%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^py-gevent@1.5.0%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
            ^py-greenlet@1.1.3%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^py-py@1.11.0%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^py-requests@2.28.1%gcc@12.2.0~socks arch=linux-rhel7-x86_64_v4
        ^py-certifi@2022.9.14%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^py-charset-normalizer@2.0.12%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^py-idna@3.4%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^py-urllib3@1.26.6%gcc@12.2.0~brotli~secure~socks arch=linux-rhel7-x86_64_v4
    ^py-setuptools@59.4.0%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^py-tblib@1.6.0%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^py-typeguard@2.12.1%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^py-setuptools-scm@7.0.5%gcc@12.2.0+toml arch=linux-rhel7-x86_64_v4
            ^py-packaging@21.3%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
                ^py-pyparsing@3.0.9%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
            ^py-tomli@2.0.1%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^py-typing-extensions@4.3.0%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^py-flit-core@3.7.1%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^py-wheel@0.37.1%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^python@3.10.6%gcc@12.2.0+bz2+ctypes+dbm~debug+libxml2+lzma~nis~optimizations+pic+pyexpat+pythoncmd+readline+shared+sqlite3+ssl~tix~tkinter~ucs4+uuid+zlib patches=0d98e93,7d40923,f2fd060 arch=linux-rhel7-x86_64_v4
        ^bzip2@1.0.8%gcc@12.2.0~debug~pic+shared arch=linux-rhel7-x86_64_v4
            ^diffutils@3.8%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^expat@2.4.8%gcc@12.2.0+libbsd arch=linux-rhel7-x86_64_v4
        ^gdbm@1.19%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^gettext@0.21%gcc@12.2.0+bzip2+curses+git~libunistring+libxml2+tar+xz arch=linux-rhel7-x86_64_v4
            ^libiconv@1.16%gcc@12.2.0 libs=shared,static arch=linux-rhel7-x86_64_v4
            ^libxml2@2.10.1%gcc@12.2.0~python arch=linux-rhel7-x86_64_v4
            ^tar@1.34%gcc@12.2.0 zip=pigz arch=linux-rhel7-x86_64_v4
                ^pigz@2.7%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
                ^zstd@1.5.2%gcc@12.2.0+programs compression=none libs=shared,static arch=linux-rhel7-x86_64_v4
        ^libffi@3.4.2%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^ncurses@6.3%gcc@12.2.0~symlinks+termlib abi=none arch=linux-rhel7-x86_64_v4
        ^openssl@1.1.1q%gcc@12.2.0~docs~shared certs=mozilla patches=3fdcf2d arch=linux-rhel7-x86_64_v4
            ^ca-certificates-mozilla@2022-07-19%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
            ^perl@5.34.1%gcc@12.2.0+cpanm+shared+threads arch=linux-rhel7-x86_64_v4
                ^berkeley-db@18.1.40%gcc@12.2.0+cxx~docs+stl patches=26090f4,b231fcc arch=linux-rhel7-x86_64_v4
        ^pkgconf@1.8.0%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^readline@8.1.2%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^sqlite@3.39.2%gcc@12.2.0+column_metadata+dynamic_extensions+fts~functions+rtree arch=linux-rhel7-x86_64_v4
        ^util-linux-uuid@2.37.4%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^xz@5.2.5%gcc@12.2.0~pic libs=shared,static arch=linux-rhel7-x86_64_v4
        ^zlib@1.2.12%gcc@12.2.0+optimize+pic+shared patches=0d38234 arch=linux-rhel7-x86_64_v4

Input spec
--------------------------------
py-pip

Concretized
--------------------------------
py-pip@22.1.2%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^python@3.10.6%gcc@12.2.0+bz2+ctypes+dbm~debug+libxml2+lzma~nis~optimizations+pic+pyexpat+pythoncmd+readline+shared+sqlite3+ssl~tix~tkinter~ucs4+uuid+zlib patches=0d98e93,7d40923,f2fd060 arch=linux-rhel7-x86_64_v4
        ^bzip2@1.0.8%gcc@12.2.0~debug~pic+shared arch=linux-rhel7-x86_64_v4
            ^diffutils@3.8%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^expat@2.4.8%gcc@12.2.0+libbsd arch=linux-rhel7-x86_64_v4
            ^libbsd@0.11.5%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
                ^libmd@1.0.4%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^gdbm@1.19%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^gettext@0.21%gcc@12.2.0+bzip2+curses+git~libunistring+libxml2+tar+xz arch=linux-rhel7-x86_64_v4
            ^libiconv@1.16%gcc@12.2.0 libs=shared,static arch=linux-rhel7-x86_64_v4
            ^libxml2@2.10.1%gcc@12.2.0~python arch=linux-rhel7-x86_64_v4
            ^tar@1.34%gcc@12.2.0 zip=pigz arch=linux-rhel7-x86_64_v4
                ^pigz@2.7%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
                ^zstd@1.5.2%gcc@12.2.0+programs compression=none libs=shared,static arch=linux-rhel7-x86_64_v4
        ^libffi@3.4.2%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^ncurses@6.3%gcc@12.2.0~symlinks+termlib abi=none arch=linux-rhel7-x86_64_v4
        ^openssl@1.1.1q%gcc@12.2.0~docs~shared certs=mozilla patches=3fdcf2d arch=linux-rhel7-x86_64_v4
            ^ca-certificates-mozilla@2022-07-19%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
            ^perl@5.34.1%gcc@12.2.0+cpanm+shared+threads arch=linux-rhel7-x86_64_v4
                ^berkeley-db@18.1.40%gcc@12.2.0+cxx~docs+stl patches=26090f4,b231fcc arch=linux-rhel7-x86_64_v4
        ^pkgconf@1.8.0%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^readline@8.1.2%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^sqlite@3.39.2%gcc@12.2.0+column_metadata+dynamic_extensions+fts~functions+rtree arch=linux-rhel7-x86_64_v4
        ^util-linux-uuid@2.37.4%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^xz@5.2.5%gcc@12.2.0~pic libs=shared,static arch=linux-rhel7-x86_64_v4
        ^zlib@1.2.12%gcc@12.2.0+optimize+pic+shared patches=0d38234 arch=linux-rhel7-x86_64_v4

Input spec
--------------------------------
py-pygithub

Concretized
--------------------------------
py-pygithub@1.55%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^py-deprecated@1.2.13%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^py-setuptools@65.0.0%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^py-wrapt@1.13.3%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^py-pip@22.1.2%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^py-pyjwt@2.4.0%gcc@12.2.0+crypto arch=linux-rhel7-x86_64_v4
        ^py-cryptography@38.0.1%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
            ^git@2.37.0%gcc@12.2.0+man+nls+perl+subtree~svn~tcltk arch=linux-rhel7-x86_64_v4
                ^autoconf@2.69%gcc@12.2.0 patches=35c4492,7793209,a49dd5b arch=linux-rhel7-x86_64_v4
                ^automake@1.16.5%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
                ^curl@7.85.0%gcc@12.2.0~gssapi~ldap~libidn2~librtmp~libssh~libssh2~nghttp2 libs=shared,static tls=openssl arch=linux-rhel7-x86_64_v4
                ^libidn2@2.3.0%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
                    ^libunistring@0.9.10%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
                ^libtool@2.4.7%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
                ^m4@1.4.19%gcc@12.2.0+sigsegv patches=9dc5fbd,bfdffa7 arch=linux-rhel7-x86_64_v4
                    ^libsigsegv@2.13%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
                ^openssh@9.0p1%gcc@12.2.0+gssapi arch=linux-rhel7-x86_64_v4
                    ^krb5@1.19.3%gcc@12.2.0+shared arch=linux-rhel7-x86_64_v4
                        ^bison@3.8.2%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
                    ^libedit@3.1-20210216%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
                ^pcre2@10.39%gcc@12.2.0~jit+multibyte arch=linux-rhel7-x86_64_v4
            ^py-setuptools-rust@1.2.0%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
                ^py-semantic-version@2.10.0%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
                ^py-setuptools-scm@7.0.5%gcc@12.2.0+toml arch=linux-rhel7-x86_64_v4
                    ^py-packaging@21.3%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
                        ^py-pyparsing@3.0.9%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
                    ^py-tomli@2.0.1%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
                ^py-typing-extensions@4.3.0%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
            ^rust@1.60.0%gcc@12.2.0+analysis+clippy~rls+rustfmt+src extra_targets=none arch=linux-rhel7-x86_64_v4
                ^cmake@3.24.2%gcc@12.2.0~doc+ncurses+ownlibs~qt build_type=Release arch=linux-rhel7-x86_64_v4
                ^gmake@4.3%gcc@12.2.0~guile+nls arch=linux-rhel7-x86_64_v4
                    ^texinfo@6.5%gcc@12.2.0 patches=12f6edb,1732115 arch=linux-rhel7-x86_64_v4
                ^libgit2@1.3.1%gcc@12.2.0~curl~ipo+mmap+ssh build_type=RelWithDebInfo https=system arch=linux-rhel7-x86_64_v4
                ^libssh2@1.10.0%gcc@12.2.0~ipo+shared build_type=RelWithDebInfo crypto=openssl arch=linux-rhel7-x86_64_v4
                ^ninja@1.11.0%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^py-pynacl@1.5.0%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^py-cffi@1.15.0%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
            ^py-pycparser@2.20%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^py-requests@2.28.1%gcc@12.2.0~socks arch=linux-rhel7-x86_64_v4
        ^py-certifi@2022.9.14%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^py-charset-normalizer@2.0.12%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^py-idna@3.4%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
            ^py-flit-core@3.7.1%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^py-urllib3@1.26.6%gcc@12.2.0~brotli~secure~socks arch=linux-rhel7-x86_64_v4
    ^py-setuptools@59.4.0%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^py-wheel@0.37.1%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^python@3.10.6%gcc@12.2.0+bz2+ctypes+dbm~debug+libxml2+lzma~nis~optimizations+pic+pyexpat+pythoncmd+readline+shared+sqlite3+ssl~tix~tkinter~ucs4+uuid+zlib patches=0d98e93,7d40923,f2fd060 arch=linux-rhel7-x86_64_v4
        ^bzip2@1.0.8%gcc@12.2.0~debug~pic+shared arch=linux-rhel7-x86_64_v4
            ^diffutils@3.8%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^expat@2.4.8%gcc@12.2.0+libbsd arch=linux-rhel7-x86_64_v4
            ^libbsd@0.11.5%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
                ^libmd@1.0.4%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^gdbm@1.19%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^gettext@0.21%gcc@12.2.0+bzip2+curses+git~libunistring+libxml2+tar+xz arch=linux-rhel7-x86_64_v4
            ^libiconv@1.16%gcc@12.2.0 libs=shared,static arch=linux-rhel7-x86_64_v4
            ^libxml2@2.10.1%gcc@12.2.0~python arch=linux-rhel7-x86_64_v4
            ^tar@1.34%gcc@12.2.0 zip=pigz arch=linux-rhel7-x86_64_v4
                ^pigz@2.7%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
                ^zstd@1.5.2%gcc@12.2.0+programs compression=none libs=shared,static arch=linux-rhel7-x86_64_v4
        ^libffi@3.4.2%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^ncurses@6.3%gcc@12.2.0~symlinks+termlib abi=none arch=linux-rhel7-x86_64_v4
        ^openssl@1.1.1q%gcc@12.2.0~docs~shared certs=mozilla patches=3fdcf2d arch=linux-rhel7-x86_64_v4
            ^ca-certificates-mozilla@2022-07-19%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
            ^perl@5.34.1%gcc@12.2.0+cpanm+shared+threads arch=linux-rhel7-x86_64_v4
                ^berkeley-db@18.1.40%gcc@12.2.0+cxx~docs+stl patches=26090f4,b231fcc arch=linux-rhel7-x86_64_v4
        ^pkgconf@1.8.0%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^readline@8.1.2%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^sqlite@3.39.2%gcc@12.2.0+column_metadata+dynamic_extensions+fts~functions+rtree arch=linux-rhel7-x86_64_v4
        ^util-linux-uuid@2.37.4%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^xz@5.2.5%gcc@12.2.0~pic libs=shared,static arch=linux-rhel7-x86_64_v4
        ^zlib@1.2.12%gcc@12.2.0+optimize+pic+shared patches=0d38234 arch=linux-rhel7-x86_64_v4

Input spec
--------------------------------
py-pytest

Concretized
--------------------------------
py-pytest@7.1.3%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^py-attrs@22.1.0%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^py-setuptools@65.0.0%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^py-iniconfig@1.1.1%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^py-packaging@21.3%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^py-pyparsing@3.0.9%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
            ^py-flit-core@3.7.1%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^py-pip@22.1.2%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^py-pluggy@1.0.0%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^py-setuptools-scm@7.0.5%gcc@12.2.0+toml arch=linux-rhel7-x86_64_v4
    ^py-py@1.11.0%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^py-setuptools@59.4.0%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^py-setuptools-scm@7.0.5%gcc@12.2.0+toml arch=linux-rhel7-x86_64_v4
        ^py-typing-extensions@4.3.0%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^py-tomli@2.0.1%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^py-wheel@0.37.1%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^python@3.10.6%gcc@12.2.0+bz2+ctypes+dbm~debug+libxml2+lzma~nis~optimizations+pic+pyexpat+pythoncmd+readline+shared+sqlite3+ssl~tix~tkinter~ucs4+uuid+zlib patches=0d98e93,7d40923,f2fd060 arch=linux-rhel7-x86_64_v4
        ^bzip2@1.0.8%gcc@12.2.0~debug~pic+shared arch=linux-rhel7-x86_64_v4
            ^diffutils@3.8%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^expat@2.4.8%gcc@12.2.0+libbsd arch=linux-rhel7-x86_64_v4
            ^libbsd@0.11.5%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
                ^libmd@1.0.4%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^gdbm@1.19%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^gettext@0.21%gcc@12.2.0+bzip2+curses+git~libunistring+libxml2+tar+xz arch=linux-rhel7-x86_64_v4
            ^libiconv@1.16%gcc@12.2.0 libs=shared,static arch=linux-rhel7-x86_64_v4
            ^libxml2@2.10.1%gcc@12.2.0~python arch=linux-rhel7-x86_64_v4
            ^tar@1.34%gcc@12.2.0 zip=pigz arch=linux-rhel7-x86_64_v4
                ^pigz@2.7%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
                ^zstd@1.5.2%gcc@12.2.0+programs compression=none libs=shared,static arch=linux-rhel7-x86_64_v4
        ^libffi@3.4.2%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^ncurses@6.3%gcc@12.2.0~symlinks+termlib abi=none arch=linux-rhel7-x86_64_v4
        ^openssl@1.1.1q%gcc@12.2.0~docs~shared certs=mozilla patches=3fdcf2d arch=linux-rhel7-x86_64_v4
            ^ca-certificates-mozilla@2022-07-19%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
            ^perl@5.34.1%gcc@12.2.0+cpanm+shared+threads arch=linux-rhel7-x86_64_v4
                ^berkeley-db@18.1.40%gcc@12.2.0+cxx~docs+stl patches=26090f4,b231fcc arch=linux-rhel7-x86_64_v4
        ^pkgconf@1.8.0%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^readline@8.1.2%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^sqlite@3.39.2%gcc@12.2.0+column_metadata+dynamic_extensions+fts~functions+rtree arch=linux-rhel7-x86_64_v4
        ^util-linux-uuid@2.37.4%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^xz@5.2.5%gcc@12.2.0~pic libs=shared,static arch=linux-rhel7-x86_64_v4
        ^zlib@1.2.12%gcc@12.2.0+optimize+pic+shared patches=0d38234 arch=linux-rhel7-x86_64_v4

Input spec
--------------------------------
py-pyyaml

Concretized
--------------------------------
py-pyyaml@6.0%gcc@12.2.0+libyaml arch=linux-rhel7-x86_64_v4
    ^libyaml@0.2.5%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^py-cython@0.29.32%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^py-pip@22.1.2%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^py-setuptools@65.0.0%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^py-wheel@0.37.1%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^python@3.10.6%gcc@12.2.0+bz2+ctypes+dbm~debug+libxml2+lzma~nis~optimizations+pic+pyexpat+pythoncmd+readline+shared+sqlite3+ssl~tix~tkinter~ucs4+uuid+zlib patches=0d98e93,7d40923,f2fd060 arch=linux-rhel7-x86_64_v4
        ^bzip2@1.0.8%gcc@12.2.0~debug~pic+shared arch=linux-rhel7-x86_64_v4
            ^diffutils@3.8%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^expat@2.4.8%gcc@12.2.0+libbsd arch=linux-rhel7-x86_64_v4
            ^libbsd@0.11.5%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
                ^libmd@1.0.4%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^gdbm@1.19%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^gettext@0.21%gcc@12.2.0+bzip2+curses+git~libunistring+libxml2+tar+xz arch=linux-rhel7-x86_64_v4
            ^libiconv@1.16%gcc@12.2.0 libs=shared,static arch=linux-rhel7-x86_64_v4
            ^libxml2@2.10.1%gcc@12.2.0~python arch=linux-rhel7-x86_64_v4
            ^tar@1.34%gcc@12.2.0 zip=pigz arch=linux-rhel7-x86_64_v4
                ^pigz@2.7%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
                ^zstd@1.5.2%gcc@12.2.0+programs compression=none libs=shared,static arch=linux-rhel7-x86_64_v4
        ^libffi@3.4.2%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^ncurses@6.3%gcc@12.2.0~symlinks+termlib abi=none arch=linux-rhel7-x86_64_v4
        ^openssl@1.1.1q%gcc@12.2.0~docs~shared certs=mozilla patches=3fdcf2d arch=linux-rhel7-x86_64_v4
            ^ca-certificates-mozilla@2022-07-19%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
            ^perl@5.34.1%gcc@12.2.0+cpanm+shared+threads arch=linux-rhel7-x86_64_v4
                ^berkeley-db@18.1.40%gcc@12.2.0+cxx~docs+stl patches=26090f4,b231fcc arch=linux-rhel7-x86_64_v4
        ^pkgconf@1.8.0%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^readline@8.1.2%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^sqlite@3.39.2%gcc@12.2.0+column_metadata+dynamic_extensions+fts~functions+rtree arch=linux-rhel7-x86_64_v4
        ^util-linux-uuid@2.37.4%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^xz@5.2.5%gcc@12.2.0~pic libs=shared,static arch=linux-rhel7-x86_64_v4
        ^zlib@1.2.12%gcc@12.2.0+optimize+pic+shared patches=0d38234 arch=linux-rhel7-x86_64_v4

Input spec
--------------------------------
py-requests

Concretized
--------------------------------
py-requests@2.28.1%gcc@12.2.0~socks arch=linux-rhel7-x86_64_v4
    ^py-certifi@2022.9.14%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^py-charset-normalizer@2.0.12%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^py-idna@3.4%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^py-flit-core@3.7.1%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^py-pip@22.1.2%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^py-setuptools@65.0.0%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^py-urllib3@1.26.6%gcc@12.2.0~brotli~secure~socks arch=linux-rhel7-x86_64_v4
    ^py-wheel@0.37.1%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^python@3.10.6%gcc@12.2.0+bz2+ctypes+dbm~debug+libxml2+lzma~nis~optimizations+pic+pyexpat+pythoncmd+readline+shared+sqlite3+ssl~tix~tkinter~ucs4+uuid+zlib patches=0d98e93,7d40923,f2fd060 arch=linux-rhel7-x86_64_v4
        ^bzip2@1.0.8%gcc@12.2.0~debug~pic+shared arch=linux-rhel7-x86_64_v4
            ^diffutils@3.8%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^expat@2.4.8%gcc@12.2.0+libbsd arch=linux-rhel7-x86_64_v4
            ^libbsd@0.11.5%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
                ^libmd@1.0.4%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^gdbm@1.19%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^gettext@0.21%gcc@12.2.0+bzip2+curses+git~libunistring+libxml2+tar+xz arch=linux-rhel7-x86_64_v4
            ^libiconv@1.16%gcc@12.2.0 libs=shared,static arch=linux-rhel7-x86_64_v4
            ^libxml2@2.10.1%gcc@12.2.0~python arch=linux-rhel7-x86_64_v4
            ^tar@1.34%gcc@12.2.0 zip=pigz arch=linux-rhel7-x86_64_v4
                ^pigz@2.7%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
                ^zstd@1.5.2%gcc@12.2.0+programs compression=none libs=shared,static arch=linux-rhel7-x86_64_v4
        ^libffi@3.4.2%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^ncurses@6.3%gcc@12.2.0~symlinks+termlib abi=none arch=linux-rhel7-x86_64_v4
        ^openssl@1.1.1q%gcc@12.2.0~docs~shared certs=mozilla patches=3fdcf2d arch=linux-rhel7-x86_64_v4
            ^ca-certificates-mozilla@2022-07-19%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
            ^perl@5.34.1%gcc@12.2.0+cpanm+shared+threads arch=linux-rhel7-x86_64_v4
                ^berkeley-db@18.1.40%gcc@12.2.0+cxx~docs+stl patches=26090f4,b231fcc arch=linux-rhel7-x86_64_v4
        ^pkgconf@1.8.0%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^readline@8.1.2%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^sqlite@3.39.2%gcc@12.2.0+column_metadata+dynamic_extensions+fts~functions+rtree arch=linux-rhel7-x86_64_v4
        ^util-linux-uuid@2.37.4%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^xz@5.2.5%gcc@12.2.0~pic libs=shared,static arch=linux-rhel7-x86_64_v4
        ^zlib@1.2.12%gcc@12.2.0+optimize+pic+shared patches=0d38234 arch=linux-rhel7-x86_64_v4

Input spec
--------------------------------
py-rich

Concretized
--------------------------------
py-rich@10.14.0%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^py-colorama@0.4.5%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^py-setuptools@65.0.0%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^py-commonmark@0.9.1%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^py-pip@22.1.2%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^py-poetry-core@1.2.0%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^py-pygments@2.13.0%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^py-setuptools@59.4.0%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^py-wheel@0.37.1%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^python@3.10.6%gcc@12.2.0+bz2+ctypes+dbm~debug+libxml2+lzma~nis~optimizations+pic+pyexpat+pythoncmd+readline+shared+sqlite3+ssl~tix~tkinter~ucs4+uuid+zlib patches=0d98e93,7d40923,f2fd060 arch=linux-rhel7-x86_64_v4
        ^bzip2@1.0.8%gcc@12.2.0~debug~pic+shared arch=linux-rhel7-x86_64_v4
            ^diffutils@3.8%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^expat@2.4.8%gcc@12.2.0+libbsd arch=linux-rhel7-x86_64_v4
            ^libbsd@0.11.5%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
                ^libmd@1.0.4%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^gdbm@1.19%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^gettext@0.21%gcc@12.2.0+bzip2+curses+git~libunistring+libxml2+tar+xz arch=linux-rhel7-x86_64_v4
            ^libiconv@1.16%gcc@12.2.0 libs=shared,static arch=linux-rhel7-x86_64_v4
            ^libxml2@2.10.1%gcc@12.2.0~python arch=linux-rhel7-x86_64_v4
            ^tar@1.34%gcc@12.2.0 zip=pigz arch=linux-rhel7-x86_64_v4
                ^pigz@2.7%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
                ^zstd@1.5.2%gcc@12.2.0+programs compression=none libs=shared,static arch=linux-rhel7-x86_64_v4
        ^libffi@3.4.2%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^ncurses@6.3%gcc@12.2.0~symlinks+termlib abi=none arch=linux-rhel7-x86_64_v4
        ^openssl@1.1.1q%gcc@12.2.0~docs~shared certs=mozilla patches=3fdcf2d arch=linux-rhel7-x86_64_v4
            ^ca-certificates-mozilla@2022-07-19%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
            ^perl@5.34.1%gcc@12.2.0+cpanm+shared+threads arch=linux-rhel7-x86_64_v4
                ^berkeley-db@18.1.40%gcc@12.2.0+cxx~docs+stl patches=26090f4,b231fcc arch=linux-rhel7-x86_64_v4
        ^pkgconf@1.8.0%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^readline@8.1.2%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^sqlite@3.39.2%gcc@12.2.0+column_metadata+dynamic_extensions+fts~functions+rtree arch=linux-rhel7-x86_64_v4
        ^util-linux-uuid@2.37.4%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^xz@5.2.5%gcc@12.2.0~pic libs=shared,static arch=linux-rhel7-x86_64_v4
        ^zlib@1.2.12%gcc@12.2.0+optimize+pic+shared patches=0d38234 arch=linux-rhel7-x86_64_v4

Input spec
--------------------------------
py-tomli@2.0.1

Concretized
--------------------------------
py-tomli@2.0.1%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^py-pip@22.1.2%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^py-wheel@0.37.1%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^python@3.10.6%gcc@12.2.0+bz2+ctypes+dbm~debug+libxml2+lzma~nis~optimizations+pic+pyexpat+pythoncmd+readline+shared+sqlite3+ssl~tix~tkinter~ucs4+uuid+zlib patches=0d98e93,7d40923,f2fd060 arch=linux-rhel7-x86_64_v4
        ^bzip2@1.0.8%gcc@12.2.0~debug~pic+shared arch=linux-rhel7-x86_64_v4
            ^diffutils@3.8%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^expat@2.4.8%gcc@12.2.0+libbsd arch=linux-rhel7-x86_64_v4
            ^libbsd@0.11.5%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
                ^libmd@1.0.4%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^gdbm@1.19%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^gettext@0.21%gcc@12.2.0+bzip2+curses+git~libunistring+libxml2+tar+xz arch=linux-rhel7-x86_64_v4
            ^libiconv@1.16%gcc@12.2.0 libs=shared,static arch=linux-rhel7-x86_64_v4
            ^libxml2@2.10.1%gcc@12.2.0~python arch=linux-rhel7-x86_64_v4
            ^tar@1.34%gcc@12.2.0 zip=pigz arch=linux-rhel7-x86_64_v4
                ^pigz@2.7%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
                ^zstd@1.5.2%gcc@12.2.0+programs compression=none libs=shared,static arch=linux-rhel7-x86_64_v4
        ^libffi@3.4.2%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^ncurses@6.3%gcc@12.2.0~symlinks+termlib abi=none arch=linux-rhel7-x86_64_v4
        ^openssl@1.1.1q%gcc@12.2.0~docs~shared certs=mozilla patches=3fdcf2d arch=linux-rhel7-x86_64_v4
            ^ca-certificates-mozilla@2022-07-19%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
            ^perl@5.34.1%gcc@12.2.0+cpanm+shared+threads arch=linux-rhel7-x86_64_v4
                ^berkeley-db@18.1.40%gcc@12.2.0+cxx~docs+stl patches=26090f4,b231fcc arch=linux-rhel7-x86_64_v4
        ^pkgconf@1.8.0%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^readline@8.1.2%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^sqlite@3.39.2%gcc@12.2.0+column_metadata+dynamic_extensions+fts~functions+rtree arch=linux-rhel7-x86_64_v4
        ^util-linux-uuid@2.37.4%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^xz@5.2.5%gcc@12.2.0~pic libs=shared,static arch=linux-rhel7-x86_64_v4
        ^zlib@1.2.12%gcc@12.2.0+optimize+pic+shared patches=0d38234 arch=linux-rhel7-x86_64_v4

Input spec
--------------------------------
py-tqdm

Concretized
--------------------------------
py-tqdm@4.64.0%gcc@12.2.0~notebook~telegram arch=linux-rhel7-x86_64_v4
    ^py-pip@22.1.2%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^py-setuptools@59.4.0%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^py-setuptools-scm@7.0.5%gcc@12.2.0+toml arch=linux-rhel7-x86_64_v4
        ^py-packaging@21.3%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
            ^py-pyparsing@3.0.9%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
            ^py-setuptools@65.0.0%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^py-tomli@2.0.1%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^py-typing-extensions@4.3.0%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
            ^py-flit-core@3.7.1%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^py-wheel@0.37.1%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^python@3.10.6%gcc@12.2.0+bz2+ctypes+dbm~debug+libxml2+lzma~nis~optimizations+pic+pyexpat+pythoncmd+readline+shared+sqlite3+ssl~tix~tkinter~ucs4+uuid+zlib patches=0d98e93,7d40923,f2fd060 arch=linux-rhel7-x86_64_v4
        ^bzip2@1.0.8%gcc@12.2.0~debug~pic+shared arch=linux-rhel7-x86_64_v4
            ^diffutils@3.8%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^expat@2.4.8%gcc@12.2.0+libbsd arch=linux-rhel7-x86_64_v4
            ^libbsd@0.11.5%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
                ^libmd@1.0.4%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^gdbm@1.19%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^gettext@0.21%gcc@12.2.0+bzip2+curses+git~libunistring+libxml2+tar+xz arch=linux-rhel7-x86_64_v4
            ^libiconv@1.16%gcc@12.2.0 libs=shared,static arch=linux-rhel7-x86_64_v4
            ^libxml2@2.10.1%gcc@12.2.0~python arch=linux-rhel7-x86_64_v4
            ^tar@1.34%gcc@12.2.0 zip=pigz arch=linux-rhel7-x86_64_v4
                ^pigz@2.7%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
                ^zstd@1.5.2%gcc@12.2.0+programs compression=none libs=shared,static arch=linux-rhel7-x86_64_v4
        ^libffi@3.4.2%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^ncurses@6.3%gcc@12.2.0~symlinks+termlib abi=none arch=linux-rhel7-x86_64_v4
        ^openssl@1.1.1q%gcc@12.2.0~docs~shared certs=mozilla patches=3fdcf2d arch=linux-rhel7-x86_64_v4
            ^ca-certificates-mozilla@2022-07-19%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
            ^perl@5.34.1%gcc@12.2.0+cpanm+shared+threads arch=linux-rhel7-x86_64_v4
                ^berkeley-db@18.1.40%gcc@12.2.0+cxx~docs+stl patches=26090f4,b231fcc arch=linux-rhel7-x86_64_v4
        ^pkgconf@1.8.0%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^readline@8.1.2%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^sqlite@3.39.2%gcc@12.2.0+column_metadata+dynamic_extensions+fts~functions+rtree arch=linux-rhel7-x86_64_v4
        ^util-linux-uuid@2.37.4%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^xz@5.2.5%gcc@12.2.0~pic libs=shared,static arch=linux-rhel7-x86_64_v4
        ^zlib@1.2.12%gcc@12.2.0+optimize+pic+shared patches=0d38234 arch=linux-rhel7-x86_64_v4

Input spec
--------------------------------
py-xxhash

Concretized
--------------------------------
py-xxhash@2.0.2%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^py-pip@22.1.2%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^py-setuptools@65.0.0%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^py-wheel@0.37.1%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^python@3.10.6%gcc@12.2.0+bz2+ctypes+dbm~debug+libxml2+lzma~nis~optimizations+pic+pyexpat+pythoncmd+readline+shared+sqlite3+ssl~tix~tkinter~ucs4+uuid+zlib patches=0d98e93,7d40923,f2fd060 arch=linux-rhel7-x86_64_v4
        ^bzip2@1.0.8%gcc@12.2.0~debug~pic+shared arch=linux-rhel7-x86_64_v4
            ^diffutils@3.8%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^expat@2.4.8%gcc@12.2.0+libbsd arch=linux-rhel7-x86_64_v4
            ^libbsd@0.11.5%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
                ^libmd@1.0.4%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^gdbm@1.19%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^gettext@0.21%gcc@12.2.0+bzip2+curses+git~libunistring+libxml2+tar+xz arch=linux-rhel7-x86_64_v4
            ^libiconv@1.16%gcc@12.2.0 libs=shared,static arch=linux-rhel7-x86_64_v4
            ^libxml2@2.10.1%gcc@12.2.0~python arch=linux-rhel7-x86_64_v4
            ^tar@1.34%gcc@12.2.0 zip=pigz arch=linux-rhel7-x86_64_v4
                ^pigz@2.7%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
                ^zstd@1.5.2%gcc@12.2.0+programs compression=none libs=shared,static arch=linux-rhel7-x86_64_v4
        ^libffi@3.4.2%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^ncurses@6.3%gcc@12.2.0~symlinks+termlib abi=none arch=linux-rhel7-x86_64_v4
        ^openssl@1.1.1q%gcc@12.2.0~docs~shared certs=mozilla patches=3fdcf2d arch=linux-rhel7-x86_64_v4
            ^ca-certificates-mozilla@2022-07-19%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
            ^perl@5.34.1%gcc@12.2.0+cpanm+shared+threads arch=linux-rhel7-x86_64_v4
                ^berkeley-db@18.1.40%gcc@12.2.0+cxx~docs+stl patches=26090f4,b231fcc arch=linux-rhel7-x86_64_v4
        ^pkgconf@1.8.0%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^readline@8.1.2%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^sqlite@3.39.2%gcc@12.2.0+column_metadata+dynamic_extensions+fts~functions+rtree arch=linux-rhel7-x86_64_v4
        ^util-linux-uuid@2.37.4%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^xz@5.2.5%gcc@12.2.0~pic libs=shared,static arch=linux-rhel7-x86_64_v4
        ^zlib@1.2.12%gcc@12.2.0+optimize+pic+shared patches=0d38234 arch=linux-rhel7-x86_64_v4
    ^xxhash@0.8.0%gcc@12.2.0 arch=linux-rhel7-x86_64_v4

Input spec
--------------------------------
python@3.10

Concretized
--------------------------------
python@3.10.6%gcc@12.2.0+bz2+ctypes+dbm~debug+libxml2+lzma~nis~optimizations+pic+pyexpat+pythoncmd+readline+shared+sqlite3+ssl~tix~tkinter~ucs4+uuid+zlib patches=0d98e93,7d40923,f2fd060 arch=linux-rhel7-x86_64_v4
    ^bzip2@1.0.8%gcc@12.2.0~debug~pic+shared arch=linux-rhel7-x86_64_v4
        ^diffutils@3.8%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^expat@2.4.8%gcc@12.2.0+libbsd arch=linux-rhel7-x86_64_v4
        ^libbsd@0.11.5%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
            ^libmd@1.0.4%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^gdbm@1.19%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^gettext@0.21%gcc@12.2.0+bzip2+curses+git~libunistring+libxml2+tar+xz arch=linux-rhel7-x86_64_v4
        ^libiconv@1.16%gcc@12.2.0 libs=shared,static arch=linux-rhel7-x86_64_v4
        ^libxml2@2.10.1%gcc@12.2.0~python arch=linux-rhel7-x86_64_v4
        ^tar@1.34%gcc@12.2.0 zip=pigz arch=linux-rhel7-x86_64_v4
            ^pigz@2.7%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
            ^zstd@1.5.2%gcc@12.2.0+programs compression=none libs=shared,static arch=linux-rhel7-x86_64_v4
    ^libffi@3.4.2%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^ncurses@6.3%gcc@12.2.0~symlinks+termlib abi=none arch=linux-rhel7-x86_64_v4
    ^openssl@1.1.1q%gcc@12.2.0~docs~shared certs=mozilla patches=3fdcf2d arch=linux-rhel7-x86_64_v4
        ^ca-certificates-mozilla@2022-07-19%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^perl@5.34.1%gcc@12.2.0+cpanm+shared+threads arch=linux-rhel7-x86_64_v4
            ^berkeley-db@18.1.40%gcc@12.2.0+cxx~docs+stl patches=26090f4,b231fcc arch=linux-rhel7-x86_64_v4
    ^pkgconf@1.8.0%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^readline@8.1.2%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^sqlite@3.39.2%gcc@12.2.0+column_metadata+dynamic_extensions+fts~functions+rtree arch=linux-rhel7-x86_64_v4
    ^util-linux-uuid@2.37.4%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^xz@5.2.5%gcc@12.2.0~pic libs=shared,static arch=linux-rhel7-x86_64_v4
    ^zlib@1.2.12%gcc@12.2.0+optimize+pic+shared patches=0d38234 arch=linux-rhel7-x86_64_v4

Input spec
--------------------------------
singularity

Concretized
--------------------------------
singularity@3.8.7%gcc@12.2.0+network+suid build_system=makefile arch=linux-rhel7-x86_64_v4
    ^cryptsetup@2.3.5%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^autoconf@2.69%gcc@12.2.0 patches=35c4492,7793209,a49dd5b arch=linux-rhel7-x86_64_v4
            ^perl@5.34.1%gcc@12.2.0+cpanm+shared+threads arch=linux-rhel7-x86_64_v4
                ^berkeley-db@18.1.40%gcc@12.2.0+cxx~docs+stl patches=26090f4,b231fcc arch=linux-rhel7-x86_64_v4
                ^gdbm@1.19%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^automake@1.16.5%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^gettext@0.21%gcc@12.2.0+bzip2+curses+git~libunistring+libxml2+tar+xz arch=linux-rhel7-x86_64_v4
            ^bzip2@1.0.8%gcc@12.2.0~debug~pic+shared arch=linux-rhel7-x86_64_v4
            ^libiconv@1.16%gcc@12.2.0 libs=shared,static arch=linux-rhel7-x86_64_v4
            ^libxml2@2.10.1%gcc@12.2.0~python arch=linux-rhel7-x86_64_v4
            ^ncurses@6.3%gcc@12.2.0~symlinks+termlib abi=none arch=linux-rhel7-x86_64_v4
            ^tar@1.34%gcc@12.2.0 zip=pigz arch=linux-rhel7-x86_64_v4
                ^pigz@2.7%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
                ^zstd@1.5.2%gcc@12.2.0+programs compression=none libs=shared,static arch=linux-rhel7-x86_64_v4
            ^xz@5.2.5%gcc@12.2.0~pic libs=shared,static arch=linux-rhel7-x86_64_v4
        ^json-c@0.16%gcc@12.2.0~ipo build_type=RelWithDebInfo arch=linux-rhel7-x86_64_v4
            ^cmake@3.24.2%gcc@12.2.0~doc+ncurses+ownlibs~qt build_type=Release arch=linux-rhel7-x86_64_v4
        ^libtool@2.4.7%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^lvm2@2.03.14%gcc@12.2.0+pkgconfig arch=linux-rhel7-x86_64_v4
            ^libaio@0.3.110%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^m4@1.4.19%gcc@12.2.0+sigsegv patches=9dc5fbd,bfdffa7 arch=linux-rhel7-x86_64_v4
            ^diffutils@3.8%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
            ^libsigsegv@2.13%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^openssl@1.1.1q%gcc@12.2.0~docs~shared certs=mozilla patches=3fdcf2d arch=linux-rhel7-x86_64_v4
            ^ca-certificates-mozilla@2022-07-19%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^pkgconf@1.8.0%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^popt@1.16%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^util-linux@2.38%gcc@12.2.0~bash arch=linux-rhel7-x86_64_v4
            ^python@3.10.6%gcc@12.2.0+bz2+ctypes+dbm~debug+libxml2+lzma~nis~optimizations+pic+pyexpat+pythoncmd+readline+shared+sqlite3+ssl~tix~tkinter~ucs4+uuid+zlib patches=0d98e93,7d40923,f2fd060 arch=linux-rhel7-x86_64_v4
                ^libffi@3.4.2%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
                ^sqlite@3.39.2%gcc@12.2.0+column_metadata+dynamic_extensions+fts~functions+rtree arch=linux-rhel7-x86_64_v4
    ^go@1.18%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^git@2.37.0%gcc@12.2.0+man+nls+perl+subtree~svn~tcltk arch=linux-rhel7-x86_64_v4
            ^curl@7.85.0%gcc@12.2.0~gssapi~ldap~libidn2~librtmp~libssh~libssh2~nghttp2 libs=shared,static tls=openssl arch=linux-rhel7-x86_64_v4
            ^expat@2.4.8%gcc@12.2.0+libbsd arch=linux-rhel7-x86_64_v4
                ^libbsd@0.11.5%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
                    ^libmd@1.0.4%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
            ^libidn2@2.3.0%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
                ^libunistring@0.9.10%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
            ^openssh@9.0p1%gcc@12.2.0+gssapi arch=linux-rhel7-x86_64_v4
                ^krb5@1.19.3%gcc@12.2.0+shared arch=linux-rhel7-x86_64_v4
                    ^bison@3.8.2%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
                ^libedit@3.1-20210216%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
            ^pcre2@10.39%gcc@12.2.0~jit+multibyte arch=linux-rhel7-x86_64_v4
        ^go-bootstrap@1.4-bootstrap-20171003%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^libgpg-error@1.45%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^gawk@5.1.1%gcc@12.2.0~nls arch=linux-rhel7-x86_64_v4
            ^gmp@6.2.1%gcc@12.2.0 libs=shared,static arch=linux-rhel7-x86_64_v4
            ^mpfr@4.1.0%gcc@12.2.0 libs=shared,static arch=linux-rhel7-x86_64_v4
                ^autoconf-archive@2022.02.11%gcc@12.2.0 patches=139214f arch=linux-rhel7-x86_64_v4
                ^texinfo@6.5%gcc@12.2.0 patches=12f6edb,1732115 arch=linux-rhel7-x86_64_v4
            ^readline@8.1.2%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^libseccomp@2.5.3%gcc@12.2.0+python arch=linux-rhel7-x86_64_v4
        ^gperf@3.1%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^py-cython@0.29.32%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
            ^py-pip@22.1.2%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
            ^py-setuptools@65.0.0%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
            ^py-wheel@0.37.1%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
            ^python@3.9.13%gcc@12.2.0+bz2+ctypes+dbm~debug+libxml2+lzma~nis~optimizations+pic+pyexpat+pythoncmd+readline+shared+sqlite3+ssl~tix~tkinter~ucs4+uuid+zlib patches=0d98e93,4c24573,f2fd060 arch=linux-rhel7-x86_64_v4
    ^pkgconf@1.8.0%gcc@12.2.0 build_system=autotools arch=linux-rhel7-x86_64_v4
    ^shadow@4.8.1%gcc@12.2.0 build_system=autotools arch=linux-rhel7-x86_64_v4
    ^squashfs@4.5.1%gcc@12.2.0+gzip~lz4~lzo~xz~zstd default_compression=gzip arch=linux-rhel7-x86_64_v4
        ^zlib@1.2.12%gcc@12.2.0+optimize+pic+shared patches=0d38234 arch=linux-rhel7-x86_64_v4
    ^util-linux-uuid@2.37.4%gcc@12.2.0 arch=linux-rhel7-x86_64_v4

Input spec
--------------------------------
snakemake@7.18.2+ftp+http+s3

Concretized
--------------------------------
snakemake@7.18.2%gcc@12.2.0+ftp~google-cloud+http~reports+s3 build_system=python_pip arch=linux-rhel7-x86_64_v4
    ^py-appdirs@1.4.4%gcc@12.2.0 patches=006d203 arch=linux-rhel7-x86_64_v4
        ^py-setuptools@65.0.0%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^py-boto3@1.18.12%gcc@12.2.0 build_system=python_pip arch=linux-rhel7-x86_64_v4
        ^py-jmespath@0.10.0%gcc@12.2.0 build_system=python_pip arch=linux-rhel7-x86_64_v4
        ^py-s3transfer@0.5.0%gcc@12.2.0 build_system=python_pip arch=linux-rhel7-x86_64_v4
    ^py-botocore@1.21.12%gcc@12.2.0 build_system=python_pip arch=linux-rhel7-x86_64_v4
        ^py-python-dateutil@2.8.2%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
            ^py-setuptools-scm@7.0.5%gcc@12.2.0+toml arch=linux-rhel7-x86_64_v4
            ^py-six@1.16.0%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^py-urllib3@1.26.6%gcc@12.2.0~brotli~secure~socks arch=linux-rhel7-x86_64_v4
    ^py-configargparse@1.2.3%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^py-connectionpool@0.0.3%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^py-datrie@0.8.2%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^py-cython@0.29.32%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^py-pytest-runner@6.0.0%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^py-docutils@0.18.1%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^py-filelock@3.8.0%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^py-setuptools-scm@7.0.5%gcc@12.2.0+toml arch=linux-rhel7-x86_64_v4
            ^py-packaging@21.3%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
                ^py-pyparsing@3.0.9%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
            ^py-tomli@2.0.1%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^py-ftputil@5.0.4%gcc@12.2.0 build_system=python_pip arch=linux-rhel7-x86_64_v4
    ^py-gitpython@3.1.24%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^py-gitdb@4.0.9%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
            ^py-smmap@5.0.0%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^py-typing-extensions@4.3.0%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
            ^py-flit-core@3.7.1%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^py-jsonschema@4.16.0%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^py-attrs@22.1.0%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^py-hatch-fancy-pypi-readme@22.7.0%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^py-hatch-vcs@0.2.0%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^py-hatchling@1.10.0%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
            ^py-editables@0.3%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
            ^py-pathspec@0.10.1%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
            ^py-pluggy@1.0.0%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^py-pyrsistent@0.18.0%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^py-nbformat@5.1.3%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^py-ipython-genutils@0.2.0%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^py-jupyter-core@4.9.2%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^py-traitlets@5.3.0%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^py-pip@22.1.2%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^py-psutil@5.8.0%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^py-pulp@2.6.0%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^py-pyyaml@6.0%gcc@12.2.0+libyaml arch=linux-rhel7-x86_64_v4
        ^libyaml@0.2.5%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^py-ratelimiter@1.2.0.post0%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^py-requests@2.28.1%gcc@12.2.0~socks arch=linux-rhel7-x86_64_v4
        ^py-certifi@2022.9.14%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^py-charset-normalizer@2.0.12%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^py-idna@3.4%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^py-reretry@0.11.1%gcc@12.2.0 build_system=python_pip arch=linux-rhel7-x86_64_v4
        ^py-pbr@5.10.0%gcc@12.2.0 build_system=python_pip arch=linux-rhel7-x86_64_v4
    ^py-setuptools@59.4.0%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^py-smart-open@5.2.1%gcc@12.2.0~azure~gcs+http~s3 arch=linux-rhel7-x86_64_v4
    ^py-stopit@1.1.2%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^py-tabulate@0.8.9%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^py-throttler@1.2.1%gcc@12.2.0 build_system=python_pip patches=720f0b4 arch=linux-rhel7-x86_64_v4
    ^py-toposort@1.6%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^py-wheel@0.37.1%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^py-wrapt@1.13.3%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^py-yte@1.5.1%gcc@12.2.0 build_system=python_pip arch=linux-rhel7-x86_64_v4
        ^py-dpath@2.0.1%gcc@12.2.0 build_system=python_pip arch=linux-rhel7-x86_64_v4
        ^py-plac@1.3.5%gcc@12.2.0 build_system=python_pip arch=linux-rhel7-x86_64_v4
        ^py-poetry-core@1.2.0%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^python@3.10.6%gcc@12.2.0+bz2+ctypes+dbm~debug+libxml2+lzma~nis~optimizations+pic+pyexpat+pythoncmd+readline+shared+sqlite3+ssl~tix~tkinter~ucs4+uuid+zlib patches=0d98e93,7d40923,f2fd060 arch=linux-rhel7-x86_64_v4
        ^bzip2@1.0.8%gcc@12.2.0~debug~pic+shared arch=linux-rhel7-x86_64_v4
            ^diffutils@3.8%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^expat@2.4.8%gcc@12.2.0+libbsd arch=linux-rhel7-x86_64_v4
            ^libbsd@0.11.5%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
                ^libmd@1.0.4%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^gdbm@1.19%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^gettext@0.21%gcc@12.2.0+bzip2+curses+git~libunistring+libxml2+tar+xz arch=linux-rhel7-x86_64_v4
            ^libiconv@1.16%gcc@12.2.0 libs=shared,static arch=linux-rhel7-x86_64_v4
            ^libxml2@2.10.1%gcc@12.2.0~python arch=linux-rhel7-x86_64_v4
            ^tar@1.34%gcc@12.2.0 zip=pigz arch=linux-rhel7-x86_64_v4
                ^pigz@2.7%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
                ^zstd@1.5.2%gcc@12.2.0+programs compression=none libs=shared,static arch=linux-rhel7-x86_64_v4
        ^libffi@3.4.2%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^ncurses@6.3%gcc@12.2.0~symlinks+termlib abi=none arch=linux-rhel7-x86_64_v4
        ^openssl@1.1.1q%gcc@12.2.0~docs~shared certs=mozilla patches=3fdcf2d arch=linux-rhel7-x86_64_v4
            ^ca-certificates-mozilla@2022-07-19%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
            ^perl@5.34.1%gcc@12.2.0+cpanm+shared+threads arch=linux-rhel7-x86_64_v4
                ^berkeley-db@18.1.40%gcc@12.2.0+cxx~docs+stl patches=26090f4,b231fcc arch=linux-rhel7-x86_64_v4
        ^pkgconf@1.8.0%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^readline@8.1.2%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^sqlite@3.39.2%gcc@12.2.0+column_metadata+dynamic_extensions+fts~functions+rtree arch=linux-rhel7-x86_64_v4
        ^util-linux-uuid@2.37.4%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^xz@5.2.5%gcc@12.2.0~pic libs=shared,static arch=linux-rhel7-x86_64_v4
        ^zlib@1.2.12%gcc@12.2.0+optimize+pic+shared patches=0d38234 arch=linux-rhel7-x86_64_v4

Input spec
--------------------------------
time

Concretized
--------------------------------
time@1.9%gcc@12.2.0 build_system=autotools arch=linux-rhel7-x86_64_v4

Input spec
--------------------------------
util-linux

Concretized
--------------------------------
util-linux@2.38%gcc@12.2.0~bash arch=linux-rhel7-x86_64_v4
    ^ncurses@6.3%gcc@12.2.0~symlinks+termlib abi=none arch=linux-rhel7-x86_64_v4
    ^pkgconf@1.8.0%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
    ^python@3.10.6%gcc@12.2.0+bz2+ctypes+dbm~debug+libxml2+lzma~nis~optimizations+pic+pyexpat+pythoncmd+readline+shared+sqlite3+ssl~tix~tkinter~ucs4+uuid+zlib patches=0d98e93,7d40923,f2fd060 arch=linux-rhel7-x86_64_v4
        ^bzip2@1.0.8%gcc@12.2.0~debug~pic+shared arch=linux-rhel7-x86_64_v4
            ^diffutils@3.8%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^expat@2.4.8%gcc@12.2.0+libbsd arch=linux-rhel7-x86_64_v4
            ^libbsd@0.11.5%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
                ^libmd@1.0.4%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^gdbm@1.19%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^gettext@0.21%gcc@12.2.0+bzip2+curses+git~libunistring+libxml2+tar+xz arch=linux-rhel7-x86_64_v4
            ^libiconv@1.16%gcc@12.2.0 libs=shared,static arch=linux-rhel7-x86_64_v4
            ^libxml2@2.10.1%gcc@12.2.0~python arch=linux-rhel7-x86_64_v4
            ^tar@1.34%gcc@12.2.0 zip=pigz arch=linux-rhel7-x86_64_v4
                ^pigz@2.7%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
                ^zstd@1.5.2%gcc@12.2.0+programs compression=none libs=shared,static arch=linux-rhel7-x86_64_v4
        ^libffi@3.4.2%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^openssl@1.1.1q%gcc@12.2.0~docs~shared certs=mozilla patches=3fdcf2d arch=linux-rhel7-x86_64_v4
            ^ca-certificates-mozilla@2022-07-19%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
            ^perl@5.34.1%gcc@12.2.0+cpanm+shared+threads arch=linux-rhel7-x86_64_v4
                ^berkeley-db@18.1.40%gcc@12.2.0+cxx~docs+stl patches=26090f4,b231fcc arch=linux-rhel7-x86_64_v4
        ^readline@8.1.2%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^sqlite@3.39.2%gcc@12.2.0+column_metadata+dynamic_extensions+fts~functions+rtree arch=linux-rhel7-x86_64_v4
        ^util-linux-uuid@2.37.4%gcc@12.2.0 arch=linux-rhel7-x86_64_v4
        ^xz@5.2.5%gcc@12.2.0~pic libs=shared,static arch=linux-rhel7-x86_64_v4
        ^zlib@1.2.12%gcc@12.2.0+optimize+pic+shared patches=0d38234 arch=linux-rhel7-x86_64_v4

Input spec
--------------------------------
xxhash

Concretized
--------------------------------
xxhash@0.8.0%gcc@12.2.0 arch=linux-rhel7-x86_64_v4

