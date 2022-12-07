Input spec
--------------------------------
apptainer

Concretized
--------------------------------
apptainer@1.1.3%gcc@11.3.0+network+suid build_system=makefile arch=linux-ubuntu22.04-skylake
    ^conmon@2.0.30%gcc@11.3.0 build_system=makefile arch=linux-ubuntu22.04-skylake
        ^glib@2.74.1%gcc@11.3.0~libmount build_system=generic tracing=none arch=linux-ubuntu22.04-skylake
            ^elfutils@0.188%gcc@11.3.0~bzip2~debuginfod+nls~xz~zstd build_system=autotools arch=linux-ubuntu22.04-skylake
            ^gettext@0.21.1%gcc@11.3.0+bzip2+curses+git~libunistring+libxml2+tar+xz build_system=autotools arch=linux-ubuntu22.04-skylake
                ^bzip2@1.0.8%gcc@11.3.0~debug~pic+shared build_system=generic arch=linux-ubuntu22.04-skylake
                ^libxml2@2.10.3%gcc@11.3.0~python build_system=autotools arch=linux-ubuntu22.04-skylake
                ^ncurses@6.3%gcc@11.3.0~symlinks+termlib abi=none build_system=autotools arch=linux-ubuntu22.04-skylake
                ^tar@1.34%gcc@11.3.0 build_system=autotools zip=pigz arch=linux-ubuntu22.04-skylake
                    ^pigz@2.7%gcc@11.3.0 build_system=makefile arch=linux-ubuntu22.04-skylake
                    ^zstd@1.5.2%gcc@11.3.0+programs build_system=makefile compression=none libs=shared,static arch=linux-ubuntu22.04-skylake
                ^xz@5.2.7%gcc@11.3.0~pic build_system=autotools libs=shared,static arch=linux-ubuntu22.04-skylake
            ^libffi@3.4.2%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
            ^libiconv@1.16%gcc@11.3.0 build_system=autotools libs=shared,static arch=linux-ubuntu22.04-skylake
            ^meson@0.64.0%gcc@11.3.0 build_system=python_pip patches=0f0b1bd arch=linux-ubuntu22.04-skylake
            ^ninja@1.11.1%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-skylake
                ^re2c@2.2%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-skylake
            ^pcre2@10.42%gcc@11.3.0~jit+multibyte build_system=autotools arch=linux-ubuntu22.04-skylake
            ^perl@5.36.0%gcc@11.3.0+cpanm+shared+threads build_system=generic arch=linux-ubuntu22.04-skylake
                ^berkeley-db@18.1.40%gcc@11.3.0+cxx~docs+stl build_system=autotools patches=26090f4,b231fcc arch=linux-ubuntu22.04-skylake
                ^gdbm@1.23%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
            ^python@3.10.8%gcc@11.3.0+bz2+crypt+ctypes+dbm~debug+libxml2+lzma~nis~optimizations+pic+pyexpat+pythoncmd+readline+shared+sqlite3+ssl~tkinter+uuid+zlib build_system=generic patches=0d98e93,7d40923,f2fd060 arch=linux-ubuntu22.04-skylake
                ^libxcrypt@4.4.33%gcc@11.3.0~obsolete_api build_system=autotools arch=linux-ubuntu22.04-skylake
                ^sqlite@3.40.0%gcc@11.3.0+column_metadata+dynamic_extensions+fts~functions+rtree build_system=autotools arch=linux-ubuntu22.04-skylake
        ^go-md2man@1.0.10%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-skylake
    ^go@1.18%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-skylake
        ^git@2.38.1%gcc@11.3.0+man+nls+perl+subtree~svn~tcltk build_system=autotools arch=linux-ubuntu22.04-skylake
            ^autoconf@2.69%gcc@11.3.0 build_system=autotools patches=35c4492,7793209,a49dd5b arch=linux-ubuntu22.04-skylake
            ^automake@1.16.5%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
            ^curl@7.85.0%gcc@11.3.0~gssapi~ldap~libidn2~librtmp~libssh~libssh2~nghttp2 build_system=autotools libs=shared,static tls=openssl arch=linux-ubuntu22.04-skylake
            ^expat@2.5.0%gcc@11.3.0+libbsd build_system=autotools arch=linux-ubuntu22.04-skylake
                ^libbsd@0.11.5%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
                    ^libmd@1.0.4%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
            ^libidn2@2.3.0%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
                ^libunistring@0.9.10%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
            ^libtool@2.4.7%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
            ^m4@1.4.19%gcc@11.3.0+sigsegv build_system=autotools patches=9dc5fbd,bfdffa7 arch=linux-ubuntu22.04-skylake
                ^diffutils@3.8%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
            ^openssh@9.1p1%gcc@11.3.0+gssapi build_system=autotools arch=linux-ubuntu22.04-skylake
                ^krb5@1.20.1%gcc@11.3.0+shared build_system=autotools arch=linux-ubuntu22.04-skylake
                    ^bison@3.8.2%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
                ^libedit@3.1-20210216%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
            ^openssl@1.1.1s%gcc@11.3.0~docs~shared build_system=generic certs=mozilla arch=linux-ubuntu22.04-skylake
                ^ca-certificates-mozilla@2022-10-11%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-skylake
        ^go-bootstrap@1.4-bootstrap-20171003%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-skylake
    ^libgpg-error@1.46%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
        ^gawk@5.1.1%gcc@11.3.0~nls build_system=autotools arch=linux-ubuntu22.04-skylake
            ^gmp@6.2.1%gcc@11.3.0 build_system=autotools libs=shared,static arch=linux-ubuntu22.04-skylake
            ^libsigsegv@2.13%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
            ^mpfr@4.1.0%gcc@11.3.0 build_system=autotools libs=shared,static arch=linux-ubuntu22.04-skylake
                ^autoconf-archive@2022.02.11%gcc@11.3.0 build_system=autotools patches=139214f arch=linux-ubuntu22.04-skylake
                ^texinfo@7.0%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
            ^readline@8.2%gcc@11.3.0 build_system=autotools patches=bbf97f1 arch=linux-ubuntu22.04-skylake
    ^libseccomp@2.5.3%gcc@11.3.0+python build_system=autotools arch=linux-ubuntu22.04-skylake
        ^gperf@3.1%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
        ^py-cython@0.29.32%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
            ^py-pip@22.2.2%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-skylake
            ^py-setuptools@63.0.0%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-skylake
            ^py-wheel@0.37.1%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-skylake
    ^pkgconf@1.8.0%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
    ^squashfs@4.5.1%gcc@11.3.0+gzip~lz4~lzo~xz~zstd build_system=makefile default_compression=gzip arch=linux-ubuntu22.04-skylake
        ^zlib@1.2.13%gcc@11.3.0+optimize+pic+shared build_system=makefile arch=linux-ubuntu22.04-skylake
    ^util-linux-uuid@2.38.1%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake

Input spec
--------------------------------
hwloc

Concretized
--------------------------------
hwloc@2.8.0%gcc@11.3.0~cairo~cuda~gl~libudev+libxml2~netloc~nvml~oneapi-level-zero~opencl+pci~rocm build_system=autotools libs=shared,static arch=linux-ubuntu22.04-skylake
    ^libpciaccess@0.16%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
        ^libtool@2.4.7%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
            ^m4@1.4.19%gcc@11.3.0+sigsegv build_system=autotools patches=9dc5fbd,bfdffa7 arch=linux-ubuntu22.04-skylake
                ^diffutils@3.8%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
                ^libsigsegv@2.13%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
        ^util-macros@1.19.3%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
    ^libxml2@2.10.3%gcc@11.3.0~python build_system=autotools arch=linux-ubuntu22.04-skylake
        ^libiconv@1.16%gcc@11.3.0 build_system=autotools libs=shared,static arch=linux-ubuntu22.04-skylake
        ^xz@5.2.7%gcc@11.3.0~pic build_system=autotools libs=shared,static arch=linux-ubuntu22.04-skylake
        ^zlib@1.2.13%gcc@11.3.0+optimize+pic+shared build_system=makefile arch=linux-ubuntu22.04-skylake
    ^ncurses@6.3%gcc@11.3.0~symlinks+termlib abi=none build_system=autotools arch=linux-ubuntu22.04-skylake
    ^pkgconf@1.8.0%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake

Input spec
--------------------------------
java

Concretized
--------------------------------
openjdk@11.0.17_8%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-skylake

Input spec
--------------------------------
micromamba

Concretized
--------------------------------
micromamba@1.1.0%gcc@11.3.0~ipo build_system=cmake build_type=RelWithDebInfo linkage=dynamic patches=c6b809a arch=linux-ubuntu22.04-skylake
    ^cli11@2.3.1%gcc@11.3.0~ipo build_system=cmake build_type=RelWithDebInfo arch=linux-ubuntu22.04-skylake
    ^cmake@3.25.1%gcc@11.3.0~doc+ncurses+ownlibs~qt build_system=generic build_type=Release arch=linux-ubuntu22.04-skylake
        ^ncurses@6.3%gcc@11.3.0~symlinks+termlib abi=none build_system=autotools arch=linux-ubuntu22.04-skylake
    ^cpp-termcolor@2.0.0%gcc@11.3.0~ipo build_system=cmake build_type=RelWithDebInfo arch=linux-ubuntu22.04-skylake
    ^curl@7.85.0%gcc@11.3.0~gssapi~ldap~libidn2~librtmp~libssh~libssh2~nghttp2 build_system=autotools libs=shared,static tls=openssl arch=linux-ubuntu22.04-skylake
        ^pkgconf@1.8.0%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
        ^zlib@1.2.13%gcc@11.3.0+optimize+pic+shared build_system=makefile arch=linux-ubuntu22.04-skylake
    ^fmt@9.1.0%gcc@11.3.0~ipo+pic~shared build_system=cmake build_type=RelWithDebInfo cxxstd=11 patches=08fb707 arch=linux-ubuntu22.04-skylake
    ^libarchive@3.5.2%gcc@11.3.0+iconv build_system=autotools compression=bz2lib,lz4,lzma,lzo2,zlib,zstd crypto=mbedtls libs=shared,static programs=none xar=libxml2 arch=linux-ubuntu22.04-skylake
        ^bzip2@1.0.8%gcc@11.3.0~debug~pic+shared build_system=generic arch=linux-ubuntu22.04-skylake
            ^diffutils@3.8%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
        ^libiconv@1.16%gcc@11.3.0 build_system=autotools libs=shared,static arch=linux-ubuntu22.04-skylake
        ^libxml2@2.10.3%gcc@11.3.0~python build_system=autotools arch=linux-ubuntu22.04-skylake
        ^lz4@1.9.4%gcc@11.3.0 build_system=makefile libs=shared,static arch=linux-ubuntu22.04-skylake
        ^lzo@2.10%gcc@11.3.0 build_system=autotools libs=shared,static arch=linux-ubuntu22.04-skylake
        ^mbedtls@2.28.0%gcc@11.3.0+pic build_system=makefile build_type=Release libs=static arch=linux-ubuntu22.04-skylake
        ^xz@5.2.7%gcc@11.3.0~pic build_system=autotools libs=shared,static arch=linux-ubuntu22.04-skylake
        ^zstd@1.5.2%gcc@11.3.0+programs build_system=makefile compression=none libs=shared,static arch=linux-ubuntu22.04-skylake
    ^libreproc@14.2.4%gcc@11.3.0+cxx~ipo+shared build_system=cmake build_type=RelWithDebInfo arch=linux-ubuntu22.04-skylake
    ^libsolv@0.7.22%gcc@11.3.0+conda~ipo+shared build_system=cmake build_type=RelWithDebInfo arch=linux-ubuntu22.04-skylake
        ^expat@2.5.0%gcc@11.3.0+libbsd build_system=autotools arch=linux-ubuntu22.04-skylake
            ^libbsd@0.11.5%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
                ^libmd@1.0.4%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
    ^nlohmann-json@3.11.2%gcc@11.3.0~ipo+multiple_headers build_system=cmake build_type=RelWithDebInfo arch=linux-ubuntu22.04-skylake
    ^openssl@1.1.1s%gcc@11.3.0~docs~shared build_system=generic certs=mozilla arch=linux-ubuntu22.04-skylake
        ^ca-certificates-mozilla@2022-10-11%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-skylake
        ^perl@5.36.0%gcc@11.3.0+cpanm+shared+threads build_system=generic arch=linux-ubuntu22.04-skylake
            ^berkeley-db@18.1.40%gcc@11.3.0+cxx~docs+stl build_system=autotools patches=26090f4,b231fcc arch=linux-ubuntu22.04-skylake
            ^gdbm@1.23%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
                ^readline@8.2%gcc@11.3.0 build_system=autotools patches=bbf97f1 arch=linux-ubuntu22.04-skylake
    ^spdlog@1.10.0%gcc@11.3.0~fmt_external~ipo+shared build_system=cmake build_type=RelWithDebInfo arch=linux-ubuntu22.04-skylake
    ^tl-expected@2022-11-24%gcc@11.3.0~ipo build_system=cmake build_type=RelWithDebInfo arch=linux-ubuntu22.04-skylake
    ^yaml-cpp@0.7.0%gcc@11.3.0~ipo+pic+shared~tests build_system=cmake build_type=RelWithDebInfo arch=linux-ubuntu22.04-skylake

Input spec
--------------------------------
nextflow

Concretized
--------------------------------
nextflow@22.10.1%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-skylake
    ^openjdk@11.0.17_8%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-skylake

Input spec
--------------------------------
py-adlfs@2022

Concretized
--------------------------------
py-adlfs@2022.11.2%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
    ^py-aiohttp@3.8.1%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
        ^py-aiosignal@1.2.0%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
        ^py-async-timeout@4.0.2%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
        ^py-attrs@22.1.0%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
        ^py-charset-normalizer@2.0.12%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
        ^py-frozenlist@1.3.1%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
        ^py-multidict@6.0.2%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
        ^py-setuptools@63.0.0%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-skylake
        ^py-yarl@1.8.1%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
            ^py-cython@0.29.32%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
            ^py-idna@3.4%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
                ^py-flit-core@3.7.1%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
    ^py-azure-datalake-store@0.0.48%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
        ^py-adal@1.2.4%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
            ^py-pyjwt@2.4.0%gcc@11.3.0+crypto build_system=python_pip arch=linux-ubuntu22.04-skylake
            ^py-python-dateutil@2.8.2%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
                ^py-setuptools-scm@7.0.5%gcc@11.3.0+toml build_system=python_pip arch=linux-ubuntu22.04-skylake
                    ^py-packaging@21.3%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
                        ^py-pyparsing@3.0.9%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
                    ^py-tomli@2.0.1%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
        ^py-cffi@1.15.1%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
            ^py-pycparser@2.21%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
        ^py-requests@2.28.1%gcc@11.3.0~socks build_system=python_pip arch=linux-ubuntu22.04-skylake
            ^py-certifi@2022.9.14%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
            ^py-urllib3@1.26.12%gcc@11.3.0~brotli~secure~socks build_system=python_pip arch=linux-ubuntu22.04-skylake
    ^py-azure-storage-blob@12.9.0%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
        ^py-azure-core@1.26.1%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
            ^py-six@1.16.0%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
            ^py-typing-extensions@4.3.0%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
        ^py-cryptography@38.0.1%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
            ^git@2.38.1%gcc@11.3.0+man+nls+perl+subtree~svn~tcltk build_system=autotools arch=linux-ubuntu22.04-skylake
                ^autoconf@2.69%gcc@11.3.0 build_system=autotools patches=35c4492,7793209,a49dd5b arch=linux-ubuntu22.04-skylake
                ^automake@1.16.5%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
                ^curl@7.85.0%gcc@11.3.0~gssapi~ldap~libidn2~librtmp~libssh~libssh2~nghttp2 build_system=autotools libs=shared,static tls=openssl arch=linux-ubuntu22.04-skylake
                ^libidn2@2.3.0%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
                    ^libunistring@0.9.10%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
                ^libtool@2.4.7%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
                ^m4@1.4.19%gcc@11.3.0+sigsegv build_system=autotools patches=9dc5fbd,bfdffa7 arch=linux-ubuntu22.04-skylake
                    ^libsigsegv@2.13%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
                ^openssh@9.1p1%gcc@11.3.0+gssapi build_system=autotools arch=linux-ubuntu22.04-skylake
                    ^krb5@1.20.1%gcc@11.3.0+shared build_system=autotools arch=linux-ubuntu22.04-skylake
                        ^bison@3.8.2%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
                    ^libedit@3.1-20210216%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
                ^pcre2@10.42%gcc@11.3.0~jit+multibyte build_system=autotools arch=linux-ubuntu22.04-skylake
            ^py-setuptools-rust@1.5.1%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
                ^py-semantic-version@2.10.0%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
            ^rust@1.65.0%gcc@11.3.0+analysis+clippy~rls+rustfmt+src build_system=generic extra_targets=none arch=linux-ubuntu22.04-skylake
                ^cmake@3.25.1%gcc@11.3.0~doc+ncurses+ownlibs~qt build_system=generic build_type=Release arch=linux-ubuntu22.04-skylake
                ^gmake@4.3%gcc@11.3.0~guile+nls build_system=autotools patches=599f134 arch=linux-ubuntu22.04-skylake
                    ^texinfo@7.0%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
                ^libgit2@1.5.0%gcc@11.3.0~curl~ipo+mmap+ssh build_system=cmake build_type=RelWithDebInfo https=system arch=linux-ubuntu22.04-skylake
                    ^pcre@8.45%gcc@11.3.0~jit+multibyte+utf build_system=autotools arch=linux-ubuntu22.04-skylake
                ^libssh2@1.10.0%gcc@11.3.0~ipo+shared build_system=cmake build_type=RelWithDebInfo crypto=openssl arch=linux-ubuntu22.04-skylake
                ^ninja@1.11.1%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-skylake
                    ^re2c@2.2%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-skylake
        ^py-msrest@0.6.21%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
            ^py-isodate@0.6.1%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
            ^py-requests-oauthlib@1.3.1%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
                ^py-oauthlib@3.2.1%gcc@11.3.0~rsa~signals~signedtoken build_system=python_pip arch=linux-ubuntu22.04-skylake
    ^py-fsspec@2022.11.0%gcc@11.3.0~http build_system=python_pip arch=linux-ubuntu22.04-skylake
    ^py-pip@22.2.2%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-skylake
    ^py-wheel@0.37.1%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-skylake
    ^python@3.10.8%gcc@11.3.0+bz2+crypt+ctypes+dbm~debug+libxml2+lzma~nis~optimizations+pic+pyexpat+pythoncmd+readline+shared+sqlite3+ssl~tkinter+uuid+zlib build_system=generic patches=0d98e93,7d40923,f2fd060 arch=linux-ubuntu22.04-skylake
        ^bzip2@1.0.8%gcc@11.3.0~debug~pic+shared build_system=generic arch=linux-ubuntu22.04-skylake
            ^diffutils@3.8%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
        ^expat@2.5.0%gcc@11.3.0+libbsd build_system=autotools arch=linux-ubuntu22.04-skylake
            ^libbsd@0.11.5%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
                ^libmd@1.0.4%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
        ^gdbm@1.23%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
        ^gettext@0.21.1%gcc@11.3.0+bzip2+curses+git~libunistring+libxml2+tar+xz build_system=autotools arch=linux-ubuntu22.04-skylake
            ^libiconv@1.16%gcc@11.3.0 build_system=autotools libs=shared,static arch=linux-ubuntu22.04-skylake
            ^libxml2@2.10.3%gcc@11.3.0~python build_system=autotools arch=linux-ubuntu22.04-skylake
            ^tar@1.34%gcc@11.3.0 build_system=autotools zip=pigz arch=linux-ubuntu22.04-skylake
                ^pigz@2.7%gcc@11.3.0 build_system=makefile arch=linux-ubuntu22.04-skylake
                ^zstd@1.5.2%gcc@11.3.0+programs build_system=makefile compression=none libs=shared,static arch=linux-ubuntu22.04-skylake
        ^libffi@3.4.2%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
        ^libxcrypt@4.4.33%gcc@11.3.0~obsolete_api build_system=autotools arch=linux-ubuntu22.04-skylake
        ^ncurses@6.3%gcc@11.3.0~symlinks+termlib abi=none build_system=autotools arch=linux-ubuntu22.04-skylake
        ^openssl@1.1.1s%gcc@11.3.0~docs~shared build_system=generic certs=mozilla arch=linux-ubuntu22.04-skylake
            ^ca-certificates-mozilla@2022-10-11%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-skylake
            ^perl@5.36.0%gcc@11.3.0+cpanm+shared+threads build_system=generic arch=linux-ubuntu22.04-skylake
                ^berkeley-db@18.1.40%gcc@11.3.0+cxx~docs+stl build_system=autotools patches=26090f4,b231fcc arch=linux-ubuntu22.04-skylake
        ^pkgconf@1.8.0%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
        ^readline@8.2%gcc@11.3.0 build_system=autotools patches=bbf97f1 arch=linux-ubuntu22.04-skylake
        ^sqlite@3.40.0%gcc@11.3.0+column_metadata+dynamic_extensions+fts~functions+rtree build_system=autotools arch=linux-ubuntu22.04-skylake
        ^util-linux-uuid@2.38.1%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
        ^xz@5.2.7%gcc@11.3.0~pic build_system=autotools libs=shared,static arch=linux-ubuntu22.04-skylake
        ^zlib@1.2.13%gcc@11.3.0+optimize+pic+shared build_system=makefile arch=linux-ubuntu22.04-skylake

Input spec
--------------------------------
py-azure-identity

Concretized
--------------------------------
py-azure-identity@1.12.0%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
    ^py-azure-core@1.26.1%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
        ^py-requests@2.28.1%gcc@11.3.0~socks build_system=python_pip arch=linux-ubuntu22.04-skylake
            ^py-certifi@2022.9.14%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
            ^py-charset-normalizer@2.0.12%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
            ^py-idna@3.4%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
            ^py-urllib3@1.26.12%gcc@11.3.0~brotli~secure~socks build_system=python_pip arch=linux-ubuntu22.04-skylake
        ^py-typing-extensions@4.3.0%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
            ^py-flit-core@3.7.1%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
    ^py-cryptography@38.0.1%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
        ^git@2.38.1%gcc@11.3.0+man+nls+perl+subtree~svn~tcltk build_system=autotools arch=linux-ubuntu22.04-skylake
            ^autoconf@2.69%gcc@11.3.0 build_system=autotools patches=35c4492,7793209,a49dd5b arch=linux-ubuntu22.04-skylake
            ^automake@1.16.5%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
            ^curl@7.85.0%gcc@11.3.0~gssapi~ldap~libidn2~librtmp~libssh~libssh2~nghttp2 build_system=autotools libs=shared,static tls=openssl arch=linux-ubuntu22.04-skylake
            ^libiconv@1.16%gcc@11.3.0 build_system=autotools libs=shared,static arch=linux-ubuntu22.04-skylake
            ^libidn2@2.3.0%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
                ^libunistring@0.9.10%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
            ^libtool@2.4.7%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
            ^m4@1.4.19%gcc@11.3.0+sigsegv build_system=autotools patches=9dc5fbd,bfdffa7 arch=linux-ubuntu22.04-skylake
                ^libsigsegv@2.13%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
            ^openssh@9.1p1%gcc@11.3.0+gssapi build_system=autotools arch=linux-ubuntu22.04-skylake
                ^krb5@1.20.1%gcc@11.3.0+shared build_system=autotools arch=linux-ubuntu22.04-skylake
                    ^bison@3.8.2%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
                ^libedit@3.1-20210216%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
            ^pcre2@10.42%gcc@11.3.0~jit+multibyte build_system=autotools arch=linux-ubuntu22.04-skylake
            ^perl@5.36.0%gcc@11.3.0+cpanm+shared+threads build_system=generic arch=linux-ubuntu22.04-skylake
                ^berkeley-db@18.1.40%gcc@11.3.0+cxx~docs+stl build_system=autotools patches=26090f4,b231fcc arch=linux-ubuntu22.04-skylake
        ^openssl@1.1.1s%gcc@11.3.0~docs~shared build_system=generic certs=mozilla arch=linux-ubuntu22.04-skylake
            ^ca-certificates-mozilla@2022-10-11%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-skylake
        ^py-cffi@1.15.1%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
            ^py-pycparser@2.21%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
        ^py-setuptools-rust@1.5.1%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
            ^py-semantic-version@2.10.0%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
        ^rust@1.65.0%gcc@11.3.0+analysis+clippy~rls+rustfmt+src build_system=generic extra_targets=none arch=linux-ubuntu22.04-skylake
            ^cmake@3.25.1%gcc@11.3.0~doc+ncurses+ownlibs~qt build_system=generic build_type=Release arch=linux-ubuntu22.04-skylake
            ^gmake@4.3%gcc@11.3.0~guile+nls build_system=autotools patches=599f134 arch=linux-ubuntu22.04-skylake
                ^texinfo@7.0%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
            ^libgit2@1.5.0%gcc@11.3.0~curl~ipo+mmap+ssh build_system=cmake build_type=RelWithDebInfo https=system arch=linux-ubuntu22.04-skylake
                ^pcre@8.45%gcc@11.3.0~jit+multibyte+utf build_system=autotools arch=linux-ubuntu22.04-skylake
            ^libssh2@1.10.0%gcc@11.3.0~ipo+shared build_system=cmake build_type=RelWithDebInfo crypto=openssl arch=linux-ubuntu22.04-skylake
            ^ninja@1.11.1%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-skylake
                ^re2c@2.2%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-skylake
    ^py-msal@1.20.0%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
        ^py-pyjwt@2.4.0%gcc@11.3.0+crypto build_system=python_pip arch=linux-ubuntu22.04-skylake
    ^py-msal-extensions@1.0.0%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
        ^py-portalocker@1.6.0%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
    ^py-pip@22.2.2%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-skylake
    ^py-setuptools@63.0.0%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-skylake
    ^py-six@1.16.0%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
    ^py-wheel@0.37.1%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-skylake
    ^python@3.10.8%gcc@11.3.0+bz2+crypt+ctypes+dbm~debug+libxml2+lzma~nis~optimizations+pic+pyexpat+pythoncmd+readline+shared+sqlite3+ssl~tkinter+uuid+zlib build_system=generic patches=0d98e93,7d40923,f2fd060 arch=linux-ubuntu22.04-skylake
        ^bzip2@1.0.8%gcc@11.3.0~debug~pic+shared build_system=generic arch=linux-ubuntu22.04-skylake
            ^diffutils@3.8%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
        ^expat@2.5.0%gcc@11.3.0+libbsd build_system=autotools arch=linux-ubuntu22.04-skylake
            ^libbsd@0.11.5%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
                ^libmd@1.0.4%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
        ^gdbm@1.23%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
        ^gettext@0.21.1%gcc@11.3.0+bzip2+curses+git~libunistring+libxml2+tar+xz build_system=autotools arch=linux-ubuntu22.04-skylake
            ^libxml2@2.10.3%gcc@11.3.0~python build_system=autotools arch=linux-ubuntu22.04-skylake
            ^tar@1.34%gcc@11.3.0 build_system=autotools zip=pigz arch=linux-ubuntu22.04-skylake
                ^pigz@2.7%gcc@11.3.0 build_system=makefile arch=linux-ubuntu22.04-skylake
                ^zstd@1.5.2%gcc@11.3.0+programs build_system=makefile compression=none libs=shared,static arch=linux-ubuntu22.04-skylake
        ^libffi@3.4.2%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
        ^libxcrypt@4.4.33%gcc@11.3.0~obsolete_api build_system=autotools arch=linux-ubuntu22.04-skylake
        ^ncurses@6.3%gcc@11.3.0~symlinks+termlib abi=none build_system=autotools arch=linux-ubuntu22.04-skylake
        ^pkgconf@1.8.0%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
        ^readline@8.2%gcc@11.3.0 build_system=autotools patches=bbf97f1 arch=linux-ubuntu22.04-skylake
        ^sqlite@3.40.0%gcc@11.3.0+column_metadata+dynamic_extensions+fts~functions+rtree build_system=autotools arch=linux-ubuntu22.04-skylake
        ^util-linux-uuid@2.38.1%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
        ^xz@5.2.7%gcc@11.3.0~pic build_system=autotools libs=shared,static arch=linux-ubuntu22.04-skylake
        ^zlib@1.2.13%gcc@11.3.0+optimize+pic+shared build_system=makefile arch=linux-ubuntu22.04-skylake

Input spec
--------------------------------
py-charmonium-time-block@0.3:0

Concretized
--------------------------------
py-charmonium-time-block@0.3.0%gcc@11.3.0 build_system=python_pip patches=2ca26cf arch=linux-ubuntu22.04-skylake
    ^py-pip@22.2.2%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-skylake
    ^py-poetry-core@1.2.0%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
    ^py-psutil@5.9.2%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
        ^py-setuptools@63.0.0%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-skylake
    ^py-wheel@0.37.1%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-skylake
    ^python@3.10.8%gcc@11.3.0+bz2+crypt+ctypes+dbm~debug+libxml2+lzma~nis~optimizations+pic+pyexpat+pythoncmd+readline+shared+sqlite3+ssl~tkinter+uuid+zlib build_system=generic patches=0d98e93,7d40923,f2fd060 arch=linux-ubuntu22.04-skylake
        ^bzip2@1.0.8%gcc@11.3.0~debug~pic+shared build_system=generic arch=linux-ubuntu22.04-skylake
            ^diffutils@3.8%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
        ^expat@2.5.0%gcc@11.3.0+libbsd build_system=autotools arch=linux-ubuntu22.04-skylake
            ^libbsd@0.11.5%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
                ^libmd@1.0.4%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
        ^gdbm@1.23%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
        ^gettext@0.21.1%gcc@11.3.0+bzip2+curses+git~libunistring+libxml2+tar+xz build_system=autotools arch=linux-ubuntu22.04-skylake
            ^libiconv@1.16%gcc@11.3.0 build_system=autotools libs=shared,static arch=linux-ubuntu22.04-skylake
            ^libxml2@2.10.3%gcc@11.3.0~python build_system=autotools arch=linux-ubuntu22.04-skylake
            ^tar@1.34%gcc@11.3.0 build_system=autotools zip=pigz arch=linux-ubuntu22.04-skylake
                ^pigz@2.7%gcc@11.3.0 build_system=makefile arch=linux-ubuntu22.04-skylake
                ^zstd@1.5.2%gcc@11.3.0+programs build_system=makefile compression=none libs=shared,static arch=linux-ubuntu22.04-skylake
        ^libffi@3.4.2%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
        ^libxcrypt@4.4.33%gcc@11.3.0~obsolete_api build_system=autotools arch=linux-ubuntu22.04-skylake
        ^ncurses@6.3%gcc@11.3.0~symlinks+termlib abi=none build_system=autotools arch=linux-ubuntu22.04-skylake
        ^openssl@1.1.1s%gcc@11.3.0~docs~shared build_system=generic certs=mozilla arch=linux-ubuntu22.04-skylake
            ^ca-certificates-mozilla@2022-10-11%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-skylake
            ^perl@5.36.0%gcc@11.3.0+cpanm+shared+threads build_system=generic arch=linux-ubuntu22.04-skylake
                ^berkeley-db@18.1.40%gcc@11.3.0+cxx~docs+stl build_system=autotools patches=26090f4,b231fcc arch=linux-ubuntu22.04-skylake
        ^pkgconf@1.8.0%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
        ^readline@8.2%gcc@11.3.0 build_system=autotools patches=bbf97f1 arch=linux-ubuntu22.04-skylake
        ^sqlite@3.40.0%gcc@11.3.0+column_metadata+dynamic_extensions+fts~functions+rtree build_system=autotools arch=linux-ubuntu22.04-skylake
        ^util-linux-uuid@2.38.1%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
        ^xz@5.2.7%gcc@11.3.0~pic build_system=autotools libs=shared,static arch=linux-ubuntu22.04-skylake
        ^zlib@1.2.13%gcc@11.3.0+optimize+pic+shared build_system=makefile arch=linux-ubuntu22.04-skylake

Input spec
--------------------------------
py-click@8

Concretized
--------------------------------
py-click@8.1.3%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
    ^py-pip@22.2.2%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-skylake
    ^py-setuptools@63.0.0%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-skylake
    ^py-wheel@0.37.1%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-skylake
    ^python@3.10.8%gcc@11.3.0+bz2+crypt+ctypes+dbm~debug+libxml2+lzma~nis~optimizations+pic+pyexpat+pythoncmd+readline+shared+sqlite3+ssl~tkinter+uuid+zlib build_system=generic patches=0d98e93,7d40923,f2fd060 arch=linux-ubuntu22.04-skylake
        ^bzip2@1.0.8%gcc@11.3.0~debug~pic+shared build_system=generic arch=linux-ubuntu22.04-skylake
            ^diffutils@3.8%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
        ^expat@2.5.0%gcc@11.3.0+libbsd build_system=autotools arch=linux-ubuntu22.04-skylake
            ^libbsd@0.11.5%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
                ^libmd@1.0.4%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
        ^gdbm@1.23%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
        ^gettext@0.21.1%gcc@11.3.0+bzip2+curses+git~libunistring+libxml2+tar+xz build_system=autotools arch=linux-ubuntu22.04-skylake
            ^libiconv@1.16%gcc@11.3.0 build_system=autotools libs=shared,static arch=linux-ubuntu22.04-skylake
            ^libxml2@2.10.3%gcc@11.3.0~python build_system=autotools arch=linux-ubuntu22.04-skylake
            ^tar@1.34%gcc@11.3.0 build_system=autotools zip=pigz arch=linux-ubuntu22.04-skylake
                ^pigz@2.7%gcc@11.3.0 build_system=makefile arch=linux-ubuntu22.04-skylake
                ^zstd@1.5.2%gcc@11.3.0+programs build_system=makefile compression=none libs=shared,static arch=linux-ubuntu22.04-skylake
        ^libffi@3.4.2%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
        ^libxcrypt@4.4.33%gcc@11.3.0~obsolete_api build_system=autotools arch=linux-ubuntu22.04-skylake
        ^ncurses@6.3%gcc@11.3.0~symlinks+termlib abi=none build_system=autotools arch=linux-ubuntu22.04-skylake
        ^openssl@1.1.1s%gcc@11.3.0~docs~shared build_system=generic certs=mozilla arch=linux-ubuntu22.04-skylake
            ^ca-certificates-mozilla@2022-10-11%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-skylake
            ^perl@5.36.0%gcc@11.3.0+cpanm+shared+threads build_system=generic arch=linux-ubuntu22.04-skylake
                ^berkeley-db@18.1.40%gcc@11.3.0+cxx~docs+stl build_system=autotools patches=26090f4,b231fcc arch=linux-ubuntu22.04-skylake
        ^pkgconf@1.8.0%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
        ^readline@8.2%gcc@11.3.0 build_system=autotools patches=bbf97f1 arch=linux-ubuntu22.04-skylake
        ^sqlite@3.40.0%gcc@11.3.0+column_metadata+dynamic_extensions+fts~functions+rtree build_system=autotools arch=linux-ubuntu22.04-skylake
        ^util-linux-uuid@2.38.1%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
        ^xz@5.2.7%gcc@11.3.0~pic build_system=autotools libs=shared,static arch=linux-ubuntu22.04-skylake
        ^zlib@1.2.13%gcc@11.3.0+optimize+pic+shared build_system=makefile arch=linux-ubuntu22.04-skylake

Input spec
--------------------------------
py-fasteners@0.18:0

Concretized
--------------------------------
py-fasteners@0.18%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
    ^py-pip@22.2.2%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-skylake
    ^py-setuptools@63.0.0%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-skylake
    ^py-wheel@0.37.1%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-skylake
    ^python@3.10.8%gcc@11.3.0+bz2+crypt+ctypes+dbm~debug+libxml2+lzma~nis~optimizations+pic+pyexpat+pythoncmd+readline+shared+sqlite3+ssl~tkinter+uuid+zlib build_system=generic patches=0d98e93,7d40923,f2fd060 arch=linux-ubuntu22.04-skylake
        ^bzip2@1.0.8%gcc@11.3.0~debug~pic+shared build_system=generic arch=linux-ubuntu22.04-skylake
            ^diffutils@3.8%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
        ^expat@2.5.0%gcc@11.3.0+libbsd build_system=autotools arch=linux-ubuntu22.04-skylake
            ^libbsd@0.11.5%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
                ^libmd@1.0.4%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
        ^gdbm@1.23%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
        ^gettext@0.21.1%gcc@11.3.0+bzip2+curses+git~libunistring+libxml2+tar+xz build_system=autotools arch=linux-ubuntu22.04-skylake
            ^libiconv@1.16%gcc@11.3.0 build_system=autotools libs=shared,static arch=linux-ubuntu22.04-skylake
            ^libxml2@2.10.3%gcc@11.3.0~python build_system=autotools arch=linux-ubuntu22.04-skylake
            ^tar@1.34%gcc@11.3.0 build_system=autotools zip=pigz arch=linux-ubuntu22.04-skylake
                ^pigz@2.7%gcc@11.3.0 build_system=makefile arch=linux-ubuntu22.04-skylake
                ^zstd@1.5.2%gcc@11.3.0+programs build_system=makefile compression=none libs=shared,static arch=linux-ubuntu22.04-skylake
        ^libffi@3.4.2%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
        ^libxcrypt@4.4.33%gcc@11.3.0~obsolete_api build_system=autotools arch=linux-ubuntu22.04-skylake
        ^ncurses@6.3%gcc@11.3.0~symlinks+termlib abi=none build_system=autotools arch=linux-ubuntu22.04-skylake
        ^openssl@1.1.1s%gcc@11.3.0~docs~shared build_system=generic certs=mozilla arch=linux-ubuntu22.04-skylake
            ^ca-certificates-mozilla@2022-10-11%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-skylake
            ^perl@5.36.0%gcc@11.3.0+cpanm+shared+threads build_system=generic arch=linux-ubuntu22.04-skylake
                ^berkeley-db@18.1.40%gcc@11.3.0+cxx~docs+stl build_system=autotools patches=26090f4,b231fcc arch=linux-ubuntu22.04-skylake
        ^pkgconf@1.8.0%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
        ^readline@8.2%gcc@11.3.0 build_system=autotools patches=bbf97f1 arch=linux-ubuntu22.04-skylake
        ^sqlite@3.40.0%gcc@11.3.0+column_metadata+dynamic_extensions+fts~functions+rtree build_system=autotools arch=linux-ubuntu22.04-skylake
        ^util-linux-uuid@2.38.1%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
        ^xz@5.2.7%gcc@11.3.0~pic build_system=autotools libs=shared,static arch=linux-ubuntu22.04-skylake
        ^zlib@1.2.13%gcc@11.3.0+optimize+pic+shared build_system=makefile arch=linux-ubuntu22.04-skylake

Input spec
--------------------------------
py-gitpython@3

Concretized
--------------------------------
py-gitpython@3.1.27%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
    ^py-gitdb@4.0.9%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
        ^py-smmap@5.0.0%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
    ^py-pip@22.2.2%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-skylake
    ^py-setuptools@63.0.0%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-skylake
    ^py-wheel@0.37.1%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-skylake
    ^python@3.10.8%gcc@11.3.0+bz2+crypt+ctypes+dbm~debug+libxml2+lzma~nis~optimizations+pic+pyexpat+pythoncmd+readline+shared+sqlite3+ssl~tkinter+uuid+zlib build_system=generic patches=0d98e93,7d40923,f2fd060 arch=linux-ubuntu22.04-skylake
        ^bzip2@1.0.8%gcc@11.3.0~debug~pic+shared build_system=generic arch=linux-ubuntu22.04-skylake
            ^diffutils@3.8%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
        ^expat@2.5.0%gcc@11.3.0+libbsd build_system=autotools arch=linux-ubuntu22.04-skylake
            ^libbsd@0.11.5%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
                ^libmd@1.0.4%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
        ^gdbm@1.23%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
        ^gettext@0.21.1%gcc@11.3.0+bzip2+curses+git~libunistring+libxml2+tar+xz build_system=autotools arch=linux-ubuntu22.04-skylake
            ^libiconv@1.16%gcc@11.3.0 build_system=autotools libs=shared,static arch=linux-ubuntu22.04-skylake
            ^libxml2@2.10.3%gcc@11.3.0~python build_system=autotools arch=linux-ubuntu22.04-skylake
            ^tar@1.34%gcc@11.3.0 build_system=autotools zip=pigz arch=linux-ubuntu22.04-skylake
                ^pigz@2.7%gcc@11.3.0 build_system=makefile arch=linux-ubuntu22.04-skylake
                ^zstd@1.5.2%gcc@11.3.0+programs build_system=makefile compression=none libs=shared,static arch=linux-ubuntu22.04-skylake
        ^libffi@3.4.2%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
        ^libxcrypt@4.4.33%gcc@11.3.0~obsolete_api build_system=autotools arch=linux-ubuntu22.04-skylake
        ^ncurses@6.3%gcc@11.3.0~symlinks+termlib abi=none build_system=autotools arch=linux-ubuntu22.04-skylake
        ^openssl@1.1.1s%gcc@11.3.0~docs~shared build_system=generic certs=mozilla arch=linux-ubuntu22.04-skylake
            ^ca-certificates-mozilla@2022-10-11%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-skylake
            ^perl@5.36.0%gcc@11.3.0+cpanm+shared+threads build_system=generic arch=linux-ubuntu22.04-skylake
                ^berkeley-db@18.1.40%gcc@11.3.0+cxx~docs+stl build_system=autotools patches=26090f4,b231fcc arch=linux-ubuntu22.04-skylake
        ^pkgconf@1.8.0%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
        ^readline@8.2%gcc@11.3.0 build_system=autotools patches=bbf97f1 arch=linux-ubuntu22.04-skylake
        ^sqlite@3.40.0%gcc@11.3.0+column_metadata+dynamic_extensions+fts~functions+rtree build_system=autotools arch=linux-ubuntu22.04-skylake
        ^util-linux-uuid@2.38.1%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
        ^xz@5.2.7%gcc@11.3.0~pic build_system=autotools libs=shared,static arch=linux-ubuntu22.04-skylake
        ^zlib@1.2.13%gcc@11.3.0+optimize+pic+shared build_system=makefile arch=linux-ubuntu22.04-skylake

Input spec
--------------------------------
py-pandas

Concretized
--------------------------------
py-pandas@1.5.2%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
    ^py-bottleneck@1.3.5%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
        ^py-versioneer@0.26%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
    ^py-cython@0.29.32%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
    ^py-numexpr@2.8.3%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
        ^py-packaging@21.3%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
            ^py-pyparsing@3.0.9%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
                ^py-flit-core@3.7.1%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
    ^py-numpy@1.23.5%gcc@11.3.0+blas+lapack build_system=python_pip patches=873745d arch=linux-ubuntu22.04-skylake
        ^openblas@0.3.21%gcc@11.3.0~bignuma~consistent_fpcsr+fortran~ilp64+locking+pic+shared build_system=makefile patches=d3d9b15 symbol_suffix=none threads=none arch=linux-ubuntu22.04-skylake
            ^perl@5.36.0%gcc@11.3.0+cpanm+shared+threads build_system=generic arch=linux-ubuntu22.04-skylake
                ^berkeley-db@18.1.40%gcc@11.3.0+cxx~docs+stl build_system=autotools patches=26090f4,b231fcc arch=linux-ubuntu22.04-skylake
    ^py-pip@22.2.2%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-skylake
    ^py-python-dateutil@2.8.2%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
        ^py-setuptools-scm@7.0.5%gcc@11.3.0+toml build_system=python_pip arch=linux-ubuntu22.04-skylake
            ^py-tomli@2.0.1%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
            ^py-typing-extensions@4.3.0%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
        ^py-six@1.16.0%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
    ^py-pytz@2022.2.1%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
    ^py-setuptools@63.0.0%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-skylake
    ^py-wheel@0.37.1%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-skylake
    ^python@3.10.8%gcc@11.3.0+bz2+crypt+ctypes+dbm~debug+libxml2+lzma~nis~optimizations+pic+pyexpat+pythoncmd+readline+shared+sqlite3+ssl~tkinter+uuid+zlib build_system=generic patches=0d98e93,7d40923,f2fd060 arch=linux-ubuntu22.04-skylake
        ^bzip2@1.0.8%gcc@11.3.0~debug~pic+shared build_system=generic arch=linux-ubuntu22.04-skylake
            ^diffutils@3.8%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
        ^expat@2.5.0%gcc@11.3.0+libbsd build_system=autotools arch=linux-ubuntu22.04-skylake
            ^libbsd@0.11.5%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
                ^libmd@1.0.4%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
        ^gdbm@1.23%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
        ^gettext@0.21.1%gcc@11.3.0+bzip2+curses+git~libunistring+libxml2+tar+xz build_system=autotools arch=linux-ubuntu22.04-skylake
            ^libiconv@1.16%gcc@11.3.0 build_system=autotools libs=shared,static arch=linux-ubuntu22.04-skylake
            ^libxml2@2.10.3%gcc@11.3.0~python build_system=autotools arch=linux-ubuntu22.04-skylake
            ^tar@1.34%gcc@11.3.0 build_system=autotools zip=pigz arch=linux-ubuntu22.04-skylake
                ^pigz@2.7%gcc@11.3.0 build_system=makefile arch=linux-ubuntu22.04-skylake
                ^zstd@1.5.2%gcc@11.3.0+programs build_system=makefile compression=none libs=shared,static arch=linux-ubuntu22.04-skylake
        ^libffi@3.4.2%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
        ^libxcrypt@4.4.33%gcc@11.3.0~obsolete_api build_system=autotools arch=linux-ubuntu22.04-skylake
        ^ncurses@6.3%gcc@11.3.0~symlinks+termlib abi=none build_system=autotools arch=linux-ubuntu22.04-skylake
        ^openssl@1.1.1s%gcc@11.3.0~docs~shared build_system=generic certs=mozilla arch=linux-ubuntu22.04-skylake
            ^ca-certificates-mozilla@2022-10-11%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-skylake
        ^pkgconf@1.8.0%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
        ^readline@8.2%gcc@11.3.0 build_system=autotools patches=bbf97f1 arch=linux-ubuntu22.04-skylake
        ^sqlite@3.40.0%gcc@11.3.0+column_metadata+dynamic_extensions+fts~functions+rtree build_system=autotools arch=linux-ubuntu22.04-skylake
        ^util-linux-uuid@2.38.1%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
        ^xz@5.2.7%gcc@11.3.0~pic build_system=autotools libs=shared,static arch=linux-ubuntu22.04-skylake
        ^zlib@1.2.13%gcc@11.3.0+optimize+pic+shared build_system=makefile arch=linux-ubuntu22.04-skylake

Input spec
--------------------------------
py-parsl

Concretized
--------------------------------
py-parsl@1.1.0%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
    ^py-dill@0.3.5.1%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
    ^py-globus-sdk@3.10.1%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
        ^py-cryptography@38.0.1%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
            ^git@2.38.1%gcc@11.3.0+man+nls+perl+subtree~svn~tcltk build_system=autotools arch=linux-ubuntu22.04-skylake
                ^autoconf@2.69%gcc@11.3.0 build_system=autotools patches=35c4492,7793209,a49dd5b arch=linux-ubuntu22.04-skylake
                ^automake@1.16.5%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
                ^curl@7.85.0%gcc@11.3.0~gssapi~ldap~libidn2~librtmp~libssh~libssh2~nghttp2 build_system=autotools libs=shared,static tls=openssl arch=linux-ubuntu22.04-skylake
                ^libidn2@2.3.0%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
                    ^libunistring@0.9.10%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
                ^libtool@2.4.7%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
                ^m4@1.4.19%gcc@11.3.0+sigsegv build_system=autotools patches=9dc5fbd,bfdffa7 arch=linux-ubuntu22.04-skylake
                    ^libsigsegv@2.13%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
                ^openssh@9.1p1%gcc@11.3.0+gssapi build_system=autotools arch=linux-ubuntu22.04-skylake
                    ^krb5@1.20.1%gcc@11.3.0+shared build_system=autotools arch=linux-ubuntu22.04-skylake
                        ^bison@3.8.2%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
                    ^libedit@3.1-20210216%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
                ^pcre2@10.42%gcc@11.3.0~jit+multibyte build_system=autotools arch=linux-ubuntu22.04-skylake
            ^py-cffi@1.15.1%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
                ^py-pycparser@2.21%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
            ^py-setuptools-rust@1.5.1%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
                ^py-semantic-version@2.10.0%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
            ^rust@1.65.0%gcc@11.3.0+analysis+clippy~rls+rustfmt+src build_system=generic extra_targets=none arch=linux-ubuntu22.04-skylake
                ^cmake@3.25.1%gcc@11.3.0~doc+ncurses+ownlibs~qt build_system=generic build_type=Release arch=linux-ubuntu22.04-skylake
                ^gmake@4.3%gcc@11.3.0~guile+nls build_system=autotools patches=599f134 arch=linux-ubuntu22.04-skylake
                    ^texinfo@7.0%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
                ^libgit2@1.5.0%gcc@11.3.0~curl~ipo+mmap+ssh build_system=cmake build_type=RelWithDebInfo https=system arch=linux-ubuntu22.04-skylake
                    ^pcre@8.45%gcc@11.3.0~jit+multibyte+utf build_system=autotools arch=linux-ubuntu22.04-skylake
                ^libssh2@1.10.0%gcc@11.3.0~ipo+shared build_system=cmake build_type=RelWithDebInfo crypto=openssl arch=linux-ubuntu22.04-skylake
                ^ninja@1.11.1%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-skylake
                    ^re2c@2.2%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-skylake
        ^py-pyjwt@2.4.0%gcc@11.3.0+crypto build_system=python_pip arch=linux-ubuntu22.04-skylake
    ^py-paramiko@2.12.0%gcc@11.3.0~invoke build_system=python_pip arch=linux-ubuntu22.04-skylake
        ^py-bcrypt@3.2.0%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
            ^py-six@1.16.0%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
        ^py-pynacl@1.5.0%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
    ^py-pip@22.2.2%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-skylake
    ^py-psutil@5.9.2%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
    ^py-pyzmq@24.0.1%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
        ^libzmq@4.3.4%gcc@11.3.0~docs~drafts+libbsd+libsodium~libunwind build_system=autotools patches=310b8aa arch=linux-ubuntu22.04-skylake
            ^libbsd@0.11.5%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
                ^libmd@1.0.4%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
            ^libsodium@1.0.18%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
        ^py-cython@0.29.32%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
        ^py-gevent@1.5.0%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
            ^py-greenlet@1.1.3%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
        ^py-packaging@21.3%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
            ^py-pyparsing@3.0.9%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
    ^py-requests@2.28.1%gcc@11.3.0~socks build_system=python_pip arch=linux-ubuntu22.04-skylake
        ^py-certifi@2022.9.14%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
        ^py-charset-normalizer@2.0.12%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
        ^py-idna@3.4%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
        ^py-urllib3@1.26.12%gcc@11.3.0~brotli~secure~socks build_system=python_pip arch=linux-ubuntu22.04-skylake
    ^py-setuptools@63.0.0%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-skylake
    ^py-tblib@1.6.0%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
    ^py-typeguard@2.12.1%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
        ^py-setuptools-scm@7.0.5%gcc@11.3.0+toml build_system=python_pip arch=linux-ubuntu22.04-skylake
            ^py-tomli@2.0.1%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
    ^py-typing-extensions@4.3.0%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
        ^py-flit-core@3.7.1%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
    ^py-wheel@0.37.1%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-skylake
    ^python@3.10.8%gcc@11.3.0+bz2+crypt+ctypes+dbm~debug+libxml2+lzma~nis~optimizations+pic+pyexpat+pythoncmd+readline+shared+sqlite3+ssl~tkinter+uuid+zlib build_system=generic patches=0d98e93,7d40923,f2fd060 arch=linux-ubuntu22.04-skylake
        ^bzip2@1.0.8%gcc@11.3.0~debug~pic+shared build_system=generic arch=linux-ubuntu22.04-skylake
            ^diffutils@3.8%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
        ^expat@2.5.0%gcc@11.3.0+libbsd build_system=autotools arch=linux-ubuntu22.04-skylake
        ^gdbm@1.23%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
        ^gettext@0.21.1%gcc@11.3.0+bzip2+curses+git~libunistring+libxml2+tar+xz build_system=autotools arch=linux-ubuntu22.04-skylake
            ^libiconv@1.16%gcc@11.3.0 build_system=autotools libs=shared,static arch=linux-ubuntu22.04-skylake
            ^libxml2@2.10.3%gcc@11.3.0~python build_system=autotools arch=linux-ubuntu22.04-skylake
            ^tar@1.34%gcc@11.3.0 build_system=autotools zip=pigz arch=linux-ubuntu22.04-skylake
                ^pigz@2.7%gcc@11.3.0 build_system=makefile arch=linux-ubuntu22.04-skylake
                ^zstd@1.5.2%gcc@11.3.0+programs build_system=makefile compression=none libs=shared,static arch=linux-ubuntu22.04-skylake
        ^libffi@3.4.2%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
        ^libxcrypt@4.4.33%gcc@11.3.0~obsolete_api build_system=autotools arch=linux-ubuntu22.04-skylake
        ^ncurses@6.3%gcc@11.3.0~symlinks+termlib abi=none build_system=autotools arch=linux-ubuntu22.04-skylake
        ^openssl@1.1.1s%gcc@11.3.0~docs~shared build_system=generic certs=mozilla arch=linux-ubuntu22.04-skylake
            ^ca-certificates-mozilla@2022-10-11%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-skylake
            ^perl@5.36.0%gcc@11.3.0+cpanm+shared+threads build_system=generic arch=linux-ubuntu22.04-skylake
                ^berkeley-db@18.1.40%gcc@11.3.0+cxx~docs+stl build_system=autotools patches=26090f4,b231fcc arch=linux-ubuntu22.04-skylake
        ^pkgconf@1.8.0%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
        ^readline@8.2%gcc@11.3.0 build_system=autotools patches=bbf97f1 arch=linux-ubuntu22.04-skylake
        ^sqlite@3.40.0%gcc@11.3.0+column_metadata+dynamic_extensions+fts~functions+rtree build_system=autotools arch=linux-ubuntu22.04-skylake
        ^util-linux-uuid@2.38.1%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
        ^xz@5.2.7%gcc@11.3.0~pic build_system=autotools libs=shared,static arch=linux-ubuntu22.04-skylake
        ^zlib@1.2.13%gcc@11.3.0+optimize+pic+shared build_system=makefile arch=linux-ubuntu22.04-skylake

Input spec
--------------------------------
py-pip

Concretized
--------------------------------
py-pip@22.2.2%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-skylake
    ^python@3.10.8%gcc@11.3.0+bz2+crypt+ctypes+dbm~debug+libxml2+lzma~nis~optimizations+pic+pyexpat+pythoncmd+readline+shared+sqlite3+ssl~tkinter+uuid+zlib build_system=generic patches=0d98e93,7d40923,f2fd060 arch=linux-ubuntu22.04-skylake
        ^bzip2@1.0.8%gcc@11.3.0~debug~pic+shared build_system=generic arch=linux-ubuntu22.04-skylake
            ^diffutils@3.8%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
        ^expat@2.5.0%gcc@11.3.0+libbsd build_system=autotools arch=linux-ubuntu22.04-skylake
            ^libbsd@0.11.5%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
                ^libmd@1.0.4%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
        ^gdbm@1.23%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
        ^gettext@0.21.1%gcc@11.3.0+bzip2+curses+git~libunistring+libxml2+tar+xz build_system=autotools arch=linux-ubuntu22.04-skylake
            ^libiconv@1.16%gcc@11.3.0 build_system=autotools libs=shared,static arch=linux-ubuntu22.04-skylake
            ^libxml2@2.10.3%gcc@11.3.0~python build_system=autotools arch=linux-ubuntu22.04-skylake
            ^tar@1.34%gcc@11.3.0 build_system=autotools zip=pigz arch=linux-ubuntu22.04-skylake
                ^pigz@2.7%gcc@11.3.0 build_system=makefile arch=linux-ubuntu22.04-skylake
                ^zstd@1.5.2%gcc@11.3.0+programs build_system=makefile compression=none libs=shared,static arch=linux-ubuntu22.04-skylake
        ^libffi@3.4.2%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
        ^libxcrypt@4.4.33%gcc@11.3.0~obsolete_api build_system=autotools arch=linux-ubuntu22.04-skylake
        ^ncurses@6.3%gcc@11.3.0~symlinks+termlib abi=none build_system=autotools arch=linux-ubuntu22.04-skylake
        ^openssl@1.1.1s%gcc@11.3.0~docs~shared build_system=generic certs=mozilla arch=linux-ubuntu22.04-skylake
            ^ca-certificates-mozilla@2022-10-11%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-skylake
            ^perl@5.36.0%gcc@11.3.0+cpanm+shared+threads build_system=generic arch=linux-ubuntu22.04-skylake
                ^berkeley-db@18.1.40%gcc@11.3.0+cxx~docs+stl build_system=autotools patches=26090f4,b231fcc arch=linux-ubuntu22.04-skylake
        ^pkgconf@1.8.0%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
        ^readline@8.2%gcc@11.3.0 build_system=autotools patches=bbf97f1 arch=linux-ubuntu22.04-skylake
        ^sqlite@3.40.0%gcc@11.3.0+column_metadata+dynamic_extensions+fts~functions+rtree build_system=autotools arch=linux-ubuntu22.04-skylake
        ^util-linux-uuid@2.38.1%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
        ^xz@5.2.7%gcc@11.3.0~pic build_system=autotools libs=shared,static arch=linux-ubuntu22.04-skylake
        ^zlib@1.2.13%gcc@11.3.0+optimize+pic+shared build_system=makefile arch=linux-ubuntu22.04-skylake

Input spec
--------------------------------
py-pygithub@1

Concretized
--------------------------------
py-pygithub@1.55%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
    ^py-deprecated@1.2.13%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
        ^py-wrapt@1.14.1%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
    ^py-pip@22.2.2%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-skylake
    ^py-pyjwt@2.4.0%gcc@11.3.0+crypto build_system=python_pip arch=linux-ubuntu22.04-skylake
        ^py-cryptography@38.0.1%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
            ^git@2.38.1%gcc@11.3.0+man+nls+perl+subtree~svn~tcltk build_system=autotools arch=linux-ubuntu22.04-skylake
                ^autoconf@2.69%gcc@11.3.0 build_system=autotools patches=35c4492,7793209,a49dd5b arch=linux-ubuntu22.04-skylake
                ^automake@1.16.5%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
                ^curl@7.85.0%gcc@11.3.0~gssapi~ldap~libidn2~librtmp~libssh~libssh2~nghttp2 build_system=autotools libs=shared,static tls=openssl arch=linux-ubuntu22.04-skylake
                ^libidn2@2.3.0%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
                    ^libunistring@0.9.10%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
                ^libtool@2.4.7%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
                ^m4@1.4.19%gcc@11.3.0+sigsegv build_system=autotools patches=9dc5fbd,bfdffa7 arch=linux-ubuntu22.04-skylake
                    ^libsigsegv@2.13%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
                ^openssh@9.1p1%gcc@11.3.0+gssapi build_system=autotools arch=linux-ubuntu22.04-skylake
                    ^krb5@1.20.1%gcc@11.3.0+shared build_system=autotools arch=linux-ubuntu22.04-skylake
                        ^bison@3.8.2%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
                    ^libedit@3.1-20210216%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
                ^pcre2@10.42%gcc@11.3.0~jit+multibyte build_system=autotools arch=linux-ubuntu22.04-skylake
            ^py-setuptools-rust@1.5.1%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
                ^py-semantic-version@2.10.0%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
                ^py-typing-extensions@4.3.0%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
            ^rust@1.65.0%gcc@11.3.0+analysis+clippy~rls+rustfmt+src build_system=generic extra_targets=none arch=linux-ubuntu22.04-skylake
                ^cmake@3.25.1%gcc@11.3.0~doc+ncurses+ownlibs~qt build_system=generic build_type=Release arch=linux-ubuntu22.04-skylake
                ^gmake@4.3%gcc@11.3.0~guile+nls build_system=autotools patches=599f134 arch=linux-ubuntu22.04-skylake
                    ^texinfo@7.0%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
                ^libgit2@1.5.0%gcc@11.3.0~curl~ipo+mmap+ssh build_system=cmake build_type=RelWithDebInfo https=system arch=linux-ubuntu22.04-skylake
                    ^pcre@8.45%gcc@11.3.0~jit+multibyte+utf build_system=autotools arch=linux-ubuntu22.04-skylake
                ^libssh2@1.10.0%gcc@11.3.0~ipo+shared build_system=cmake build_type=RelWithDebInfo crypto=openssl arch=linux-ubuntu22.04-skylake
                ^ninja@1.11.1%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-skylake
                    ^re2c@2.2%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-skylake
    ^py-pynacl@1.5.0%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
        ^py-cffi@1.15.1%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
            ^py-pycparser@2.21%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
    ^py-requests@2.28.1%gcc@11.3.0~socks build_system=python_pip arch=linux-ubuntu22.04-skylake
        ^py-certifi@2022.9.14%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
        ^py-charset-normalizer@2.0.12%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
        ^py-idna@3.4%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
            ^py-flit-core@3.7.1%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
        ^py-urllib3@1.26.12%gcc@11.3.0~brotli~secure~socks build_system=python_pip arch=linux-ubuntu22.04-skylake
    ^py-setuptools@63.0.0%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-skylake
    ^py-wheel@0.37.1%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-skylake
    ^python@3.10.8%gcc@11.3.0+bz2+crypt+ctypes+dbm~debug+libxml2+lzma~nis~optimizations+pic+pyexpat+pythoncmd+readline+shared+sqlite3+ssl~tkinter+uuid+zlib build_system=generic patches=0d98e93,7d40923,f2fd060 arch=linux-ubuntu22.04-skylake
        ^bzip2@1.0.8%gcc@11.3.0~debug~pic+shared build_system=generic arch=linux-ubuntu22.04-skylake
            ^diffutils@3.8%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
        ^expat@2.5.0%gcc@11.3.0+libbsd build_system=autotools arch=linux-ubuntu22.04-skylake
            ^libbsd@0.11.5%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
                ^libmd@1.0.4%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
        ^gdbm@1.23%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
        ^gettext@0.21.1%gcc@11.3.0+bzip2+curses+git~libunistring+libxml2+tar+xz build_system=autotools arch=linux-ubuntu22.04-skylake
            ^libiconv@1.16%gcc@11.3.0 build_system=autotools libs=shared,static arch=linux-ubuntu22.04-skylake
            ^libxml2@2.10.3%gcc@11.3.0~python build_system=autotools arch=linux-ubuntu22.04-skylake
            ^tar@1.34%gcc@11.3.0 build_system=autotools zip=pigz arch=linux-ubuntu22.04-skylake
                ^pigz@2.7%gcc@11.3.0 build_system=makefile arch=linux-ubuntu22.04-skylake
                ^zstd@1.5.2%gcc@11.3.0+programs build_system=makefile compression=none libs=shared,static arch=linux-ubuntu22.04-skylake
        ^libffi@3.4.2%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
        ^libxcrypt@4.4.33%gcc@11.3.0~obsolete_api build_system=autotools arch=linux-ubuntu22.04-skylake
        ^ncurses@6.3%gcc@11.3.0~symlinks+termlib abi=none build_system=autotools arch=linux-ubuntu22.04-skylake
        ^openssl@1.1.1s%gcc@11.3.0~docs~shared build_system=generic certs=mozilla arch=linux-ubuntu22.04-skylake
            ^ca-certificates-mozilla@2022-10-11%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-skylake
            ^perl@5.36.0%gcc@11.3.0+cpanm+shared+threads build_system=generic arch=linux-ubuntu22.04-skylake
                ^berkeley-db@18.1.40%gcc@11.3.0+cxx~docs+stl build_system=autotools patches=26090f4,b231fcc arch=linux-ubuntu22.04-skylake
        ^pkgconf@1.8.0%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
        ^readline@8.2%gcc@11.3.0 build_system=autotools patches=bbf97f1 arch=linux-ubuntu22.04-skylake
        ^sqlite@3.40.0%gcc@11.3.0+column_metadata+dynamic_extensions+fts~functions+rtree build_system=autotools arch=linux-ubuntu22.04-skylake
        ^util-linux-uuid@2.38.1%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
        ^xz@5.2.7%gcc@11.3.0~pic build_system=autotools libs=shared,static arch=linux-ubuntu22.04-skylake
        ^zlib@1.2.13%gcc@11.3.0+optimize+pic+shared build_system=makefile arch=linux-ubuntu22.04-skylake

Input spec
--------------------------------
py-pyyaml@6

Concretized
--------------------------------
py-pyyaml@6.0%gcc@11.3.0+libyaml build_system=python_pip arch=linux-ubuntu22.04-skylake
    ^libyaml@0.2.5%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
    ^py-cython@0.29.32%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
    ^py-pip@22.2.2%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-skylake
    ^py-setuptools@63.0.0%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-skylake
    ^py-wheel@0.37.1%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-skylake
    ^python@3.10.8%gcc@11.3.0+bz2+crypt+ctypes+dbm~debug+libxml2+lzma~nis~optimizations+pic+pyexpat+pythoncmd+readline+shared+sqlite3+ssl~tkinter+uuid+zlib build_system=generic patches=0d98e93,7d40923,f2fd060 arch=linux-ubuntu22.04-skylake
        ^bzip2@1.0.8%gcc@11.3.0~debug~pic+shared build_system=generic arch=linux-ubuntu22.04-skylake
            ^diffutils@3.8%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
        ^expat@2.5.0%gcc@11.3.0+libbsd build_system=autotools arch=linux-ubuntu22.04-skylake
            ^libbsd@0.11.5%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
                ^libmd@1.0.4%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
        ^gdbm@1.23%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
        ^gettext@0.21.1%gcc@11.3.0+bzip2+curses+git~libunistring+libxml2+tar+xz build_system=autotools arch=linux-ubuntu22.04-skylake
            ^libiconv@1.16%gcc@11.3.0 build_system=autotools libs=shared,static arch=linux-ubuntu22.04-skylake
            ^libxml2@2.10.3%gcc@11.3.0~python build_system=autotools arch=linux-ubuntu22.04-skylake
            ^tar@1.34%gcc@11.3.0 build_system=autotools zip=pigz arch=linux-ubuntu22.04-skylake
                ^pigz@2.7%gcc@11.3.0 build_system=makefile arch=linux-ubuntu22.04-skylake
                ^zstd@1.5.2%gcc@11.3.0+programs build_system=makefile compression=none libs=shared,static arch=linux-ubuntu22.04-skylake
        ^libffi@3.4.2%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
        ^libxcrypt@4.4.33%gcc@11.3.0~obsolete_api build_system=autotools arch=linux-ubuntu22.04-skylake
        ^ncurses@6.3%gcc@11.3.0~symlinks+termlib abi=none build_system=autotools arch=linux-ubuntu22.04-skylake
        ^openssl@1.1.1s%gcc@11.3.0~docs~shared build_system=generic certs=mozilla arch=linux-ubuntu22.04-skylake
            ^ca-certificates-mozilla@2022-10-11%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-skylake
            ^perl@5.36.0%gcc@11.3.0+cpanm+shared+threads build_system=generic arch=linux-ubuntu22.04-skylake
                ^berkeley-db@18.1.40%gcc@11.3.0+cxx~docs+stl build_system=autotools patches=26090f4,b231fcc arch=linux-ubuntu22.04-skylake
        ^pkgconf@1.8.0%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
        ^readline@8.2%gcc@11.3.0 build_system=autotools patches=bbf97f1 arch=linux-ubuntu22.04-skylake
        ^sqlite@3.40.0%gcc@11.3.0+column_metadata+dynamic_extensions+fts~functions+rtree build_system=autotools arch=linux-ubuntu22.04-skylake
        ^util-linux-uuid@2.38.1%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
        ^xz@5.2.7%gcc@11.3.0~pic build_system=autotools libs=shared,static arch=linux-ubuntu22.04-skylake
        ^zlib@1.2.13%gcc@11.3.0+optimize+pic+shared build_system=makefile arch=linux-ubuntu22.04-skylake

Input spec
--------------------------------
py-tqdm

Concretized
--------------------------------
py-tqdm@4.64.1%gcc@11.3.0~notebook~telegram build_system=python_pip arch=linux-ubuntu22.04-skylake
    ^py-pip@22.2.2%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-skylake
    ^py-setuptools@63.0.0%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-skylake
    ^py-setuptools-scm@7.0.5%gcc@11.3.0+toml build_system=python_pip arch=linux-ubuntu22.04-skylake
        ^py-packaging@21.3%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
            ^py-pyparsing@3.0.9%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
        ^py-tomli@2.0.1%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
            ^py-flit-core@3.7.1%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
        ^py-typing-extensions@4.3.0%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
    ^py-wheel@0.37.1%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-skylake
    ^python@3.10.8%gcc@11.3.0+bz2+crypt+ctypes+dbm~debug+libxml2+lzma~nis~optimizations+pic+pyexpat+pythoncmd+readline+shared+sqlite3+ssl~tkinter+uuid+zlib build_system=generic patches=0d98e93,7d40923,f2fd060 arch=linux-ubuntu22.04-skylake
        ^bzip2@1.0.8%gcc@11.3.0~debug~pic+shared build_system=generic arch=linux-ubuntu22.04-skylake
            ^diffutils@3.8%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
        ^expat@2.5.0%gcc@11.3.0+libbsd build_system=autotools arch=linux-ubuntu22.04-skylake
            ^libbsd@0.11.5%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
                ^libmd@1.0.4%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
        ^gdbm@1.23%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
        ^gettext@0.21.1%gcc@11.3.0+bzip2+curses+git~libunistring+libxml2+tar+xz build_system=autotools arch=linux-ubuntu22.04-skylake
            ^libiconv@1.16%gcc@11.3.0 build_system=autotools libs=shared,static arch=linux-ubuntu22.04-skylake
            ^libxml2@2.10.3%gcc@11.3.0~python build_system=autotools arch=linux-ubuntu22.04-skylake
            ^tar@1.34%gcc@11.3.0 build_system=autotools zip=pigz arch=linux-ubuntu22.04-skylake
                ^pigz@2.7%gcc@11.3.0 build_system=makefile arch=linux-ubuntu22.04-skylake
                ^zstd@1.5.2%gcc@11.3.0+programs build_system=makefile compression=none libs=shared,static arch=linux-ubuntu22.04-skylake
        ^libffi@3.4.2%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
        ^libxcrypt@4.4.33%gcc@11.3.0~obsolete_api build_system=autotools arch=linux-ubuntu22.04-skylake
        ^ncurses@6.3%gcc@11.3.0~symlinks+termlib abi=none build_system=autotools arch=linux-ubuntu22.04-skylake
        ^openssl@1.1.1s%gcc@11.3.0~docs~shared build_system=generic certs=mozilla arch=linux-ubuntu22.04-skylake
            ^ca-certificates-mozilla@2022-10-11%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-skylake
            ^perl@5.36.0%gcc@11.3.0+cpanm+shared+threads build_system=generic arch=linux-ubuntu22.04-skylake
                ^berkeley-db@18.1.40%gcc@11.3.0+cxx~docs+stl build_system=autotools patches=26090f4,b231fcc arch=linux-ubuntu22.04-skylake
        ^pkgconf@1.8.0%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
        ^readline@8.2%gcc@11.3.0 build_system=autotools patches=bbf97f1 arch=linux-ubuntu22.04-skylake
        ^sqlite@3.40.0%gcc@11.3.0+column_metadata+dynamic_extensions+fts~functions+rtree build_system=autotools arch=linux-ubuntu22.04-skylake
        ^util-linux-uuid@2.38.1%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
        ^xz@5.2.7%gcc@11.3.0~pic build_system=autotools libs=shared,static arch=linux-ubuntu22.04-skylake
        ^zlib@1.2.13%gcc@11.3.0+optimize+pic+shared build_system=makefile arch=linux-ubuntu22.04-skylake

Input spec
--------------------------------
py-xxhash

Concretized
--------------------------------
py-xxhash@2.0.2%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
    ^py-pip@22.2.2%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-skylake
    ^py-setuptools@63.0.0%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-skylake
    ^py-wheel@0.37.1%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-skylake
    ^python@3.10.8%gcc@11.3.0+bz2+crypt+ctypes+dbm~debug+libxml2+lzma~nis~optimizations+pic+pyexpat+pythoncmd+readline+shared+sqlite3+ssl~tkinter+uuid+zlib build_system=generic patches=0d98e93,7d40923,f2fd060 arch=linux-ubuntu22.04-skylake
        ^bzip2@1.0.8%gcc@11.3.0~debug~pic+shared build_system=generic arch=linux-ubuntu22.04-skylake
            ^diffutils@3.8%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
        ^expat@2.5.0%gcc@11.3.0+libbsd build_system=autotools arch=linux-ubuntu22.04-skylake
            ^libbsd@0.11.5%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
                ^libmd@1.0.4%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
        ^gdbm@1.23%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
        ^gettext@0.21.1%gcc@11.3.0+bzip2+curses+git~libunistring+libxml2+tar+xz build_system=autotools arch=linux-ubuntu22.04-skylake
            ^libiconv@1.16%gcc@11.3.0 build_system=autotools libs=shared,static arch=linux-ubuntu22.04-skylake
            ^libxml2@2.10.3%gcc@11.3.0~python build_system=autotools arch=linux-ubuntu22.04-skylake
            ^tar@1.34%gcc@11.3.0 build_system=autotools zip=pigz arch=linux-ubuntu22.04-skylake
                ^pigz@2.7%gcc@11.3.0 build_system=makefile arch=linux-ubuntu22.04-skylake
                ^zstd@1.5.2%gcc@11.3.0+programs build_system=makefile compression=none libs=shared,static arch=linux-ubuntu22.04-skylake
        ^libffi@3.4.2%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
        ^libxcrypt@4.4.33%gcc@11.3.0~obsolete_api build_system=autotools arch=linux-ubuntu22.04-skylake
        ^ncurses@6.3%gcc@11.3.0~symlinks+termlib abi=none build_system=autotools arch=linux-ubuntu22.04-skylake
        ^openssl@1.1.1s%gcc@11.3.0~docs~shared build_system=generic certs=mozilla arch=linux-ubuntu22.04-skylake
            ^ca-certificates-mozilla@2022-10-11%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-skylake
            ^perl@5.36.0%gcc@11.3.0+cpanm+shared+threads build_system=generic arch=linux-ubuntu22.04-skylake
                ^berkeley-db@18.1.40%gcc@11.3.0+cxx~docs+stl build_system=autotools patches=26090f4,b231fcc arch=linux-ubuntu22.04-skylake
        ^pkgconf@1.8.0%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
        ^readline@8.2%gcc@11.3.0 build_system=autotools patches=bbf97f1 arch=linux-ubuntu22.04-skylake
        ^sqlite@3.40.0%gcc@11.3.0+column_metadata+dynamic_extensions+fts~functions+rtree build_system=autotools arch=linux-ubuntu22.04-skylake
        ^util-linux-uuid@2.38.1%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
        ^xz@5.2.7%gcc@11.3.0~pic build_system=autotools libs=shared,static arch=linux-ubuntu22.04-skylake
        ^zlib@1.2.13%gcc@11.3.0+optimize+pic+shared build_system=makefile arch=linux-ubuntu22.04-skylake
    ^xxhash@0.8.0%gcc@11.3.0 build_system=makefile arch=linux-ubuntu22.04-skylake

Input spec
--------------------------------
python@3.10

Concretized
--------------------------------
python@3.10.8%gcc@11.3.0+bz2+crypt+ctypes+dbm~debug+libxml2+lzma~nis~optimizations+pic+pyexpat+pythoncmd+readline+shared+sqlite3+ssl~tkinter+uuid+zlib build_system=generic patches=0d98e93,7d40923,f2fd060 arch=linux-ubuntu22.04-skylake
    ^bzip2@1.0.8%gcc@11.3.0~debug~pic+shared build_system=generic arch=linux-ubuntu22.04-skylake
        ^diffutils@3.8%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
    ^expat@2.5.0%gcc@11.3.0+libbsd build_system=autotools arch=linux-ubuntu22.04-skylake
        ^libbsd@0.11.5%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
            ^libmd@1.0.4%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
    ^gdbm@1.23%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
    ^gettext@0.21.1%gcc@11.3.0+bzip2+curses+git~libunistring+libxml2+tar+xz build_system=autotools arch=linux-ubuntu22.04-skylake
        ^libiconv@1.16%gcc@11.3.0 build_system=autotools libs=shared,static arch=linux-ubuntu22.04-skylake
        ^libxml2@2.10.3%gcc@11.3.0~python build_system=autotools arch=linux-ubuntu22.04-skylake
        ^tar@1.34%gcc@11.3.0 build_system=autotools zip=pigz arch=linux-ubuntu22.04-skylake
            ^pigz@2.7%gcc@11.3.0 build_system=makefile arch=linux-ubuntu22.04-skylake
            ^zstd@1.5.2%gcc@11.3.0+programs build_system=makefile compression=none libs=shared,static arch=linux-ubuntu22.04-skylake
    ^libffi@3.4.2%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
    ^libxcrypt@4.4.33%gcc@11.3.0~obsolete_api build_system=autotools arch=linux-ubuntu22.04-skylake
    ^ncurses@6.3%gcc@11.3.0~symlinks+termlib abi=none build_system=autotools arch=linux-ubuntu22.04-skylake
    ^openssl@1.1.1s%gcc@11.3.0~docs~shared build_system=generic certs=mozilla arch=linux-ubuntu22.04-skylake
        ^ca-certificates-mozilla@2022-10-11%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-skylake
        ^perl@5.36.0%gcc@11.3.0+cpanm+shared+threads build_system=generic arch=linux-ubuntu22.04-skylake
            ^berkeley-db@18.1.40%gcc@11.3.0+cxx~docs+stl build_system=autotools patches=26090f4,b231fcc arch=linux-ubuntu22.04-skylake
    ^pkgconf@1.8.0%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
    ^readline@8.2%gcc@11.3.0 build_system=autotools patches=bbf97f1 arch=linux-ubuntu22.04-skylake
    ^sqlite@3.40.0%gcc@11.3.0+column_metadata+dynamic_extensions+fts~functions+rtree build_system=autotools arch=linux-ubuntu22.04-skylake
    ^util-linux-uuid@2.38.1%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
    ^xz@5.2.7%gcc@11.3.0~pic build_system=autotools libs=shared,static arch=linux-ubuntu22.04-skylake
    ^zlib@1.2.13%gcc@11.3.0+optimize+pic+shared build_system=makefile arch=linux-ubuntu22.04-skylake

Input spec
--------------------------------
snakemake@7.18.2+ftp+http+reports+s3

Concretized
--------------------------------
snakemake@7.18.2%gcc@11.3.0+ftp~google-cloud+http+reports+s3 build_system=python_pip arch=linux-ubuntu22.04-skylake
    ^py-appdirs@1.4.4%gcc@11.3.0 build_system=python_pip patches=006d203 arch=linux-ubuntu22.04-skylake
    ^py-boto3@1.26.26%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
        ^py-jmespath@1.0.1%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
        ^py-s3transfer@0.6.0%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
    ^py-botocore@1.29.26%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
        ^py-python-dateutil@2.8.2%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
            ^py-setuptools-scm@7.0.5%gcc@11.3.0+toml build_system=python_pip arch=linux-ubuntu22.04-skylake
                ^py-typing-extensions@4.3.0%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
            ^py-six@1.16.0%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
        ^py-urllib3@1.26.12%gcc@11.3.0~brotli~secure~socks build_system=python_pip arch=linux-ubuntu22.04-skylake
    ^py-configargparse@1.2.3%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
    ^py-connectionpool@0.0.3%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
    ^py-datrie@0.8.2%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
        ^py-cython@0.29.32%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
        ^py-pytest-runner@6.0.0%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
    ^py-docutils@0.19%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
    ^py-ftputil@5.0.4%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
    ^py-gitpython@3.1.27%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
        ^py-gitdb@4.0.9%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
            ^py-smmap@5.0.0%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
    ^py-jinja2@3.1.2%gcc@11.3.0~i18n build_system=python_pip arch=linux-ubuntu22.04-skylake
        ^py-markupsafe@2.1.1%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
    ^py-jsonschema@4.16.0%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
        ^py-attrs@22.1.0%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
        ^py-hatch-fancy-pypi-readme@22.7.0%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
            ^py-tomli@2.0.1%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
        ^py-hatch-vcs@0.2.0%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
        ^py-hatchling@1.10.0%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
            ^py-editables@0.3%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
            ^py-packaging@21.3%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
            ^py-pathspec@0.10.1%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
            ^py-pluggy@1.0.0%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
        ^py-pyrsistent@0.18.1%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
    ^py-nbformat@5.7.0%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
        ^py-fastjsonschema@2.16.2%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
        ^py-hatch-nodejs-version@0.3.1%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
        ^py-jupyter-core@5.1.0%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
            ^py-platformdirs@2.5.2%gcc@11.3.0~wheel build_system=python_pip arch=linux-ubuntu22.04-skylake
        ^py-traitlets@5.3.0%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
    ^py-networkx@2.8.6%gcc@11.3.0~extra build_system=python_pip arch=linux-ubuntu22.04-skylake
        ^py-matplotlib@3.6.2%gcc@11.3.0~animation~fonts~latex~movies backend=agg build_system=python_pip arch=linux-ubuntu22.04-skylake
            ^freetype@2.11.1%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
            ^libpng@1.6.37%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
            ^py-contourpy@1.0.5%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
            ^py-cycler@0.11.0%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
            ^py-fonttools@4.37.3%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
            ^py-kiwisolver@1.4.4%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
                ^py-cppy@1.2.1%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
            ^py-pillow@9.2.0%gcc@11.3.0~freetype~imagequant+jpeg~jpeg2000~lcms~raqm~tiff~webp~xcb+zlib build_system=python_pip arch=linux-ubuntu22.04-skylake
                ^libjpeg-turbo@2.1.4%gcc@11.3.0~ipo~jpeg8+shared+static build_system=cmake build_type=RelWithDebInfo arch=linux-ubuntu22.04-skylake
                    ^nasm@2.15.05%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
            ^py-pyparsing@3.0.9%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
            ^qhull@2020.2%gcc@11.3.0~ipo build_system=cmake build_type=RelWithDebInfo arch=linux-ubuntu22.04-skylake
                ^cmake@3.25.1%gcc@11.3.0~doc+ncurses+ownlibs~qt build_system=generic build_type=Release arch=linux-ubuntu22.04-skylake
        ^py-numpy@1.23.5%gcc@11.3.0+blas+lapack build_system=python_pip patches=873745d arch=linux-ubuntu22.04-skylake
            ^openblas@0.3.21%gcc@11.3.0~bignuma~consistent_fpcsr+fortran~ilp64+locking+pic+shared build_system=makefile patches=d3d9b15 symbol_suffix=none threads=none arch=linux-ubuntu22.04-skylake
        ^py-pandas@1.5.2%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
            ^py-bottleneck@1.3.5%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
                ^py-versioneer@0.26%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
            ^py-numexpr@2.8.3%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
            ^py-pytz@2022.2.1%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
        ^py-scipy@1.9.3%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
            ^py-build@0.7.0%gcc@11.3.0~virtualenv build_system=python_pip patches=9a151ac arch=linux-ubuntu22.04-skylake
                ^py-pep517@0.12.0%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
            ^py-meson-python@0.10.0%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
                ^meson@0.64.0%gcc@11.3.0 build_system=python_pip patches=0f0b1bd arch=linux-ubuntu22.04-skylake
                ^py-pyproject-metadata@0.6.1%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
            ^py-pybind11@2.10.1%gcc@11.3.0~ipo build_system=cmake build_type=RelWithDebInfo arch=linux-ubuntu22.04-skylake
                ^ninja@1.11.1%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-skylake
                    ^re2c@2.2%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-skylake
            ^py-pythran@0.11.0%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
                ^py-beniget@0.4.1%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
                ^py-gast@0.5.3%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
                ^py-ply@3.11%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
    ^py-pip@22.2.2%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-skylake
    ^py-psutil@5.9.2%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
    ^py-pulp@2.6.0%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
    ^py-pygments@2.13.0%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
    ^py-pygraphviz@1.10%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
        ^graphviz@2.49.0%gcc@11.3.0~doc~expat~ghostscript~gtkplus~gts~java~libgd~pangocairo~poppler~qt~quartz~x build_system=autotools arch=linux-ubuntu22.04-skylake
            ^autoconf@2.69%gcc@11.3.0 build_system=autotools patches=35c4492,7793209,a49dd5b arch=linux-ubuntu22.04-skylake
                ^m4@1.4.19%gcc@11.3.0+sigsegv build_system=autotools patches=9dc5fbd,bfdffa7 arch=linux-ubuntu22.04-skylake
                    ^libsigsegv@2.13%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
            ^automake@1.16.5%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
            ^bison@3.8.2%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
            ^flex@2.6.3%gcc@11.3.0+lex~nls build_system=autotools arch=linux-ubuntu22.04-skylake
                ^findutils@4.9.0%gcc@11.3.0 build_system=autotools patches=440b954 arch=linux-ubuntu22.04-skylake
            ^libtool@2.4.7%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
            ^sed@4.8%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
    ^py-pyyaml@6.0%gcc@11.3.0+libyaml build_system=python_pip arch=linux-ubuntu22.04-skylake
        ^libyaml@0.2.5%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
    ^py-requests@2.28.1%gcc@11.3.0~socks build_system=python_pip arch=linux-ubuntu22.04-skylake
        ^py-certifi@2022.9.14%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
        ^py-charset-normalizer@2.0.12%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
        ^py-idna@3.4%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
            ^py-flit-core@3.7.1%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
    ^py-reretry@0.11.1%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
        ^py-pbr@5.10.0%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
    ^py-setuptools@63.0.0%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-skylake
    ^py-smart-open@5.2.1%gcc@11.3.0~azure~gcs+http~s3 build_system=python_pip arch=linux-ubuntu22.04-skylake
    ^py-stopit@1.1.2%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
    ^py-tabulate@0.8.9%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
    ^py-throttler@1.2.2%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
    ^py-toposort@1.6%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
    ^py-wheel@0.37.1%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-skylake
    ^py-wrapt@1.14.1%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
    ^py-yte@1.5.1%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
        ^py-dpath@2.0.1%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
        ^py-plac@1.3.5%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
        ^py-poetry-core@1.2.0%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-skylake
    ^python@3.10.8%gcc@11.3.0+bz2+crypt+ctypes+dbm~debug+libxml2+lzma~nis~optimizations+pic+pyexpat+pythoncmd+readline+shared+sqlite3+ssl~tkinter+uuid+zlib build_system=generic patches=0d98e93,7d40923,f2fd060 arch=linux-ubuntu22.04-skylake
        ^bzip2@1.0.8%gcc@11.3.0~debug~pic+shared build_system=generic arch=linux-ubuntu22.04-skylake
            ^diffutils@3.8%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
        ^expat@2.5.0%gcc@11.3.0+libbsd build_system=autotools arch=linux-ubuntu22.04-skylake
            ^libbsd@0.11.5%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
                ^libmd@1.0.4%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
        ^gdbm@1.23%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
        ^gettext@0.21.1%gcc@11.3.0+bzip2+curses+git~libunistring+libxml2+tar+xz build_system=autotools arch=linux-ubuntu22.04-skylake
            ^libiconv@1.16%gcc@11.3.0 build_system=autotools libs=shared,static arch=linux-ubuntu22.04-skylake
            ^libxml2@2.10.3%gcc@11.3.0~python build_system=autotools arch=linux-ubuntu22.04-skylake
            ^tar@1.34%gcc@11.3.0 build_system=autotools zip=pigz arch=linux-ubuntu22.04-skylake
                ^pigz@2.7%gcc@11.3.0 build_system=makefile arch=linux-ubuntu22.04-skylake
                ^zstd@1.5.2%gcc@11.3.0+programs build_system=makefile compression=none libs=shared,static arch=linux-ubuntu22.04-skylake
        ^libffi@3.4.2%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
        ^libxcrypt@4.4.33%gcc@11.3.0~obsolete_api build_system=autotools arch=linux-ubuntu22.04-skylake
        ^ncurses@6.3%gcc@11.3.0~symlinks+termlib abi=none build_system=autotools arch=linux-ubuntu22.04-skylake
        ^openssl@1.1.1s%gcc@11.3.0~docs~shared build_system=generic certs=mozilla arch=linux-ubuntu22.04-skylake
            ^ca-certificates-mozilla@2022-10-11%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-skylake
            ^perl@5.36.0%gcc@11.3.0+cpanm+shared+threads build_system=generic arch=linux-ubuntu22.04-skylake
                ^berkeley-db@18.1.40%gcc@11.3.0+cxx~docs+stl build_system=autotools patches=26090f4,b231fcc arch=linux-ubuntu22.04-skylake
        ^pkgconf@1.8.0%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
        ^readline@8.2%gcc@11.3.0 build_system=autotools patches=bbf97f1 arch=linux-ubuntu22.04-skylake
        ^sqlite@3.40.0%gcc@11.3.0+column_metadata+dynamic_extensions+fts~functions+rtree build_system=autotools arch=linux-ubuntu22.04-skylake
        ^util-linux-uuid@2.38.1%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
        ^xz@5.2.7%gcc@11.3.0~pic build_system=autotools libs=shared,static arch=linux-ubuntu22.04-skylake
        ^zlib@1.2.13%gcc@11.3.0+optimize+pic+shared build_system=makefile arch=linux-ubuntu22.04-skylake

Input spec
--------------------------------
time

Concretized
--------------------------------
time@1.9%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake

Input spec
--------------------------------
util-linux

Concretized
--------------------------------
util-linux@2.38.1%gcc@11.3.0~bash build_system=autotools arch=linux-ubuntu22.04-skylake
    ^libxcrypt@4.4.33%gcc@11.3.0~obsolete_api build_system=autotools arch=linux-ubuntu22.04-skylake
    ^ncurses@6.3%gcc@11.3.0~symlinks+termlib abi=none build_system=autotools arch=linux-ubuntu22.04-skylake
    ^pkgconf@1.8.0%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
    ^python@3.10.8%gcc@11.3.0+bz2+crypt+ctypes+dbm~debug+libxml2+lzma~nis~optimizations+pic+pyexpat+pythoncmd+readline+shared+sqlite3+ssl~tkinter+uuid+zlib build_system=generic patches=0d98e93,7d40923,f2fd060 arch=linux-ubuntu22.04-skylake
        ^bzip2@1.0.8%gcc@11.3.0~debug~pic+shared build_system=generic arch=linux-ubuntu22.04-skylake
            ^diffutils@3.8%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
        ^expat@2.5.0%gcc@11.3.0+libbsd build_system=autotools arch=linux-ubuntu22.04-skylake
            ^libbsd@0.11.5%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
                ^libmd@1.0.4%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
        ^gdbm@1.23%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
        ^gettext@0.21.1%gcc@11.3.0+bzip2+curses+git~libunistring+libxml2+tar+xz build_system=autotools arch=linux-ubuntu22.04-skylake
            ^libiconv@1.16%gcc@11.3.0 build_system=autotools libs=shared,static arch=linux-ubuntu22.04-skylake
            ^libxml2@2.10.3%gcc@11.3.0~python build_system=autotools arch=linux-ubuntu22.04-skylake
            ^tar@1.34%gcc@11.3.0 build_system=autotools zip=pigz arch=linux-ubuntu22.04-skylake
                ^pigz@2.7%gcc@11.3.0 build_system=makefile arch=linux-ubuntu22.04-skylake
                ^zstd@1.5.2%gcc@11.3.0+programs build_system=makefile compression=none libs=shared,static arch=linux-ubuntu22.04-skylake
        ^libffi@3.4.2%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
        ^openssl@1.1.1s%gcc@11.3.0~docs~shared build_system=generic certs=mozilla arch=linux-ubuntu22.04-skylake
            ^ca-certificates-mozilla@2022-10-11%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-skylake
            ^perl@5.36.0%gcc@11.3.0+cpanm+shared+threads build_system=generic arch=linux-ubuntu22.04-skylake
                ^berkeley-db@18.1.40%gcc@11.3.0+cxx~docs+stl build_system=autotools patches=26090f4,b231fcc arch=linux-ubuntu22.04-skylake
        ^readline@8.2%gcc@11.3.0 build_system=autotools patches=bbf97f1 arch=linux-ubuntu22.04-skylake
        ^sqlite@3.40.0%gcc@11.3.0+column_metadata+dynamic_extensions+fts~functions+rtree build_system=autotools arch=linux-ubuntu22.04-skylake
        ^util-linux-uuid@2.38.1%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-skylake
        ^xz@5.2.7%gcc@11.3.0~pic build_system=autotools libs=shared,static arch=linux-ubuntu22.04-skylake
    ^zlib@1.2.13%gcc@11.3.0+optimize+pic+shared build_system=makefile arch=linux-ubuntu22.04-skylake

