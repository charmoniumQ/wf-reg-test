Input spec
--------------------------------
git

Concretized
--------------------------------
git@2.39.1%gcc@11.3.0+man+nls+perl+subtree~svn~tcltk build_system=autotools arch=linux-ubuntu22.04-zen2
    ^autoconf@2.69%gcc@11.3.0 build_system=autotools patches=35c4492,7793209,a49dd5b arch=linux-ubuntu22.04-zen2
    ^automake@1.16.5%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
    ^curl@7.87.0%gcc@11.3.0~gssapi~ldap~libidn2~librtmp~libssh~libssh2~nghttp2 build_system=autotools libs=shared,static tls=openssl arch=linux-ubuntu22.04-zen2
        ^pkgconf@1.8.0%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
    ^expat@2.5.0%gcc@11.3.0+libbsd build_system=autotools arch=linux-ubuntu22.04-zen2
        ^libbsd@0.11.7%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
            ^libmd@1.0.4%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
    ^gettext@0.21.1%gcc@11.3.0+bzip2+curses+git~libunistring+libxml2+tar+xz build_system=autotools arch=linux-ubuntu22.04-zen2
        ^bzip2@1.0.8%gcc@11.3.0~debug~pic+shared build_system=generic arch=linux-ubuntu22.04-zen2
        ^libxml2@2.10.3%gcc@11.3.0~python build_system=autotools arch=linux-ubuntu22.04-zen2
        ^ncurses@6.4%gcc@11.3.0~symlinks+termlib abi=none build_system=autotools arch=linux-ubuntu22.04-zen2
        ^tar@1.34%gcc@11.3.0 build_system=autotools zip=pigz arch=linux-ubuntu22.04-zen2
            ^pigz@2.7%gcc@11.3.0 build_system=makefile arch=linux-ubuntu22.04-zen2
            ^zstd@1.5.2%gcc@11.3.0+programs build_system=makefile compression=none libs=shared,static arch=linux-ubuntu22.04-zen2
        ^xz@5.4.1%gcc@11.3.0~pic build_system=autotools libs=shared,static arch=linux-ubuntu22.04-zen2
    ^libiconv@1.17%gcc@11.3.0 build_system=autotools libs=shared,static arch=linux-ubuntu22.04-zen2
    ^libidn2@2.3.4%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^libunistring@1.1%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
    ^libtool@2.4.7%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
    ^m4@1.4.19%gcc@11.3.0+sigsegv build_system=autotools patches=9dc5fbd,bfdffa7 arch=linux-ubuntu22.04-zen2
        ^diffutils@3.8%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^libsigsegv@2.13%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
    ^openssh@9.1p1%gcc@11.3.0+gssapi build_system=autotools arch=linux-ubuntu22.04-zen2
        ^krb5@1.20.1%gcc@11.3.0+shared build_system=autotools arch=linux-ubuntu22.04-zen2
            ^bison@3.8.2%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^libedit@3.1-20210216%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^libxcrypt@4.4.33%gcc@11.3.0~obsolete_api build_system=autotools arch=linux-ubuntu22.04-zen2
    ^openssl@1.1.1s%gcc@11.3.0~docs~shared build_system=generic certs=mozilla arch=linux-ubuntu22.04-zen2
        ^ca-certificates-mozilla@2023-01-10%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-zen2
    ^pcre2@10.42%gcc@11.3.0~jit+multibyte build_system=autotools arch=linux-ubuntu22.04-zen2
    ^perl@5.34.0%gcc@11.3.0~cpanm+open+shared+threads build_system=generic arch=linux-ubuntu22.04-zen2
    ^zlib@1.2.13%gcc@11.3.0+optimize+pic+shared build_system=makefile arch=linux-ubuntu22.04-zen2

Input spec
--------------------------------
tar

Concretized
--------------------------------
tar@1.34%gcc@11.3.0 build_system=autotools zip=pigz arch=linux-ubuntu22.04-zen2
    ^bzip2@1.0.8%gcc@11.3.0~debug~pic+shared build_system=generic arch=linux-ubuntu22.04-zen2
        ^diffutils@3.8%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
    ^libiconv@1.17%gcc@11.3.0 build_system=autotools libs=shared,static arch=linux-ubuntu22.04-zen2
    ^pigz@2.7%gcc@11.3.0 build_system=makefile arch=linux-ubuntu22.04-zen2
        ^zlib@1.2.13%gcc@11.3.0+optimize+pic+shared build_system=makefile arch=linux-ubuntu22.04-zen2
    ^xz@5.4.1%gcc@11.3.0~pic build_system=autotools libs=shared,static arch=linux-ubuntu22.04-zen2
    ^zstd@1.5.2%gcc@11.3.0+programs build_system=makefile compression=none libs=shared,static arch=linux-ubuntu22.04-zen2

Input spec
--------------------------------
xz

Concretized
--------------------------------
xz@5.4.1%gcc@11.3.0~pic build_system=autotools libs=shared,static arch=linux-ubuntu22.04-zen2

Input spec
--------------------------------
ncdu

Concretized
--------------------------------
ncdu@1.17%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-zen2
    ^ncurses@6.4%gcc@11.3.0~symlinks+termlib abi=none build_system=autotools arch=linux-ubuntu22.04-zen2
    ^pkgconf@1.8.0%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2

Input spec
--------------------------------
file

Concretized
--------------------------------
file@5.44%gcc@11.3.0+static build_system=autotools arch=linux-ubuntu22.04-zen2
    ^bzip2@1.0.8%gcc@11.3.0~debug~pic+shared build_system=generic arch=linux-ubuntu22.04-zen2
        ^diffutils@3.8%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
            ^libiconv@1.17%gcc@11.3.0 build_system=autotools libs=shared,static arch=linux-ubuntu22.04-zen2
    ^xz@5.4.1%gcc@11.3.0~pic build_system=autotools libs=shared,static arch=linux-ubuntu22.04-zen2
    ^zlib@1.2.13%gcc@11.3.0+optimize+pic+shared build_system=makefile arch=linux-ubuntu22.04-zen2
    ^zstd@1.5.2%gcc@11.3.0+programs build_system=makefile compression=none libs=shared,static arch=linux-ubuntu22.04-zen2

Input spec
--------------------------------
hwloc

Concretized
--------------------------------
hwloc@2.9.0%gcc@11.3.0~cairo~cuda~gl~libudev+libxml2~netloc~nvml~oneapi-level-zero~opencl+pci~rocm build_system=autotools libs=shared,static arch=linux-ubuntu22.04-zen2
    ^libpciaccess@0.16%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^libtool@2.4.7%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
            ^m4@1.4.19%gcc@11.3.0+sigsegv build_system=autotools patches=9dc5fbd,bfdffa7 arch=linux-ubuntu22.04-zen2
                ^diffutils@3.8%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
                ^libsigsegv@2.13%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^util-macros@1.19.3%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
    ^libxml2@2.10.3%gcc@11.3.0~python build_system=autotools arch=linux-ubuntu22.04-zen2
        ^libiconv@1.17%gcc@11.3.0 build_system=autotools libs=shared,static arch=linux-ubuntu22.04-zen2
        ^xz@5.4.1%gcc@11.3.0~pic build_system=autotools libs=shared,static arch=linux-ubuntu22.04-zen2
        ^zlib@1.2.13%gcc@11.3.0+optimize+pic+shared build_system=makefile arch=linux-ubuntu22.04-zen2
    ^ncurses@6.4%gcc@11.3.0~symlinks+termlib abi=none build_system=autotools arch=linux-ubuntu22.04-zen2
    ^pkgconf@1.8.0%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2

Input spec
--------------------------------
time

Concretized
--------------------------------
time@1.9%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2

Input spec
--------------------------------
nextflow

Concretized
--------------------------------
nextflow@22.10.4%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-zen2
    ^openjdk@11.0.17_8%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-zen2

Input spec
--------------------------------
singularityce+suid

Concretized
--------------------------------
singularityce@3.10.3%gcc@11.3.0+network+suid build_system=makefile arch=linux-ubuntu22.04-zen2
    ^conmon@2.1.5%gcc@11.3.0 build_system=makefile arch=linux-ubuntu22.04-zen2
        ^glib@2.74.3%gcc@11.3.0~libmount build_system=generic tracing=none arch=linux-ubuntu22.04-zen2
            ^elfutils@0.188%gcc@11.3.0~bzip2~debuginfod+nls~xz~zstd build_system=autotools arch=linux-ubuntu22.04-zen2
            ^libffi@3.4.4%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
            ^libiconv@1.17%gcc@11.3.0 build_system=autotools libs=shared,static arch=linux-ubuntu22.04-zen2
            ^meson@1.0.0%gcc@11.3.0 build_system=python_pip patches=0f0b1bd arch=linux-ubuntu22.04-zen2
            ^ninja@1.11.1%gcc@11.3.0+re2c build_system=generic arch=linux-ubuntu22.04-zen2
                ^re2c@2.2%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-zen2
            ^pcre2@10.42%gcc@11.3.0~jit+multibyte build_system=autotools arch=linux-ubuntu22.04-zen2
            ^perl@5.34.0%gcc@11.3.0~cpanm+open+shared+threads build_system=generic arch=linux-ubuntu22.04-zen2
            ^python@3.10.8%gcc@11.3.0+bz2+crypt+ctypes+dbm~debug+libxml2+lzma~nis~optimizations+pic+pyexpat+pythoncmd+readline+shared+sqlite3+ssl~tkinter+uuid+zlib build_system=generic patches=0d98e93,7d40923,f2fd060 arch=linux-ubuntu22.04-zen2
                ^expat@2.5.0%gcc@11.3.0+libbsd build_system=autotools arch=linux-ubuntu22.04-zen2
                    ^libbsd@0.11.7%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
                        ^libmd@1.0.4%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
                ^gdbm@1.23%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
                ^sqlite@3.40.1%gcc@11.3.0+column_metadata+dynamic_extensions+fts~functions+rtree build_system=autotools arch=linux-ubuntu22.04-zen2
        ^go-md2man@2.0.2%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-zen2
    ^cryptsetup@2.3.5%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^autoconf@2.69%gcc@11.3.0 build_system=autotools patches=35c4492,7793209,a49dd5b arch=linux-ubuntu22.04-zen2
        ^automake@1.16.5%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^gettext@0.21.1%gcc@11.3.0+bzip2+curses+git~libunistring+libxml2+tar+xz build_system=autotools arch=linux-ubuntu22.04-zen2
            ^bzip2@1.0.8%gcc@11.3.0~debug~pic+shared build_system=generic arch=linux-ubuntu22.04-zen2
            ^libxml2@2.10.3%gcc@11.3.0~python build_system=autotools arch=linux-ubuntu22.04-zen2
            ^ncurses@6.4%gcc@11.3.0~symlinks+termlib abi=none build_system=autotools arch=linux-ubuntu22.04-zen2
            ^tar@1.34%gcc@11.3.0 build_system=autotools zip=pigz arch=linux-ubuntu22.04-zen2
                ^pigz@2.7%gcc@11.3.0 build_system=makefile arch=linux-ubuntu22.04-zen2
                ^zstd@1.5.2%gcc@11.3.0+programs build_system=makefile compression=none libs=shared,static arch=linux-ubuntu22.04-zen2
            ^xz@5.4.1%gcc@11.3.0~pic build_system=autotools libs=shared,static arch=linux-ubuntu22.04-zen2
        ^json-c@0.16%gcc@11.3.0~ipo build_system=cmake build_type=RelWithDebInfo arch=linux-ubuntu22.04-zen2
            ^cmake@3.22.1%gcc@11.3.0~doc+ncurses+ownlibs~qt build_system=generic build_type=Release arch=linux-ubuntu22.04-zen2
        ^libtool@2.4.7%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^lvm2@2.03.14%gcc@11.3.0+pkgconfig build_system=autotools arch=linux-ubuntu22.04-zen2
            ^libaio@0.3.110%gcc@11.3.0 build_system=makefile arch=linux-ubuntu22.04-zen2
        ^m4@1.4.19%gcc@11.3.0+sigsegv build_system=autotools patches=9dc5fbd,bfdffa7 arch=linux-ubuntu22.04-zen2
            ^diffutils@3.8%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
            ^libsigsegv@2.13%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^openssl@1.1.1s%gcc@11.3.0~docs~shared build_system=generic certs=mozilla arch=linux-ubuntu22.04-zen2
            ^ca-certificates-mozilla@2023-01-10%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-zen2
        ^popt@1.16%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^util-linux@2.38.1%gcc@11.3.0~bash build_system=autotools arch=linux-ubuntu22.04-zen2
            ^libxcrypt@4.4.33%gcc@11.3.0~obsolete_api build_system=autotools arch=linux-ubuntu22.04-zen2
    ^go@1.18.1%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-zen2
    ^libgpg-error@1.46%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^gawk@5.1.1%gcc@11.3.0~nls build_system=autotools arch=linux-ubuntu22.04-zen2
            ^gmp@6.2.1%gcc@11.3.0+cxx build_system=autotools libs=shared,static arch=linux-ubuntu22.04-zen2
            ^mpfr@4.1.0%gcc@11.3.0 build_system=autotools libs=shared,static arch=linux-ubuntu22.04-zen2
                ^autoconf-archive@2022.02.11%gcc@11.3.0 build_system=autotools patches=139214f arch=linux-ubuntu22.04-zen2
                ^texinfo@7.0%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
            ^readline@8.2%gcc@11.3.0 build_system=autotools patches=bbf97f1 arch=linux-ubuntu22.04-zen2
    ^libseccomp@2.5.4%gcc@11.3.0+python build_system=autotools arch=linux-ubuntu22.04-zen2
        ^gperf@3.1%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^py-cython@0.29.32%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
            ^py-pip@22.2.2%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-zen2
            ^py-setuptools@63.0.0%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-zen2
            ^py-wheel@0.37.1%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-zen2
    ^pkgconf@1.8.0%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
    ^shadow@4.8.1%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
    ^squashfs@4.5.1%gcc@11.3.0+gzip~lz4~lzo~xz~zstd build_system=makefile default_compression=gzip arch=linux-ubuntu22.04-zen2
        ^zlib@1.2.13%gcc@11.3.0+optimize+pic+shared build_system=makefile arch=linux-ubuntu22.04-zen2
    ^util-linux-uuid@2.38.1%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2

Input spec
--------------------------------
squashfuse

Concretized
--------------------------------
squashfuse@0.1.104%gcc@11.3.0+lz4+lzo~min_size+shared+static+xz+zlib+zstd build_system=autotools arch=linux-ubuntu22.04-zen2
    ^libfuse@3.11.0%gcc@11.3.0~strip~system_install~useroot+utils build_system=meson buildtype=debugoptimized default_library=shared patches=3ad6719,fa7a3a5 arch=linux-ubuntu22.04-zen2
        ^meson@1.0.0%gcc@11.3.0 build_system=python_pip patches=0f0b1bd arch=linux-ubuntu22.04-zen2
            ^py-pip@22.2.2%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-zen2
            ^py-setuptools@63.0.0%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-zen2
            ^py-wheel@0.37.1%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-zen2
            ^python@3.10.8%gcc@11.3.0+bz2+crypt+ctypes+dbm~debug+libxml2+lzma~nis~optimizations+pic+pyexpat+pythoncmd+readline+shared+sqlite3+ssl~tkinter+uuid+zlib build_system=generic patches=0d98e93,7d40923,f2fd060 arch=linux-ubuntu22.04-zen2
                ^bzip2@1.0.8%gcc@11.3.0~debug~pic+shared build_system=generic arch=linux-ubuntu22.04-zen2
                    ^diffutils@3.8%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
                ^expat@2.5.0%gcc@11.3.0+libbsd build_system=autotools arch=linux-ubuntu22.04-zen2
                    ^libbsd@0.11.7%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
                        ^libmd@1.0.4%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
                ^gdbm@1.23%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
                ^gettext@0.21.1%gcc@11.3.0+bzip2+curses+git~libunistring+libxml2+tar+xz build_system=autotools arch=linux-ubuntu22.04-zen2
                    ^libiconv@1.17%gcc@11.3.0 build_system=autotools libs=shared,static arch=linux-ubuntu22.04-zen2
                    ^libxml2@2.10.3%gcc@11.3.0~python build_system=autotools arch=linux-ubuntu22.04-zen2
                    ^tar@1.34%gcc@11.3.0 build_system=autotools zip=pigz arch=linux-ubuntu22.04-zen2
                        ^pigz@2.7%gcc@11.3.0 build_system=makefile arch=linux-ubuntu22.04-zen2
                ^libffi@3.4.4%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
                ^libxcrypt@4.4.33%gcc@11.3.0~obsolete_api build_system=autotools arch=linux-ubuntu22.04-zen2
                    ^perl@5.34.0%gcc@11.3.0~cpanm+open+shared+threads build_system=generic arch=linux-ubuntu22.04-zen2
                ^ncurses@6.4%gcc@11.3.0~symlinks+termlib abi=none build_system=autotools arch=linux-ubuntu22.04-zen2
                ^openssl@1.1.1s%gcc@11.3.0~docs~shared build_system=generic certs=mozilla arch=linux-ubuntu22.04-zen2
                    ^ca-certificates-mozilla@2023-01-10%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-zen2
                ^readline@8.2%gcc@11.3.0 build_system=autotools patches=bbf97f1 arch=linux-ubuntu22.04-zen2
                ^sqlite@3.40.1%gcc@11.3.0+column_metadata+dynamic_extensions+fts~functions+rtree build_system=autotools arch=linux-ubuntu22.04-zen2
                ^util-linux-uuid@2.38.1%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^ninja@1.11.1%gcc@11.3.0+re2c build_system=generic arch=linux-ubuntu22.04-zen2
            ^re2c@2.2%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-zen2
    ^lz4@1.9.4%gcc@11.3.0 build_system=makefile libs=shared,static arch=linux-ubuntu22.04-zen2
    ^lzo@2.10%gcc@11.3.0 build_system=autotools libs=shared,static arch=linux-ubuntu22.04-zen2
    ^pkgconf@1.8.0%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
    ^xz@5.4.1%gcc@11.3.0~pic build_system=autotools libs=shared,static arch=linux-ubuntu22.04-zen2
    ^zlib@1.2.13%gcc@11.3.0+optimize+pic+shared build_system=makefile arch=linux-ubuntu22.04-zen2
    ^zstd@1.5.2%gcc@11.3.0+programs build_system=makefile compression=none libs=shared,static arch=linux-ubuntu22.04-zen2

Input spec
--------------------------------
e2fsprogs

Concretized
--------------------------------
e2fsprogs@1.45.6%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
    ^texinfo@7.0%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^gettext@0.21.1%gcc@11.3.0+bzip2+curses+git~libunistring+libxml2+tar+xz build_system=autotools arch=linux-ubuntu22.04-zen2
            ^bzip2@1.0.8%gcc@11.3.0~debug~pic+shared build_system=generic arch=linux-ubuntu22.04-zen2
                ^diffutils@3.8%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
            ^libiconv@1.17%gcc@11.3.0 build_system=autotools libs=shared,static arch=linux-ubuntu22.04-zen2
            ^libxml2@2.10.3%gcc@11.3.0~python build_system=autotools arch=linux-ubuntu22.04-zen2
                ^zlib@1.2.13%gcc@11.3.0+optimize+pic+shared build_system=makefile arch=linux-ubuntu22.04-zen2
            ^tar@1.34%gcc@11.3.0 build_system=autotools zip=pigz arch=linux-ubuntu22.04-zen2
                ^pigz@2.7%gcc@11.3.0 build_system=makefile arch=linux-ubuntu22.04-zen2
                ^zstd@1.5.2%gcc@11.3.0+programs build_system=makefile compression=none libs=shared,static arch=linux-ubuntu22.04-zen2
            ^xz@5.4.1%gcc@11.3.0~pic build_system=autotools libs=shared,static arch=linux-ubuntu22.04-zen2
        ^ncurses@6.4%gcc@11.3.0~symlinks+termlib abi=none build_system=autotools arch=linux-ubuntu22.04-zen2
            ^pkgconf@1.8.0%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^perl@5.34.0%gcc@11.3.0~cpanm+open+shared+threads build_system=generic arch=linux-ubuntu22.04-zen2

Input spec
--------------------------------
snakemake@7.18.2+ftp+http+reports+s3

Concretized
--------------------------------
snakemake@7.18.2%gcc@11.3.0+ftp~google-cloud+http+reports+s3 build_system=python_pip arch=linux-ubuntu22.04-zen2
    ^py-appdirs@1.4.4%gcc@11.3.0 build_system=python_pip patches=006d203 arch=linux-ubuntu22.04-zen2
    ^py-boto3@1.26.26%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
        ^py-jmespath@1.0.1%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
        ^py-s3transfer@0.6.0%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
    ^py-botocore@1.29.56%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
        ^py-python-dateutil@2.8.2%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
            ^py-setuptools-scm@7.0.5%gcc@11.3.0+toml build_system=python_pip arch=linux-ubuntu22.04-zen2
                ^py-typing-extensions@4.3.0%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
            ^py-six@1.16.0%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
        ^py-urllib3@1.26.12%gcc@11.3.0~brotli~secure~socks build_system=python_pip arch=linux-ubuntu22.04-zen2
    ^py-configargparse@1.2.3%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
    ^py-connectionpool@0.0.3%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
    ^py-datrie@0.8.2%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
        ^py-cython@0.29.32%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
        ^py-pytest-runner@6.0.0%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
    ^py-docutils@0.19%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
    ^py-ftputil@5.0.4%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
    ^py-gitpython@3.1.27%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
        ^py-gitdb@4.0.9%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
            ^py-smmap@5.0.0%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
    ^py-jinja2@3.1.2%gcc@11.3.0~i18n build_system=python_pip arch=linux-ubuntu22.04-zen2
        ^py-markupsafe@2.1.1%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
    ^py-jsonschema@4.16.0%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
        ^py-attrs@22.1.0%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
        ^py-hatch-fancy-pypi-readme@22.7.0%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
            ^py-tomli@2.0.1%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
        ^py-hatch-vcs@0.2.0%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
        ^py-hatchling@1.10.0%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
            ^py-editables@0.3%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
            ^py-packaging@23.0%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
            ^py-pathspec@0.10.1%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
            ^py-pluggy@1.0.0%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
        ^py-pyrsistent@0.18.1%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
    ^py-nbformat@5.7.0%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
        ^py-fastjsonschema@2.16.2%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
        ^py-hatch-nodejs-version@0.3.1%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
        ^py-jupyter-core@5.1.0%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
            ^py-platformdirs@2.5.2%gcc@11.3.0~wheel build_system=python_pip arch=linux-ubuntu22.04-zen2
        ^py-traitlets@5.7.1%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
    ^py-networkx@2.8.6%gcc@11.3.0~extra build_system=python_pip arch=linux-ubuntu22.04-zen2
        ^py-matplotlib@3.6.3%gcc@11.3.0~animation~fonts~latex~movies backend=agg build_system=python_pip arch=linux-ubuntu22.04-zen2
            ^freetype@2.11.1%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
            ^libpng@1.6.37%gcc@11.3.0 build_system=autotools libs=shared,static arch=linux-ubuntu22.04-zen2
            ^py-contourpy@1.0.5%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
            ^py-cycler@0.11.0%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
            ^py-fonttools@4.37.3%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
            ^py-kiwisolver@1.4.4%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
                ^py-cppy@1.2.1%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
            ^py-pillow@9.2.0%gcc@11.3.0~freetype~imagequant+jpeg~jpeg2000~lcms~raqm~tiff~webp~xcb+zlib build_system=python_pip arch=linux-ubuntu22.04-zen2
                ^libjpeg-turbo@2.1.4%gcc@11.3.0~ipo~jpeg8+shared+static build_system=cmake build_type=RelWithDebInfo arch=linux-ubuntu22.04-zen2
                    ^nasm@2.15.05%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
            ^py-pyparsing@3.0.9%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
            ^qhull@2020.2%gcc@11.3.0~ipo build_system=cmake build_type=RelWithDebInfo arch=linux-ubuntu22.04-zen2
                ^cmake@3.22.1%gcc@11.3.0~doc+ncurses+ownlibs~qt build_system=generic build_type=Release arch=linux-ubuntu22.04-zen2
        ^py-numpy@1.24.2%gcc@11.3.0+blas+lapack build_system=python_pip patches=873745d arch=linux-ubuntu22.04-zen2
            ^openblas@0.3.21%gcc@11.3.0~bignuma~consistent_fpcsr+fortran~ilp64+locking+pic+shared build_system=makefile patches=d3d9b15 symbol_suffix=none threads=none arch=linux-ubuntu22.04-zen2
        ^py-pandas@1.5.3%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
            ^py-bottleneck@1.3.5%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
                ^py-versioneer@0.26%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
            ^py-numexpr@2.8.3%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
            ^py-pytz@2022.2.1%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
        ^py-scipy@1.10.0%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
            ^py-build@0.7.0%gcc@11.3.0~virtualenv build_system=python_pip patches=9a151ac arch=linux-ubuntu22.04-zen2
                ^py-pep517@0.12.0%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
            ^py-meson-python@0.11.0%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
                ^meson@1.0.0%gcc@11.3.0 build_system=python_pip patches=0f0b1bd arch=linux-ubuntu22.04-zen2
                ^py-pyproject-metadata@0.6.1%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
            ^py-pybind11@2.10.1%gcc@11.3.0~ipo build_system=cmake build_type=RelWithDebInfo arch=linux-ubuntu22.04-zen2
                ^ninja@1.11.1%gcc@11.3.0+re2c build_system=generic arch=linux-ubuntu22.04-zen2
                    ^re2c@2.2%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-zen2
            ^py-pythran@0.12.0%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
                ^py-beniget@0.4.1%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
                ^py-gast@0.5.3%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
                ^py-ply@3.11%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
    ^py-pip@22.2.2%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-zen2
    ^py-psutil@5.9.2%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
    ^py-pulp@2.6.0%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
    ^py-pygments@2.13.0%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
    ^py-pygraphviz@1.10%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
        ^graphviz@2.49.0%gcc@11.3.0~doc~expat~ghostscript~gtkplus~gts~java~libgd~pangocairo~poppler~qt~quartz~x build_system=autotools arch=linux-ubuntu22.04-zen2
            ^autoconf@2.69%gcc@11.3.0 build_system=autotools patches=35c4492,7793209,a49dd5b arch=linux-ubuntu22.04-zen2
                ^m4@1.4.19%gcc@11.3.0+sigsegv build_system=autotools patches=9dc5fbd,bfdffa7 arch=linux-ubuntu22.04-zen2
                    ^libsigsegv@2.13%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
            ^automake@1.16.5%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
            ^bison@3.8.2%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
            ^flex@2.6.3%gcc@11.3.0+lex~nls build_system=autotools arch=linux-ubuntu22.04-zen2
                ^findutils@4.9.0%gcc@11.3.0 build_system=autotools patches=440b954 arch=linux-ubuntu22.04-zen2
            ^libtool@2.4.7%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
            ^sed@4.8%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
    ^py-pyyaml@6.0%gcc@11.3.0+libyaml build_system=python_pip arch=linux-ubuntu22.04-zen2
        ^libyaml@0.2.5%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
    ^py-requests@2.28.1%gcc@11.3.0~socks build_system=python_pip arch=linux-ubuntu22.04-zen2
        ^py-certifi@2022.9.14%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
        ^py-charset-normalizer@2.0.12%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
        ^py-idna@3.4%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
            ^py-flit-core@3.7.1%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
    ^py-reretry@0.11.1%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
        ^py-pbr@5.10.0%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
    ^py-setuptools@63.0.0%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-zen2
    ^py-smart-open@5.2.1%gcc@11.3.0~azure~gcs+http~s3 build_system=python_pip arch=linux-ubuntu22.04-zen2
    ^py-stopit@1.1.2%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
    ^py-tabulate@0.8.9%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
    ^py-throttler@1.2.2%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
    ^py-toposort@1.6%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
    ^py-wheel@0.37.1%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-zen2
    ^py-wrapt@1.14.1%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
    ^py-yte@1.5.1%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
        ^py-dpath@2.0.1%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
        ^py-plac@1.3.5%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
        ^py-poetry-core@1.2.0%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
    ^python@3.10.8%gcc@11.3.0+bz2+crypt+ctypes+dbm~debug+libxml2+lzma~nis~optimizations+pic+pyexpat+pythoncmd+readline+shared+sqlite3+ssl~tkinter+uuid+zlib build_system=generic patches=0d98e93,7d40923,f2fd060 arch=linux-ubuntu22.04-zen2
        ^bzip2@1.0.8%gcc@11.3.0~debug~pic+shared build_system=generic arch=linux-ubuntu22.04-zen2
            ^diffutils@3.8%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^expat@2.5.0%gcc@11.3.0+libbsd build_system=autotools arch=linux-ubuntu22.04-zen2
            ^libbsd@0.11.7%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
                ^libmd@1.0.4%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^gdbm@1.23%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^gettext@0.21.1%gcc@11.3.0+bzip2+curses+git~libunistring+libxml2+tar+xz build_system=autotools arch=linux-ubuntu22.04-zen2
            ^libiconv@1.17%gcc@11.3.0 build_system=autotools libs=shared,static arch=linux-ubuntu22.04-zen2
            ^libxml2@2.10.3%gcc@11.3.0~python build_system=autotools arch=linux-ubuntu22.04-zen2
            ^tar@1.34%gcc@11.3.0 build_system=autotools zip=pigz arch=linux-ubuntu22.04-zen2
                ^pigz@2.7%gcc@11.3.0 build_system=makefile arch=linux-ubuntu22.04-zen2
                ^zstd@1.5.2%gcc@11.3.0+programs build_system=makefile compression=none libs=shared,static arch=linux-ubuntu22.04-zen2
        ^libffi@3.4.4%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^libxcrypt@4.4.33%gcc@11.3.0~obsolete_api build_system=autotools arch=linux-ubuntu22.04-zen2
            ^perl@5.34.0%gcc@11.3.0~cpanm+open+shared+threads build_system=generic arch=linux-ubuntu22.04-zen2
        ^ncurses@6.4%gcc@11.3.0~symlinks+termlib abi=none build_system=autotools arch=linux-ubuntu22.04-zen2
        ^openssl@1.1.1s%gcc@11.3.0~docs~shared build_system=generic certs=mozilla arch=linux-ubuntu22.04-zen2
            ^ca-certificates-mozilla@2023-01-10%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-zen2
        ^pkgconf@1.8.0%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^readline@8.2%gcc@11.3.0 build_system=autotools patches=bbf97f1 arch=linux-ubuntu22.04-zen2
        ^sqlite@3.40.1%gcc@11.3.0+column_metadata+dynamic_extensions+fts~functions+rtree build_system=autotools arch=linux-ubuntu22.04-zen2
        ^util-linux-uuid@2.38.1%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^xz@5.4.1%gcc@11.3.0~pic build_system=autotools libs=shared,static arch=linux-ubuntu22.04-zen2
        ^zlib@1.2.13%gcc@11.3.0+optimize+pic+shared build_system=makefile arch=linux-ubuntu22.04-zen2

Input spec
--------------------------------
py-pandas

Concretized
--------------------------------
py-pandas@1.5.3%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
    ^py-bottleneck@1.3.5%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
        ^py-versioneer@0.26%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
    ^py-cython@0.29.32%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
    ^py-numexpr@2.8.3%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
        ^py-packaging@23.0%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
            ^py-flit-core@3.7.1%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
    ^py-numpy@1.24.2%gcc@11.3.0+blas+lapack build_system=python_pip patches=873745d arch=linux-ubuntu22.04-zen2
        ^openblas@0.3.21%gcc@11.3.0~bignuma~consistent_fpcsr+fortran~ilp64+locking+pic+shared build_system=makefile patches=d3d9b15 symbol_suffix=none threads=none arch=linux-ubuntu22.04-zen2
            ^perl@5.34.0%gcc@11.3.0~cpanm+open+shared+threads build_system=generic arch=linux-ubuntu22.04-zen2
    ^py-pip@22.2.2%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-zen2
    ^py-python-dateutil@2.8.2%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
        ^py-setuptools-scm@7.0.5%gcc@11.3.0+toml build_system=python_pip arch=linux-ubuntu22.04-zen2
            ^py-tomli@2.0.1%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
            ^py-typing-extensions@4.3.0%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
        ^py-six@1.16.0%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
    ^py-pytz@2022.2.1%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
    ^py-setuptools@63.0.0%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-zen2
    ^py-wheel@0.37.1%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-zen2
    ^python@3.10.8%gcc@11.3.0+bz2+crypt+ctypes+dbm~debug+libxml2+lzma~nis~optimizations+pic+pyexpat+pythoncmd+readline+shared+sqlite3+ssl~tkinter+uuid+zlib build_system=generic patches=0d98e93,7d40923,f2fd060 arch=linux-ubuntu22.04-zen2
        ^bzip2@1.0.8%gcc@11.3.0~debug~pic+shared build_system=generic arch=linux-ubuntu22.04-zen2
            ^diffutils@3.8%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^expat@2.5.0%gcc@11.3.0+libbsd build_system=autotools arch=linux-ubuntu22.04-zen2
            ^libbsd@0.11.7%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
                ^libmd@1.0.4%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^gdbm@1.23%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^gettext@0.21.1%gcc@11.3.0+bzip2+curses+git~libunistring+libxml2+tar+xz build_system=autotools arch=linux-ubuntu22.04-zen2
            ^libiconv@1.17%gcc@11.3.0 build_system=autotools libs=shared,static arch=linux-ubuntu22.04-zen2
            ^libxml2@2.10.3%gcc@11.3.0~python build_system=autotools arch=linux-ubuntu22.04-zen2
            ^tar@1.34%gcc@11.3.0 build_system=autotools zip=pigz arch=linux-ubuntu22.04-zen2
                ^pigz@2.7%gcc@11.3.0 build_system=makefile arch=linux-ubuntu22.04-zen2
                ^zstd@1.5.2%gcc@11.3.0+programs build_system=makefile compression=none libs=shared,static arch=linux-ubuntu22.04-zen2
        ^libffi@3.4.4%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^libxcrypt@4.4.33%gcc@11.3.0~obsolete_api build_system=autotools arch=linux-ubuntu22.04-zen2
        ^ncurses@6.4%gcc@11.3.0~symlinks+termlib abi=none build_system=autotools arch=linux-ubuntu22.04-zen2
        ^openssl@1.1.1s%gcc@11.3.0~docs~shared build_system=generic certs=mozilla arch=linux-ubuntu22.04-zen2
            ^ca-certificates-mozilla@2023-01-10%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-zen2
        ^pkgconf@1.8.0%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^readline@8.2%gcc@11.3.0 build_system=autotools patches=bbf97f1 arch=linux-ubuntu22.04-zen2
        ^sqlite@3.40.1%gcc@11.3.0+column_metadata+dynamic_extensions+fts~functions+rtree build_system=autotools arch=linux-ubuntu22.04-zen2
        ^util-linux-uuid@2.38.1%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^xz@5.4.1%gcc@11.3.0~pic build_system=autotools libs=shared,static arch=linux-ubuntu22.04-zen2
        ^zlib@1.2.13%gcc@11.3.0+optimize+pic+shared build_system=makefile arch=linux-ubuntu22.04-zen2

Input spec
--------------------------------
py-peppy

Concretized
--------------------------------
py-peppy@0.35.4%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
    ^py-attmap@0.13.2%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
    ^py-logmuse@0.2.7%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
    ^py-pandas@1.5.3%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
        ^py-bottleneck@1.3.5%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
            ^py-versioneer@0.26%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
        ^py-cython@0.29.32%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
        ^py-numexpr@2.8.3%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
            ^py-packaging@23.0%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
                ^py-flit-core@3.7.1%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
        ^py-numpy@1.24.2%gcc@11.3.0+blas+lapack build_system=python_pip patches=873745d arch=linux-ubuntu22.04-zen2
            ^openblas@0.3.21%gcc@11.3.0~bignuma~consistent_fpcsr+fortran~ilp64+locking+pic+shared build_system=makefile patches=d3d9b15 symbol_suffix=none threads=none arch=linux-ubuntu22.04-zen2
        ^py-python-dateutil@2.8.2%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
            ^py-setuptools-scm@7.0.5%gcc@11.3.0+toml build_system=python_pip arch=linux-ubuntu22.04-zen2
                ^py-tomli@2.0.1%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
                ^py-typing-extensions@4.3.0%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
            ^py-six@1.16.0%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
        ^py-pytz@2022.2.1%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
    ^py-pip@22.2.2%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-zen2
    ^py-pyyaml@6.0%gcc@11.3.0+libyaml build_system=python_pip arch=linux-ubuntu22.04-zen2
        ^libyaml@0.2.5%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
    ^py-rich@12.5.1%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
        ^py-commonmark@0.9.1%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
        ^py-poetry-core@1.2.0%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
        ^py-pygments@2.13.0%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
    ^py-setuptools@63.0.0%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-zen2
    ^py-ubiquerg@0.6.2%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
    ^py-wheel@0.37.1%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-zen2
    ^python@3.10.8%gcc@11.3.0+bz2+crypt+ctypes+dbm~debug+libxml2+lzma~nis~optimizations+pic+pyexpat+pythoncmd+readline+shared+sqlite3+ssl~tkinter+uuid+zlib build_system=generic patches=0d98e93,7d40923,f2fd060 arch=linux-ubuntu22.04-zen2
        ^bzip2@1.0.8%gcc@11.3.0~debug~pic+shared build_system=generic arch=linux-ubuntu22.04-zen2
            ^diffutils@3.8%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^expat@2.5.0%gcc@11.3.0+libbsd build_system=autotools arch=linux-ubuntu22.04-zen2
            ^libbsd@0.11.7%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
                ^libmd@1.0.4%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^gdbm@1.23%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^gettext@0.21.1%gcc@11.3.0+bzip2+curses+git~libunistring+libxml2+tar+xz build_system=autotools arch=linux-ubuntu22.04-zen2
            ^libiconv@1.17%gcc@11.3.0 build_system=autotools libs=shared,static arch=linux-ubuntu22.04-zen2
            ^libxml2@2.10.3%gcc@11.3.0~python build_system=autotools arch=linux-ubuntu22.04-zen2
            ^tar@1.34%gcc@11.3.0 build_system=autotools zip=pigz arch=linux-ubuntu22.04-zen2
                ^pigz@2.7%gcc@11.3.0 build_system=makefile arch=linux-ubuntu22.04-zen2
                ^zstd@1.5.2%gcc@11.3.0+programs build_system=makefile compression=none libs=shared,static arch=linux-ubuntu22.04-zen2
        ^libffi@3.4.4%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^libxcrypt@4.4.33%gcc@11.3.0~obsolete_api build_system=autotools arch=linux-ubuntu22.04-zen2
            ^perl@5.34.0%gcc@11.3.0~cpanm+open+shared+threads build_system=generic arch=linux-ubuntu22.04-zen2
        ^ncurses@6.4%gcc@11.3.0~symlinks+termlib abi=none build_system=autotools arch=linux-ubuntu22.04-zen2
        ^openssl@1.1.1s%gcc@11.3.0~docs~shared build_system=generic certs=mozilla arch=linux-ubuntu22.04-zen2
            ^ca-certificates-mozilla@2023-01-10%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-zen2
        ^pkgconf@1.8.0%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^readline@8.2%gcc@11.3.0 build_system=autotools patches=bbf97f1 arch=linux-ubuntu22.04-zen2
        ^sqlite@3.40.1%gcc@11.3.0+column_metadata+dynamic_extensions+fts~functions+rtree build_system=autotools arch=linux-ubuntu22.04-zen2
        ^util-linux-uuid@2.38.1%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^xz@5.4.1%gcc@11.3.0~pic build_system=autotools libs=shared,static arch=linux-ubuntu22.04-zen2
        ^zlib@1.2.13%gcc@11.3.0+optimize+pic+shared build_system=makefile arch=linux-ubuntu22.04-zen2

Input spec
--------------------------------
miniconda3

Concretized
--------------------------------
miniconda3@22.11.1%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-zen2

Input spec
--------------------------------
py-pyopenssl

Concretized
--------------------------------
py-pyopenssl@22.1.0%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
    ^py-cryptography@38.0.1%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
        ^git@2.39.1%gcc@11.3.0+man+nls+perl+subtree~svn~tcltk build_system=autotools arch=linux-ubuntu22.04-zen2
            ^autoconf@2.69%gcc@11.3.0 build_system=autotools patches=35c4492,7793209,a49dd5b arch=linux-ubuntu22.04-zen2
            ^automake@1.16.5%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
            ^curl@7.87.0%gcc@11.3.0~gssapi~ldap~libidn2~librtmp~libssh~libssh2~nghttp2 build_system=autotools libs=shared,static tls=openssl arch=linux-ubuntu22.04-zen2
            ^libiconv@1.17%gcc@11.3.0 build_system=autotools libs=shared,static arch=linux-ubuntu22.04-zen2
            ^libidn2@2.3.4%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
                ^libunistring@1.1%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
            ^libtool@2.4.7%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
            ^m4@1.4.19%gcc@11.3.0+sigsegv build_system=autotools patches=9dc5fbd,bfdffa7 arch=linux-ubuntu22.04-zen2
                ^libsigsegv@2.13%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
            ^openssh@9.1p1%gcc@11.3.0+gssapi build_system=autotools arch=linux-ubuntu22.04-zen2
                ^krb5@1.20.1%gcc@11.3.0+shared build_system=autotools arch=linux-ubuntu22.04-zen2
                    ^bison@3.8.2%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
                ^libedit@3.1-20210216%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
            ^pcre2@10.42%gcc@11.3.0~jit+multibyte build_system=autotools arch=linux-ubuntu22.04-zen2
            ^perl@5.34.0%gcc@11.3.0~cpanm+open+shared+threads build_system=generic arch=linux-ubuntu22.04-zen2
        ^openssl@1.1.1s%gcc@11.3.0~docs~shared build_system=generic certs=mozilla arch=linux-ubuntu22.04-zen2
            ^ca-certificates-mozilla@2023-01-10%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-zen2
        ^py-cffi@1.15.1%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
            ^py-pycparser@2.21%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
        ^py-setuptools-rust@1.5.1%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
            ^py-semantic-version@2.10.0%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
            ^py-typing-extensions@4.3.0%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
                ^py-flit-core@3.7.1%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
        ^rust@1.61.0%gcc@11.3.0+analysis+clippy~rls+rustfmt+src build_system=generic extra_targets=none arch=linux-ubuntu22.04-zen2
    ^py-pip@22.2.2%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-zen2
    ^py-setuptools@63.0.0%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-zen2
    ^py-wheel@0.37.1%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-zen2
    ^python@3.10.8%gcc@11.3.0+bz2+crypt+ctypes+dbm~debug+libxml2+lzma~nis~optimizations+pic+pyexpat+pythoncmd+readline+shared+sqlite3+ssl~tkinter+uuid+zlib build_system=generic patches=0d98e93,7d40923,f2fd060 arch=linux-ubuntu22.04-zen2
        ^bzip2@1.0.8%gcc@11.3.0~debug~pic+shared build_system=generic arch=linux-ubuntu22.04-zen2
            ^diffutils@3.8%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^expat@2.5.0%gcc@11.3.0+libbsd build_system=autotools arch=linux-ubuntu22.04-zen2
            ^libbsd@0.11.7%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
                ^libmd@1.0.4%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^gdbm@1.23%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^gettext@0.21.1%gcc@11.3.0+bzip2+curses+git~libunistring+libxml2+tar+xz build_system=autotools arch=linux-ubuntu22.04-zen2
            ^libxml2@2.10.3%gcc@11.3.0~python build_system=autotools arch=linux-ubuntu22.04-zen2
            ^tar@1.34%gcc@11.3.0 build_system=autotools zip=pigz arch=linux-ubuntu22.04-zen2
                ^pigz@2.7%gcc@11.3.0 build_system=makefile arch=linux-ubuntu22.04-zen2
                ^zstd@1.5.2%gcc@11.3.0+programs build_system=makefile compression=none libs=shared,static arch=linux-ubuntu22.04-zen2
        ^libffi@3.4.4%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^libxcrypt@4.4.33%gcc@11.3.0~obsolete_api build_system=autotools arch=linux-ubuntu22.04-zen2
        ^ncurses@6.4%gcc@11.3.0~symlinks+termlib abi=none build_system=autotools arch=linux-ubuntu22.04-zen2
        ^pkgconf@1.8.0%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^readline@8.2%gcc@11.3.0 build_system=autotools patches=bbf97f1 arch=linux-ubuntu22.04-zen2
        ^sqlite@3.40.1%gcc@11.3.0+column_metadata+dynamic_extensions+fts~functions+rtree build_system=autotools arch=linux-ubuntu22.04-zen2
        ^util-linux-uuid@2.38.1%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^xz@5.4.1%gcc@11.3.0~pic build_system=autotools libs=shared,static arch=linux-ubuntu22.04-zen2
        ^zlib@1.2.13%gcc@11.3.0+optimize+pic+shared build_system=makefile arch=linux-ubuntu22.04-zen2

Input spec
--------------------------------
python@3.10

Concretized
--------------------------------
python@3.10.8%gcc@11.3.0+bz2+crypt+ctypes+dbm~debug+libxml2+lzma~nis~optimizations+pic+pyexpat+pythoncmd+readline+shared+sqlite3+ssl~tkinter+uuid+zlib build_system=generic patches=0d98e93,7d40923,f2fd060 arch=linux-ubuntu22.04-zen2
    ^bzip2@1.0.8%gcc@11.3.0~debug~pic+shared build_system=generic arch=linux-ubuntu22.04-zen2
        ^diffutils@3.8%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
    ^expat@2.5.0%gcc@11.3.0+libbsd build_system=autotools arch=linux-ubuntu22.04-zen2
        ^libbsd@0.11.7%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
            ^libmd@1.0.4%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
    ^gdbm@1.23%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
    ^gettext@0.21.1%gcc@11.3.0+bzip2+curses+git~libunistring+libxml2+tar+xz build_system=autotools arch=linux-ubuntu22.04-zen2
        ^libiconv@1.17%gcc@11.3.0 build_system=autotools libs=shared,static arch=linux-ubuntu22.04-zen2
        ^libxml2@2.10.3%gcc@11.3.0~python build_system=autotools arch=linux-ubuntu22.04-zen2
        ^tar@1.34%gcc@11.3.0 build_system=autotools zip=pigz arch=linux-ubuntu22.04-zen2
            ^pigz@2.7%gcc@11.3.0 build_system=makefile arch=linux-ubuntu22.04-zen2
            ^zstd@1.5.2%gcc@11.3.0+programs build_system=makefile compression=none libs=shared,static arch=linux-ubuntu22.04-zen2
    ^libffi@3.4.4%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
    ^libxcrypt@4.4.33%gcc@11.3.0~obsolete_api build_system=autotools arch=linux-ubuntu22.04-zen2
        ^perl@5.34.0%gcc@11.3.0~cpanm+open+shared+threads build_system=generic arch=linux-ubuntu22.04-zen2
    ^ncurses@6.4%gcc@11.3.0~symlinks+termlib abi=none build_system=autotools arch=linux-ubuntu22.04-zen2
    ^openssl@1.1.1s%gcc@11.3.0~docs~shared build_system=generic certs=mozilla arch=linux-ubuntu22.04-zen2
        ^ca-certificates-mozilla@2023-01-10%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-zen2
    ^pkgconf@1.8.0%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
    ^readline@8.2%gcc@11.3.0 build_system=autotools patches=bbf97f1 arch=linux-ubuntu22.04-zen2
    ^sqlite@3.40.1%gcc@11.3.0+column_metadata+dynamic_extensions+fts~functions+rtree build_system=autotools arch=linux-ubuntu22.04-zen2
    ^util-linux-uuid@2.38.1%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
    ^xz@5.4.1%gcc@11.3.0~pic build_system=autotools libs=shared,static arch=linux-ubuntu22.04-zen2
    ^zlib@1.2.13%gcc@11.3.0+optimize+pic+shared build_system=makefile arch=linux-ubuntu22.04-zen2

Input spec
--------------------------------
py-pygithub@1

Concretized
--------------------------------
py-pygithub@1.55%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
    ^py-deprecated@1.2.13%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
        ^py-wrapt@1.14.1%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
    ^py-pip@22.2.2%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-zen2
    ^py-pyjwt@2.4.0%gcc@11.3.0+crypto build_system=python_pip arch=linux-ubuntu22.04-zen2
        ^py-cryptography@38.0.1%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
            ^git@2.39.1%gcc@11.3.0+man+nls+perl+subtree~svn~tcltk build_system=autotools arch=linux-ubuntu22.04-zen2
                ^autoconf@2.69%gcc@11.3.0 build_system=autotools patches=35c4492,7793209,a49dd5b arch=linux-ubuntu22.04-zen2
                ^automake@1.16.5%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
                ^curl@7.87.0%gcc@11.3.0~gssapi~ldap~libidn2~librtmp~libssh~libssh2~nghttp2 build_system=autotools libs=shared,static tls=openssl arch=linux-ubuntu22.04-zen2
                ^libidn2@2.3.4%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
                    ^libunistring@1.1%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
                ^libtool@2.4.7%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
                ^m4@1.4.19%gcc@11.3.0+sigsegv build_system=autotools patches=9dc5fbd,bfdffa7 arch=linux-ubuntu22.04-zen2
                    ^libsigsegv@2.13%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
                ^openssh@9.1p1%gcc@11.3.0+gssapi build_system=autotools arch=linux-ubuntu22.04-zen2
                    ^krb5@1.20.1%gcc@11.3.0+shared build_system=autotools arch=linux-ubuntu22.04-zen2
                        ^bison@3.8.2%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
                    ^libedit@3.1-20210216%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
                ^pcre2@10.42%gcc@11.3.0~jit+multibyte build_system=autotools arch=linux-ubuntu22.04-zen2
            ^py-setuptools-rust@1.5.1%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
                ^py-semantic-version@2.10.0%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
                ^py-typing-extensions@4.3.0%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
            ^rust@1.61.0%gcc@11.3.0+analysis+clippy~rls+rustfmt+src build_system=generic extra_targets=none arch=linux-ubuntu22.04-zen2
    ^py-pynacl@1.5.0%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
        ^py-cffi@1.15.1%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
            ^py-pycparser@2.21%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
    ^py-requests@2.28.1%gcc@11.3.0~socks build_system=python_pip arch=linux-ubuntu22.04-zen2
        ^py-certifi@2022.9.14%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
        ^py-charset-normalizer@2.0.12%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
        ^py-idna@3.4%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
            ^py-flit-core@3.7.1%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
        ^py-urllib3@1.26.12%gcc@11.3.0~brotli~secure~socks build_system=python_pip arch=linux-ubuntu22.04-zen2
    ^py-setuptools@63.0.0%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-zen2
    ^py-wheel@0.37.1%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-zen2
    ^python@3.10.8%gcc@11.3.0+bz2+crypt+ctypes+dbm~debug+libxml2+lzma~nis~optimizations+pic+pyexpat+pythoncmd+readline+shared+sqlite3+ssl~tkinter+uuid+zlib build_system=generic patches=0d98e93,7d40923,f2fd060 arch=linux-ubuntu22.04-zen2
        ^bzip2@1.0.8%gcc@11.3.0~debug~pic+shared build_system=generic arch=linux-ubuntu22.04-zen2
            ^diffutils@3.8%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^expat@2.5.0%gcc@11.3.0+libbsd build_system=autotools arch=linux-ubuntu22.04-zen2
            ^libbsd@0.11.7%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
                ^libmd@1.0.4%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^gdbm@1.23%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^gettext@0.21.1%gcc@11.3.0+bzip2+curses+git~libunistring+libxml2+tar+xz build_system=autotools arch=linux-ubuntu22.04-zen2
            ^libiconv@1.17%gcc@11.3.0 build_system=autotools libs=shared,static arch=linux-ubuntu22.04-zen2
            ^libxml2@2.10.3%gcc@11.3.0~python build_system=autotools arch=linux-ubuntu22.04-zen2
            ^tar@1.34%gcc@11.3.0 build_system=autotools zip=pigz arch=linux-ubuntu22.04-zen2
                ^pigz@2.7%gcc@11.3.0 build_system=makefile arch=linux-ubuntu22.04-zen2
                ^zstd@1.5.2%gcc@11.3.0+programs build_system=makefile compression=none libs=shared,static arch=linux-ubuntu22.04-zen2
        ^libffi@3.4.4%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^libxcrypt@4.4.33%gcc@11.3.0~obsolete_api build_system=autotools arch=linux-ubuntu22.04-zen2
            ^perl@5.34.0%gcc@11.3.0~cpanm+open+shared+threads build_system=generic arch=linux-ubuntu22.04-zen2
        ^ncurses@6.4%gcc@11.3.0~symlinks+termlib abi=none build_system=autotools arch=linux-ubuntu22.04-zen2
        ^openssl@1.1.1s%gcc@11.3.0~docs~shared build_system=generic certs=mozilla arch=linux-ubuntu22.04-zen2
            ^ca-certificates-mozilla@2023-01-10%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-zen2
        ^pkgconf@1.8.0%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^readline@8.2%gcc@11.3.0 build_system=autotools patches=bbf97f1 arch=linux-ubuntu22.04-zen2
        ^sqlite@3.40.1%gcc@11.3.0+column_metadata+dynamic_extensions+fts~functions+rtree build_system=autotools arch=linux-ubuntu22.04-zen2
        ^util-linux-uuid@2.38.1%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^xz@5.4.1%gcc@11.3.0~pic build_system=autotools libs=shared,static arch=linux-ubuntu22.04-zen2
        ^zlib@1.2.13%gcc@11.3.0+optimize+pic+shared build_system=makefile arch=linux-ubuntu22.04-zen2

Input spec
--------------------------------
py-gitpython@3

Concretized
--------------------------------
py-gitpython@3.1.27%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
    ^py-gitdb@4.0.9%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
        ^py-smmap@5.0.0%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
    ^py-pip@22.2.2%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-zen2
    ^py-setuptools@63.0.0%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-zen2
    ^py-wheel@0.37.1%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-zen2
    ^python@3.10.8%gcc@11.3.0+bz2+crypt+ctypes+dbm~debug+libxml2+lzma~nis~optimizations+pic+pyexpat+pythoncmd+readline+shared+sqlite3+ssl~tkinter+uuid+zlib build_system=generic patches=0d98e93,7d40923,f2fd060 arch=linux-ubuntu22.04-zen2
        ^bzip2@1.0.8%gcc@11.3.0~debug~pic+shared build_system=generic arch=linux-ubuntu22.04-zen2
            ^diffutils@3.8%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^expat@2.5.0%gcc@11.3.0+libbsd build_system=autotools arch=linux-ubuntu22.04-zen2
            ^libbsd@0.11.7%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
                ^libmd@1.0.4%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^gdbm@1.23%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^gettext@0.21.1%gcc@11.3.0+bzip2+curses+git~libunistring+libxml2+tar+xz build_system=autotools arch=linux-ubuntu22.04-zen2
            ^libiconv@1.17%gcc@11.3.0 build_system=autotools libs=shared,static arch=linux-ubuntu22.04-zen2
            ^libxml2@2.10.3%gcc@11.3.0~python build_system=autotools arch=linux-ubuntu22.04-zen2
            ^tar@1.34%gcc@11.3.0 build_system=autotools zip=pigz arch=linux-ubuntu22.04-zen2
                ^pigz@2.7%gcc@11.3.0 build_system=makefile arch=linux-ubuntu22.04-zen2
                ^zstd@1.5.2%gcc@11.3.0+programs build_system=makefile compression=none libs=shared,static arch=linux-ubuntu22.04-zen2
        ^libffi@3.4.4%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^libxcrypt@4.4.33%gcc@11.3.0~obsolete_api build_system=autotools arch=linux-ubuntu22.04-zen2
            ^perl@5.34.0%gcc@11.3.0~cpanm+open+shared+threads build_system=generic arch=linux-ubuntu22.04-zen2
        ^ncurses@6.4%gcc@11.3.0~symlinks+termlib abi=none build_system=autotools arch=linux-ubuntu22.04-zen2
        ^openssl@1.1.1s%gcc@11.3.0~docs~shared build_system=generic certs=mozilla arch=linux-ubuntu22.04-zen2
            ^ca-certificates-mozilla@2023-01-10%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-zen2
        ^pkgconf@1.8.0%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^readline@8.2%gcc@11.3.0 build_system=autotools patches=bbf97f1 arch=linux-ubuntu22.04-zen2
        ^sqlite@3.40.1%gcc@11.3.0+column_metadata+dynamic_extensions+fts~functions+rtree build_system=autotools arch=linux-ubuntu22.04-zen2
        ^util-linux-uuid@2.38.1%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^xz@5.4.1%gcc@11.3.0~pic build_system=autotools libs=shared,static arch=linux-ubuntu22.04-zen2
        ^zlib@1.2.13%gcc@11.3.0+optimize+pic+shared build_system=makefile arch=linux-ubuntu22.04-zen2

Input spec
--------------------------------
py-xxhash

Concretized
--------------------------------
py-xxhash@3.2.0%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
    ^py-pip@22.2.2%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-zen2
    ^py-setuptools@63.0.0%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-zen2
    ^py-setuptools-scm@7.0.5%gcc@11.3.0+toml build_system=python_pip arch=linux-ubuntu22.04-zen2
        ^py-packaging@23.0%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
            ^py-flit-core@3.7.1%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
        ^py-tomli@2.0.1%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
        ^py-typing-extensions@4.3.0%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
    ^py-wheel@0.37.1%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-zen2
    ^python@3.10.8%gcc@11.3.0+bz2+crypt+ctypes+dbm~debug+libxml2+lzma~nis~optimizations+pic+pyexpat+pythoncmd+readline+shared+sqlite3+ssl~tkinter+uuid+zlib build_system=generic patches=0d98e93,7d40923,f2fd060 arch=linux-ubuntu22.04-zen2
        ^bzip2@1.0.8%gcc@11.3.0~debug~pic+shared build_system=generic arch=linux-ubuntu22.04-zen2
            ^diffutils@3.8%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^expat@2.5.0%gcc@11.3.0+libbsd build_system=autotools arch=linux-ubuntu22.04-zen2
            ^libbsd@0.11.7%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
                ^libmd@1.0.4%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^gdbm@1.23%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^gettext@0.21.1%gcc@11.3.0+bzip2+curses+git~libunistring+libxml2+tar+xz build_system=autotools arch=linux-ubuntu22.04-zen2
            ^libiconv@1.17%gcc@11.3.0 build_system=autotools libs=shared,static arch=linux-ubuntu22.04-zen2
            ^libxml2@2.10.3%gcc@11.3.0~python build_system=autotools arch=linux-ubuntu22.04-zen2
            ^tar@1.34%gcc@11.3.0 build_system=autotools zip=pigz arch=linux-ubuntu22.04-zen2
                ^pigz@2.7%gcc@11.3.0 build_system=makefile arch=linux-ubuntu22.04-zen2
                ^zstd@1.5.2%gcc@11.3.0+programs build_system=makefile compression=none libs=shared,static arch=linux-ubuntu22.04-zen2
        ^libffi@3.4.4%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^libxcrypt@4.4.33%gcc@11.3.0~obsolete_api build_system=autotools arch=linux-ubuntu22.04-zen2
            ^perl@5.34.0%gcc@11.3.0~cpanm+open+shared+threads build_system=generic arch=linux-ubuntu22.04-zen2
        ^ncurses@6.4%gcc@11.3.0~symlinks+termlib abi=none build_system=autotools arch=linux-ubuntu22.04-zen2
        ^openssl@1.1.1s%gcc@11.3.0~docs~shared build_system=generic certs=mozilla arch=linux-ubuntu22.04-zen2
            ^ca-certificates-mozilla@2023-01-10%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-zen2
        ^pkgconf@1.8.0%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^readline@8.2%gcc@11.3.0 build_system=autotools patches=bbf97f1 arch=linux-ubuntu22.04-zen2
        ^sqlite@3.40.1%gcc@11.3.0+column_metadata+dynamic_extensions+fts~functions+rtree build_system=autotools arch=linux-ubuntu22.04-zen2
        ^util-linux-uuid@2.38.1%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^xz@5.4.1%gcc@11.3.0~pic build_system=autotools libs=shared,static arch=linux-ubuntu22.04-zen2
        ^zlib@1.2.13%gcc@11.3.0+optimize+pic+shared build_system=makefile arch=linux-ubuntu22.04-zen2
    ^xxhash@0.8.1%gcc@11.3.0 build_system=makefile arch=linux-ubuntu22.04-zen2

Input spec
--------------------------------
py-pyyaml@6

Concretized
--------------------------------
py-pyyaml@6.0%gcc@11.3.0+libyaml build_system=python_pip arch=linux-ubuntu22.04-zen2
    ^libyaml@0.2.5%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
    ^py-cython@0.29.32%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
    ^py-pip@22.2.2%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-zen2
    ^py-setuptools@63.0.0%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-zen2
    ^py-wheel@0.37.1%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-zen2
    ^python@3.10.8%gcc@11.3.0+bz2+crypt+ctypes+dbm~debug+libxml2+lzma~nis~optimizations+pic+pyexpat+pythoncmd+readline+shared+sqlite3+ssl~tkinter+uuid+zlib build_system=generic patches=0d98e93,7d40923,f2fd060 arch=linux-ubuntu22.04-zen2
        ^bzip2@1.0.8%gcc@11.3.0~debug~pic+shared build_system=generic arch=linux-ubuntu22.04-zen2
            ^diffutils@3.8%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^expat@2.5.0%gcc@11.3.0+libbsd build_system=autotools arch=linux-ubuntu22.04-zen2
            ^libbsd@0.11.7%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
                ^libmd@1.0.4%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^gdbm@1.23%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^gettext@0.21.1%gcc@11.3.0+bzip2+curses+git~libunistring+libxml2+tar+xz build_system=autotools arch=linux-ubuntu22.04-zen2
            ^libiconv@1.17%gcc@11.3.0 build_system=autotools libs=shared,static arch=linux-ubuntu22.04-zen2
            ^libxml2@2.10.3%gcc@11.3.0~python build_system=autotools arch=linux-ubuntu22.04-zen2
            ^tar@1.34%gcc@11.3.0 build_system=autotools zip=pigz arch=linux-ubuntu22.04-zen2
                ^pigz@2.7%gcc@11.3.0 build_system=makefile arch=linux-ubuntu22.04-zen2
                ^zstd@1.5.2%gcc@11.3.0+programs build_system=makefile compression=none libs=shared,static arch=linux-ubuntu22.04-zen2
        ^libffi@3.4.4%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^libxcrypt@4.4.33%gcc@11.3.0~obsolete_api build_system=autotools arch=linux-ubuntu22.04-zen2
            ^perl@5.34.0%gcc@11.3.0~cpanm+open+shared+threads build_system=generic arch=linux-ubuntu22.04-zen2
        ^ncurses@6.4%gcc@11.3.0~symlinks+termlib abi=none build_system=autotools arch=linux-ubuntu22.04-zen2
        ^openssl@1.1.1s%gcc@11.3.0~docs~shared build_system=generic certs=mozilla arch=linux-ubuntu22.04-zen2
            ^ca-certificates-mozilla@2023-01-10%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-zen2
        ^pkgconf@1.8.0%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^readline@8.2%gcc@11.3.0 build_system=autotools patches=bbf97f1 arch=linux-ubuntu22.04-zen2
        ^sqlite@3.40.1%gcc@11.3.0+column_metadata+dynamic_extensions+fts~functions+rtree build_system=autotools arch=linux-ubuntu22.04-zen2
        ^util-linux-uuid@2.38.1%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^xz@5.4.1%gcc@11.3.0~pic build_system=autotools libs=shared,static arch=linux-ubuntu22.04-zen2
        ^zlib@1.2.13%gcc@11.3.0+optimize+pic+shared build_system=makefile arch=linux-ubuntu22.04-zen2

Input spec
--------------------------------
py-charmonium-time-block@0.3.1:

Concretized
--------------------------------
py-charmonium-time-block@0.3.2%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
    ^py-pip@22.2.2%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-zen2
    ^py-poetry-core@1.2.0%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
    ^py-psutil@5.9.2%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
        ^py-setuptools@63.0.0%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-zen2
    ^py-wheel@0.37.1%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-zen2
    ^python@3.10.8%gcc@11.3.0+bz2+crypt+ctypes+dbm~debug+libxml2+lzma~nis~optimizations+pic+pyexpat+pythoncmd+readline+shared+sqlite3+ssl~tkinter+uuid+zlib build_system=generic patches=0d98e93,7d40923,f2fd060 arch=linux-ubuntu22.04-zen2
        ^bzip2@1.0.8%gcc@11.3.0~debug~pic+shared build_system=generic arch=linux-ubuntu22.04-zen2
            ^diffutils@3.8%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^expat@2.5.0%gcc@11.3.0+libbsd build_system=autotools arch=linux-ubuntu22.04-zen2
            ^libbsd@0.11.7%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
                ^libmd@1.0.4%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^gdbm@1.23%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^gettext@0.21.1%gcc@11.3.0+bzip2+curses+git~libunistring+libxml2+tar+xz build_system=autotools arch=linux-ubuntu22.04-zen2
            ^libiconv@1.17%gcc@11.3.0 build_system=autotools libs=shared,static arch=linux-ubuntu22.04-zen2
            ^libxml2@2.10.3%gcc@11.3.0~python build_system=autotools arch=linux-ubuntu22.04-zen2
            ^tar@1.34%gcc@11.3.0 build_system=autotools zip=pigz arch=linux-ubuntu22.04-zen2
                ^pigz@2.7%gcc@11.3.0 build_system=makefile arch=linux-ubuntu22.04-zen2
                ^zstd@1.5.2%gcc@11.3.0+programs build_system=makefile compression=none libs=shared,static arch=linux-ubuntu22.04-zen2
        ^libffi@3.4.4%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^libxcrypt@4.4.33%gcc@11.3.0~obsolete_api build_system=autotools arch=linux-ubuntu22.04-zen2
            ^perl@5.34.0%gcc@11.3.0~cpanm+open+shared+threads build_system=generic arch=linux-ubuntu22.04-zen2
        ^ncurses@6.4%gcc@11.3.0~symlinks+termlib abi=none build_system=autotools arch=linux-ubuntu22.04-zen2
        ^openssl@1.1.1s%gcc@11.3.0~docs~shared build_system=generic certs=mozilla arch=linux-ubuntu22.04-zen2
            ^ca-certificates-mozilla@2023-01-10%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-zen2
        ^pkgconf@1.8.0%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^readline@8.2%gcc@11.3.0 build_system=autotools patches=bbf97f1 arch=linux-ubuntu22.04-zen2
        ^sqlite@3.40.1%gcc@11.3.0+column_metadata+dynamic_extensions+fts~functions+rtree build_system=autotools arch=linux-ubuntu22.04-zen2
        ^util-linux-uuid@2.38.1%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^xz@5.4.1%gcc@11.3.0~pic build_system=autotools libs=shared,static arch=linux-ubuntu22.04-zen2
        ^zlib@1.2.13%gcc@11.3.0+optimize+pic+shared build_system=makefile arch=linux-ubuntu22.04-zen2

Input spec
--------------------------------
py-charmonium-freeze@0.7:

Concretized
--------------------------------
py-charmonium-freeze@0.7.0%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
    ^py-pip@22.2.2%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-zen2
    ^py-poetry-core@1.2.0%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
    ^py-psutil@5.9.2%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
        ^py-setuptools@63.0.0%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-zen2
    ^py-wheel@0.37.1%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-zen2
    ^python@3.10.8%gcc@11.3.0+bz2+crypt+ctypes+dbm~debug+libxml2+lzma~nis~optimizations+pic+pyexpat+pythoncmd+readline+shared+sqlite3+ssl~tkinter+uuid+zlib build_system=generic patches=0d98e93,7d40923,f2fd060 arch=linux-ubuntu22.04-zen2
        ^bzip2@1.0.8%gcc@11.3.0~debug~pic+shared build_system=generic arch=linux-ubuntu22.04-zen2
            ^diffutils@3.8%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^expat@2.5.0%gcc@11.3.0+libbsd build_system=autotools arch=linux-ubuntu22.04-zen2
            ^libbsd@0.11.7%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
                ^libmd@1.0.4%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^gdbm@1.23%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^gettext@0.21.1%gcc@11.3.0+bzip2+curses+git~libunistring+libxml2+tar+xz build_system=autotools arch=linux-ubuntu22.04-zen2
            ^libiconv@1.17%gcc@11.3.0 build_system=autotools libs=shared,static arch=linux-ubuntu22.04-zen2
            ^libxml2@2.10.3%gcc@11.3.0~python build_system=autotools arch=linux-ubuntu22.04-zen2
            ^tar@1.34%gcc@11.3.0 build_system=autotools zip=pigz arch=linux-ubuntu22.04-zen2
                ^pigz@2.7%gcc@11.3.0 build_system=makefile arch=linux-ubuntu22.04-zen2
                ^zstd@1.5.2%gcc@11.3.0+programs build_system=makefile compression=none libs=shared,static arch=linux-ubuntu22.04-zen2
        ^libffi@3.4.4%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^libxcrypt@4.4.33%gcc@11.3.0~obsolete_api build_system=autotools arch=linux-ubuntu22.04-zen2
            ^perl@5.34.0%gcc@11.3.0~cpanm+open+shared+threads build_system=generic arch=linux-ubuntu22.04-zen2
        ^ncurses@6.4%gcc@11.3.0~symlinks+termlib abi=none build_system=autotools arch=linux-ubuntu22.04-zen2
        ^openssl@1.1.1s%gcc@11.3.0~docs~shared build_system=generic certs=mozilla arch=linux-ubuntu22.04-zen2
            ^ca-certificates-mozilla@2023-01-10%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-zen2
        ^pkgconf@1.8.0%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^readline@8.2%gcc@11.3.0 build_system=autotools patches=bbf97f1 arch=linux-ubuntu22.04-zen2
        ^sqlite@3.40.1%gcc@11.3.0+column_metadata+dynamic_extensions+fts~functions+rtree build_system=autotools arch=linux-ubuntu22.04-zen2
        ^util-linux-uuid@2.38.1%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^xz@5.4.1%gcc@11.3.0~pic build_system=autotools libs=shared,static arch=linux-ubuntu22.04-zen2
        ^zlib@1.2.13%gcc@11.3.0+optimize+pic+shared build_system=makefile arch=linux-ubuntu22.04-zen2

Input spec
--------------------------------
py-universal-pathlib

Concretized
--------------------------------
py-universal-pathlib@0.0.21%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
    ^py-flit-core@3.7.1%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
    ^py-fsspec@2023.1.0%gcc@11.3.0~http build_system=python_pip arch=linux-ubuntu22.04-zen2
        ^py-setuptools@63.0.0%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-zen2
    ^py-pip@22.2.2%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-zen2
    ^py-wheel@0.37.1%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-zen2
    ^python@3.10.8%gcc@11.3.0+bz2+crypt+ctypes+dbm~debug+libxml2+lzma~nis~optimizations+pic+pyexpat+pythoncmd+readline+shared+sqlite3+ssl~tkinter+uuid+zlib build_system=generic patches=0d98e93,7d40923,f2fd060 arch=linux-ubuntu22.04-zen2
        ^bzip2@1.0.8%gcc@11.3.0~debug~pic+shared build_system=generic arch=linux-ubuntu22.04-zen2
            ^diffutils@3.8%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^expat@2.5.0%gcc@11.3.0+libbsd build_system=autotools arch=linux-ubuntu22.04-zen2
            ^libbsd@0.11.7%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
                ^libmd@1.0.4%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^gdbm@1.23%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^gettext@0.21.1%gcc@11.3.0+bzip2+curses+git~libunistring+libxml2+tar+xz build_system=autotools arch=linux-ubuntu22.04-zen2
            ^libiconv@1.17%gcc@11.3.0 build_system=autotools libs=shared,static arch=linux-ubuntu22.04-zen2
            ^libxml2@2.10.3%gcc@11.3.0~python build_system=autotools arch=linux-ubuntu22.04-zen2
            ^tar@1.34%gcc@11.3.0 build_system=autotools zip=pigz arch=linux-ubuntu22.04-zen2
                ^pigz@2.7%gcc@11.3.0 build_system=makefile arch=linux-ubuntu22.04-zen2
                ^zstd@1.5.2%gcc@11.3.0+programs build_system=makefile compression=none libs=shared,static arch=linux-ubuntu22.04-zen2
        ^libffi@3.4.4%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^libxcrypt@4.4.33%gcc@11.3.0~obsolete_api build_system=autotools arch=linux-ubuntu22.04-zen2
            ^perl@5.34.0%gcc@11.3.0~cpanm+open+shared+threads build_system=generic arch=linux-ubuntu22.04-zen2
        ^ncurses@6.4%gcc@11.3.0~symlinks+termlib abi=none build_system=autotools arch=linux-ubuntu22.04-zen2
        ^openssl@1.1.1s%gcc@11.3.0~docs~shared build_system=generic certs=mozilla arch=linux-ubuntu22.04-zen2
            ^ca-certificates-mozilla@2023-01-10%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-zen2
        ^pkgconf@1.8.0%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^readline@8.2%gcc@11.3.0 build_system=autotools patches=bbf97f1 arch=linux-ubuntu22.04-zen2
        ^sqlite@3.40.1%gcc@11.3.0+column_metadata+dynamic_extensions+fts~functions+rtree build_system=autotools arch=linux-ubuntu22.04-zen2
        ^util-linux-uuid@2.38.1%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^xz@5.4.1%gcc@11.3.0~pic build_system=autotools libs=shared,static arch=linux-ubuntu22.04-zen2
        ^zlib@1.2.13%gcc@11.3.0+optimize+pic+shared build_system=makefile arch=linux-ubuntu22.04-zen2

Input spec
--------------------------------
py-toolz

Concretized
--------------------------------
py-toolz@0.12.0%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
    ^py-pip@22.2.2%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-zen2
    ^py-setuptools@63.0.0%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-zen2
    ^py-wheel@0.37.1%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-zen2
    ^python@3.10.8%gcc@11.3.0+bz2+crypt+ctypes+dbm~debug+libxml2+lzma~nis~optimizations+pic+pyexpat+pythoncmd+readline+shared+sqlite3+ssl~tkinter+uuid+zlib build_system=generic patches=0d98e93,7d40923,f2fd060 arch=linux-ubuntu22.04-zen2
        ^bzip2@1.0.8%gcc@11.3.0~debug~pic+shared build_system=generic arch=linux-ubuntu22.04-zen2
            ^diffutils@3.8%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^expat@2.5.0%gcc@11.3.0+libbsd build_system=autotools arch=linux-ubuntu22.04-zen2
            ^libbsd@0.11.7%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
                ^libmd@1.0.4%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^gdbm@1.23%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^gettext@0.21.1%gcc@11.3.0+bzip2+curses+git~libunistring+libxml2+tar+xz build_system=autotools arch=linux-ubuntu22.04-zen2
            ^libiconv@1.17%gcc@11.3.0 build_system=autotools libs=shared,static arch=linux-ubuntu22.04-zen2
            ^libxml2@2.10.3%gcc@11.3.0~python build_system=autotools arch=linux-ubuntu22.04-zen2
            ^tar@1.34%gcc@11.3.0 build_system=autotools zip=pigz arch=linux-ubuntu22.04-zen2
                ^pigz@2.7%gcc@11.3.0 build_system=makefile arch=linux-ubuntu22.04-zen2
                ^zstd@1.5.2%gcc@11.3.0+programs build_system=makefile compression=none libs=shared,static arch=linux-ubuntu22.04-zen2
        ^libffi@3.4.4%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^libxcrypt@4.4.33%gcc@11.3.0~obsolete_api build_system=autotools arch=linux-ubuntu22.04-zen2
            ^perl@5.34.0%gcc@11.3.0~cpanm+open+shared+threads build_system=generic arch=linux-ubuntu22.04-zen2
        ^ncurses@6.4%gcc@11.3.0~symlinks+termlib abi=none build_system=autotools arch=linux-ubuntu22.04-zen2
        ^openssl@1.1.1s%gcc@11.3.0~docs~shared build_system=generic certs=mozilla arch=linux-ubuntu22.04-zen2
            ^ca-certificates-mozilla@2023-01-10%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-zen2
        ^pkgconf@1.8.0%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^readline@8.2%gcc@11.3.0 build_system=autotools patches=bbf97f1 arch=linux-ubuntu22.04-zen2
        ^sqlite@3.40.1%gcc@11.3.0+column_metadata+dynamic_extensions+fts~functions+rtree build_system=autotools arch=linux-ubuntu22.04-zen2
        ^util-linux-uuid@2.38.1%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^xz@5.4.1%gcc@11.3.0~pic build_system=autotools libs=shared,static arch=linux-ubuntu22.04-zen2
        ^zlib@1.2.13%gcc@11.3.0+optimize+pic+shared build_system=makefile arch=linux-ubuntu22.04-zen2

Input spec
--------------------------------
py-parsl

Concretized
--------------------------------
py-parsl@1.1.0%gcc@11.3.0~monitoring build_system=python_pip arch=linux-ubuntu22.04-zen2
    ^py-dill@0.3.6%gcc@11.3.0 build_system=python_pip patches=daf79b1 arch=linux-ubuntu22.04-zen2
    ^py-globus-sdk@3.10.1%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
        ^py-cryptography@38.0.1%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
            ^git@2.39.1%gcc@11.3.0+man+nls+perl+subtree~svn~tcltk build_system=autotools arch=linux-ubuntu22.04-zen2
                ^autoconf@2.69%gcc@11.3.0 build_system=autotools patches=35c4492,7793209,a49dd5b arch=linux-ubuntu22.04-zen2
                ^automake@1.16.5%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
                ^curl@7.87.0%gcc@11.3.0~gssapi~ldap~libidn2~librtmp~libssh~libssh2~nghttp2 build_system=autotools libs=shared,static tls=openssl arch=linux-ubuntu22.04-zen2
                ^libidn2@2.3.4%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
                    ^libunistring@1.1%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
                ^libtool@2.4.7%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
                ^m4@1.4.19%gcc@11.3.0+sigsegv build_system=autotools patches=9dc5fbd,bfdffa7 arch=linux-ubuntu22.04-zen2
                    ^libsigsegv@2.13%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
                ^openssh@9.1p1%gcc@11.3.0+gssapi build_system=autotools arch=linux-ubuntu22.04-zen2
                    ^krb5@1.20.1%gcc@11.3.0+shared build_system=autotools arch=linux-ubuntu22.04-zen2
                        ^bison@3.8.2%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
                    ^libedit@3.1-20210216%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
                ^pcre2@10.42%gcc@11.3.0~jit+multibyte build_system=autotools arch=linux-ubuntu22.04-zen2
            ^py-cffi@1.15.1%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
                ^py-pycparser@2.21%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
            ^py-setuptools-rust@1.5.1%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
                ^py-semantic-version@2.10.0%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
            ^rust@1.61.0%gcc@11.3.0+analysis+clippy~rls+rustfmt+src build_system=generic extra_targets=none arch=linux-ubuntu22.04-zen2
        ^py-pyjwt@2.4.0%gcc@11.3.0+crypto build_system=python_pip arch=linux-ubuntu22.04-zen2
    ^py-paramiko@2.12.0%gcc@11.3.0~invoke build_system=python_pip arch=linux-ubuntu22.04-zen2
        ^py-bcrypt@3.2.0%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
        ^py-pynacl@1.5.0%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
        ^py-six@1.16.0%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
    ^py-pip@22.2.2%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-zen2
    ^py-psutil@5.9.2%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
    ^py-pyzmq@24.0.1%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
        ^libzmq@4.3.4%gcc@11.3.0~docs~drafts+libbsd+libsodium~libunwind build_system=autotools patches=310b8aa arch=linux-ubuntu22.04-zen2
            ^libbsd@0.11.7%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
                ^libmd@1.0.4%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
            ^libsodium@1.0.18%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^py-cython@0.29.32%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
        ^py-gevent@1.5.0%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
            ^py-greenlet@1.1.3%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
        ^py-packaging@23.0%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
    ^py-requests@2.28.1%gcc@11.3.0~socks build_system=python_pip arch=linux-ubuntu22.04-zen2
        ^py-certifi@2022.9.14%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
        ^py-charset-normalizer@2.0.12%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
        ^py-idna@3.4%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
        ^py-urllib3@1.26.12%gcc@11.3.0~brotli~secure~socks build_system=python_pip arch=linux-ubuntu22.04-zen2
    ^py-setuptools@63.0.0%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-zen2
    ^py-tblib@1.6.0%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
    ^py-typeguard@2.12.1%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
        ^py-setuptools-scm@7.0.5%gcc@11.3.0+toml build_system=python_pip arch=linux-ubuntu22.04-zen2
            ^py-tomli@2.0.1%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
    ^py-typing-extensions@4.3.0%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
        ^py-flit-core@3.7.1%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
    ^py-wheel@0.37.1%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-zen2
    ^python@3.10.8%gcc@11.3.0+bz2+crypt+ctypes+dbm~debug+libxml2+lzma~nis~optimizations+pic+pyexpat+pythoncmd+readline+shared+sqlite3+ssl~tkinter+uuid+zlib build_system=generic patches=0d98e93,7d40923,f2fd060 arch=linux-ubuntu22.04-zen2
        ^bzip2@1.0.8%gcc@11.3.0~debug~pic+shared build_system=generic arch=linux-ubuntu22.04-zen2
            ^diffutils@3.8%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^expat@2.5.0%gcc@11.3.0+libbsd build_system=autotools arch=linux-ubuntu22.04-zen2
        ^gdbm@1.23%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^gettext@0.21.1%gcc@11.3.0+bzip2+curses+git~libunistring+libxml2+tar+xz build_system=autotools arch=linux-ubuntu22.04-zen2
            ^libiconv@1.17%gcc@11.3.0 build_system=autotools libs=shared,static arch=linux-ubuntu22.04-zen2
            ^libxml2@2.10.3%gcc@11.3.0~python build_system=autotools arch=linux-ubuntu22.04-zen2
            ^tar@1.34%gcc@11.3.0 build_system=autotools zip=pigz arch=linux-ubuntu22.04-zen2
                ^pigz@2.7%gcc@11.3.0 build_system=makefile arch=linux-ubuntu22.04-zen2
                ^zstd@1.5.2%gcc@11.3.0+programs build_system=makefile compression=none libs=shared,static arch=linux-ubuntu22.04-zen2
        ^libffi@3.4.4%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^libxcrypt@4.4.33%gcc@11.3.0~obsolete_api build_system=autotools arch=linux-ubuntu22.04-zen2
            ^perl@5.34.0%gcc@11.3.0~cpanm+open+shared+threads build_system=generic arch=linux-ubuntu22.04-zen2
        ^ncurses@6.4%gcc@11.3.0~symlinks+termlib abi=none build_system=autotools arch=linux-ubuntu22.04-zen2
        ^openssl@1.1.1s%gcc@11.3.0~docs~shared build_system=generic certs=mozilla arch=linux-ubuntu22.04-zen2
            ^ca-certificates-mozilla@2023-01-10%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-zen2
        ^pkgconf@1.8.0%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^readline@8.2%gcc@11.3.0 build_system=autotools patches=bbf97f1 arch=linux-ubuntu22.04-zen2
        ^sqlite@3.40.1%gcc@11.3.0+column_metadata+dynamic_extensions+fts~functions+rtree build_system=autotools arch=linux-ubuntu22.04-zen2
        ^util-linux-uuid@2.38.1%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^xz@5.4.1%gcc@11.3.0~pic build_system=autotools libs=shared,static arch=linux-ubuntu22.04-zen2
        ^zlib@1.2.13%gcc@11.3.0+optimize+pic+shared build_system=makefile arch=linux-ubuntu22.04-zen2

Input spec
--------------------------------
py-fasteners@0.18:

Concretized
--------------------------------
py-fasteners@0.18%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
    ^py-pip@22.2.2%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-zen2
    ^py-setuptools@63.0.0%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-zen2
    ^py-wheel@0.37.1%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-zen2
    ^python@3.10.8%gcc@11.3.0+bz2+crypt+ctypes+dbm~debug+libxml2+lzma~nis~optimizations+pic+pyexpat+pythoncmd+readline+shared+sqlite3+ssl~tkinter+uuid+zlib build_system=generic patches=0d98e93,7d40923,f2fd060 arch=linux-ubuntu22.04-zen2
        ^bzip2@1.0.8%gcc@11.3.0~debug~pic+shared build_system=generic arch=linux-ubuntu22.04-zen2
            ^diffutils@3.8%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^expat@2.5.0%gcc@11.3.0+libbsd build_system=autotools arch=linux-ubuntu22.04-zen2
            ^libbsd@0.11.7%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
                ^libmd@1.0.4%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^gdbm@1.23%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^gettext@0.21.1%gcc@11.3.0+bzip2+curses+git~libunistring+libxml2+tar+xz build_system=autotools arch=linux-ubuntu22.04-zen2
            ^libiconv@1.17%gcc@11.3.0 build_system=autotools libs=shared,static arch=linux-ubuntu22.04-zen2
            ^libxml2@2.10.3%gcc@11.3.0~python build_system=autotools arch=linux-ubuntu22.04-zen2
            ^tar@1.34%gcc@11.3.0 build_system=autotools zip=pigz arch=linux-ubuntu22.04-zen2
                ^pigz@2.7%gcc@11.3.0 build_system=makefile arch=linux-ubuntu22.04-zen2
                ^zstd@1.5.2%gcc@11.3.0+programs build_system=makefile compression=none libs=shared,static arch=linux-ubuntu22.04-zen2
        ^libffi@3.4.4%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^libxcrypt@4.4.33%gcc@11.3.0~obsolete_api build_system=autotools arch=linux-ubuntu22.04-zen2
            ^perl@5.34.0%gcc@11.3.0~cpanm+open+shared+threads build_system=generic arch=linux-ubuntu22.04-zen2
        ^ncurses@6.4%gcc@11.3.0~symlinks+termlib abi=none build_system=autotools arch=linux-ubuntu22.04-zen2
        ^openssl@1.1.1s%gcc@11.3.0~docs~shared build_system=generic certs=mozilla arch=linux-ubuntu22.04-zen2
            ^ca-certificates-mozilla@2023-01-10%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-zen2
        ^pkgconf@1.8.0%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^readline@8.2%gcc@11.3.0 build_system=autotools patches=bbf97f1 arch=linux-ubuntu22.04-zen2
        ^sqlite@3.40.1%gcc@11.3.0+column_metadata+dynamic_extensions+fts~functions+rtree build_system=autotools arch=linux-ubuntu22.04-zen2
        ^util-linux-uuid@2.38.1%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^xz@5.4.1%gcc@11.3.0~pic build_system=autotools libs=shared,static arch=linux-ubuntu22.04-zen2
        ^zlib@1.2.13%gcc@11.3.0+optimize+pic+shared build_system=makefile arch=linux-ubuntu22.04-zen2

Input spec
--------------------------------
py-adlfs@2022

Concretized
--------------------------------
py-adlfs@2022.11.2%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
    ^py-aiohttp@3.8.1%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
        ^py-aiosignal@1.2.0%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
        ^py-async-timeout@4.0.2%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
        ^py-attrs@22.1.0%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
        ^py-charset-normalizer@2.0.12%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
        ^py-frozenlist@1.3.1%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
        ^py-multidict@6.0.2%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
        ^py-setuptools@63.0.0%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-zen2
        ^py-yarl@1.8.1%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
            ^py-cython@0.29.32%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
            ^py-idna@3.4%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
                ^py-flit-core@3.7.1%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
    ^py-azure-datalake-store@0.0.48%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
        ^py-adal@1.2.4%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
            ^py-pyjwt@2.4.0%gcc@11.3.0+crypto build_system=python_pip arch=linux-ubuntu22.04-zen2
            ^py-python-dateutil@2.8.2%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
                ^py-setuptools-scm@7.0.5%gcc@11.3.0+toml build_system=python_pip arch=linux-ubuntu22.04-zen2
                    ^py-packaging@23.0%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
                    ^py-tomli@2.0.1%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
        ^py-cffi@1.15.1%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
            ^py-pycparser@2.21%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
        ^py-requests@2.28.1%gcc@11.3.0~socks build_system=python_pip arch=linux-ubuntu22.04-zen2
            ^py-certifi@2022.9.14%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
            ^py-urllib3@1.26.12%gcc@11.3.0~brotli~secure~socks build_system=python_pip arch=linux-ubuntu22.04-zen2
    ^py-azure-storage-blob@12.9.0%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
        ^py-azure-core@1.26.1%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
            ^py-six@1.16.0%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
            ^py-typing-extensions@4.3.0%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
        ^py-cryptography@38.0.1%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
            ^git@2.39.1%gcc@11.3.0+man+nls+perl+subtree~svn~tcltk build_system=autotools arch=linux-ubuntu22.04-zen2
                ^autoconf@2.69%gcc@11.3.0 build_system=autotools patches=35c4492,7793209,a49dd5b arch=linux-ubuntu22.04-zen2
                ^automake@1.16.5%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
                ^curl@7.87.0%gcc@11.3.0~gssapi~ldap~libidn2~librtmp~libssh~libssh2~nghttp2 build_system=autotools libs=shared,static tls=openssl arch=linux-ubuntu22.04-zen2
                ^libidn2@2.3.4%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
                    ^libunistring@1.1%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
                ^libtool@2.4.7%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
                ^m4@1.4.19%gcc@11.3.0+sigsegv build_system=autotools patches=9dc5fbd,bfdffa7 arch=linux-ubuntu22.04-zen2
                    ^libsigsegv@2.13%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
                ^openssh@9.1p1%gcc@11.3.0+gssapi build_system=autotools arch=linux-ubuntu22.04-zen2
                    ^krb5@1.20.1%gcc@11.3.0+shared build_system=autotools arch=linux-ubuntu22.04-zen2
                        ^bison@3.8.2%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
                    ^libedit@3.1-20210216%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
                ^pcre2@10.42%gcc@11.3.0~jit+multibyte build_system=autotools arch=linux-ubuntu22.04-zen2
            ^py-setuptools-rust@1.5.1%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
                ^py-semantic-version@2.10.0%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
            ^rust@1.61.0%gcc@11.3.0+analysis+clippy~rls+rustfmt+src build_system=generic extra_targets=none arch=linux-ubuntu22.04-zen2
        ^py-msrest@0.6.21%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
            ^py-isodate@0.6.1%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
            ^py-requests-oauthlib@1.3.1%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
                ^py-oauthlib@3.2.1%gcc@11.3.0~rsa~signals~signedtoken build_system=python_pip arch=linux-ubuntu22.04-zen2
    ^py-fsspec@2023.1.0%gcc@11.3.0~http build_system=python_pip arch=linux-ubuntu22.04-zen2
    ^py-pip@22.2.2%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-zen2
    ^py-wheel@0.37.1%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-zen2
    ^python@3.10.8%gcc@11.3.0+bz2+crypt+ctypes+dbm~debug+libxml2+lzma~nis~optimizations+pic+pyexpat+pythoncmd+readline+shared+sqlite3+ssl~tkinter+uuid+zlib build_system=generic patches=0d98e93,7d40923,f2fd060 arch=linux-ubuntu22.04-zen2
        ^bzip2@1.0.8%gcc@11.3.0~debug~pic+shared build_system=generic arch=linux-ubuntu22.04-zen2
            ^diffutils@3.8%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^expat@2.5.0%gcc@11.3.0+libbsd build_system=autotools arch=linux-ubuntu22.04-zen2
            ^libbsd@0.11.7%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
                ^libmd@1.0.4%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^gdbm@1.23%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^gettext@0.21.1%gcc@11.3.0+bzip2+curses+git~libunistring+libxml2+tar+xz build_system=autotools arch=linux-ubuntu22.04-zen2
            ^libiconv@1.17%gcc@11.3.0 build_system=autotools libs=shared,static arch=linux-ubuntu22.04-zen2
            ^libxml2@2.10.3%gcc@11.3.0~python build_system=autotools arch=linux-ubuntu22.04-zen2
            ^tar@1.34%gcc@11.3.0 build_system=autotools zip=pigz arch=linux-ubuntu22.04-zen2
                ^pigz@2.7%gcc@11.3.0 build_system=makefile arch=linux-ubuntu22.04-zen2
                ^zstd@1.5.2%gcc@11.3.0+programs build_system=makefile compression=none libs=shared,static arch=linux-ubuntu22.04-zen2
        ^libffi@3.4.4%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^libxcrypt@4.4.33%gcc@11.3.0~obsolete_api build_system=autotools arch=linux-ubuntu22.04-zen2
            ^perl@5.34.0%gcc@11.3.0~cpanm+open+shared+threads build_system=generic arch=linux-ubuntu22.04-zen2
        ^ncurses@6.4%gcc@11.3.0~symlinks+termlib abi=none build_system=autotools arch=linux-ubuntu22.04-zen2
        ^openssl@1.1.1s%gcc@11.3.0~docs~shared build_system=generic certs=mozilla arch=linux-ubuntu22.04-zen2
            ^ca-certificates-mozilla@2023-01-10%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-zen2
        ^pkgconf@1.8.0%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^readline@8.2%gcc@11.3.0 build_system=autotools patches=bbf97f1 arch=linux-ubuntu22.04-zen2
        ^sqlite@3.40.1%gcc@11.3.0+column_metadata+dynamic_extensions+fts~functions+rtree build_system=autotools arch=linux-ubuntu22.04-zen2
        ^util-linux-uuid@2.38.1%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^xz@5.4.1%gcc@11.3.0~pic build_system=autotools libs=shared,static arch=linux-ubuntu22.04-zen2
        ^zlib@1.2.13%gcc@11.3.0+optimize+pic+shared build_system=makefile arch=linux-ubuntu22.04-zen2

Input spec
--------------------------------
py-click@8

Concretized
--------------------------------
py-click@8.1.3%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
    ^py-pip@22.2.2%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-zen2
    ^py-setuptools@63.0.0%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-zen2
    ^py-wheel@0.37.1%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-zen2
    ^python@3.10.8%gcc@11.3.0+bz2+crypt+ctypes+dbm~debug+libxml2+lzma~nis~optimizations+pic+pyexpat+pythoncmd+readline+shared+sqlite3+ssl~tkinter+uuid+zlib build_system=generic patches=0d98e93,7d40923,f2fd060 arch=linux-ubuntu22.04-zen2
        ^bzip2@1.0.8%gcc@11.3.0~debug~pic+shared build_system=generic arch=linux-ubuntu22.04-zen2
            ^diffutils@3.8%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^expat@2.5.0%gcc@11.3.0+libbsd build_system=autotools arch=linux-ubuntu22.04-zen2
            ^libbsd@0.11.7%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
                ^libmd@1.0.4%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^gdbm@1.23%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^gettext@0.21.1%gcc@11.3.0+bzip2+curses+git~libunistring+libxml2+tar+xz build_system=autotools arch=linux-ubuntu22.04-zen2
            ^libiconv@1.17%gcc@11.3.0 build_system=autotools libs=shared,static arch=linux-ubuntu22.04-zen2
            ^libxml2@2.10.3%gcc@11.3.0~python build_system=autotools arch=linux-ubuntu22.04-zen2
            ^tar@1.34%gcc@11.3.0 build_system=autotools zip=pigz arch=linux-ubuntu22.04-zen2
                ^pigz@2.7%gcc@11.3.0 build_system=makefile arch=linux-ubuntu22.04-zen2
                ^zstd@1.5.2%gcc@11.3.0+programs build_system=makefile compression=none libs=shared,static arch=linux-ubuntu22.04-zen2
        ^libffi@3.4.4%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^libxcrypt@4.4.33%gcc@11.3.0~obsolete_api build_system=autotools arch=linux-ubuntu22.04-zen2
            ^perl@5.34.0%gcc@11.3.0~cpanm+open+shared+threads build_system=generic arch=linux-ubuntu22.04-zen2
        ^ncurses@6.4%gcc@11.3.0~symlinks+termlib abi=none build_system=autotools arch=linux-ubuntu22.04-zen2
        ^openssl@1.1.1s%gcc@11.3.0~docs~shared build_system=generic certs=mozilla arch=linux-ubuntu22.04-zen2
            ^ca-certificates-mozilla@2023-01-10%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-zen2
        ^pkgconf@1.8.0%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^readline@8.2%gcc@11.3.0 build_system=autotools patches=bbf97f1 arch=linux-ubuntu22.04-zen2
        ^sqlite@3.40.1%gcc@11.3.0+column_metadata+dynamic_extensions+fts~functions+rtree build_system=autotools arch=linux-ubuntu22.04-zen2
        ^util-linux-uuid@2.38.1%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^xz@5.4.1%gcc@11.3.0~pic build_system=autotools libs=shared,static arch=linux-ubuntu22.04-zen2
        ^zlib@1.2.13%gcc@11.3.0+optimize+pic+shared build_system=makefile arch=linux-ubuntu22.04-zen2

Input spec
--------------------------------
py-lazy-object-proxy

Concretized
--------------------------------
py-lazy-object-proxy@1.7.1%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
    ^py-pip@22.2.2%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-zen2
    ^py-setuptools@63.0.0%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-zen2
    ^py-setuptools-scm@7.0.5%gcc@11.3.0+toml build_system=python_pip arch=linux-ubuntu22.04-zen2
        ^py-packaging@23.0%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
            ^py-flit-core@3.7.1%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
        ^py-tomli@2.0.1%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
        ^py-typing-extensions@4.3.0%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
    ^py-wheel@0.37.1%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-zen2
    ^python@3.10.8%gcc@11.3.0+bz2+crypt+ctypes+dbm~debug+libxml2+lzma~nis~optimizations+pic+pyexpat+pythoncmd+readline+shared+sqlite3+ssl~tkinter+uuid+zlib build_system=generic patches=0d98e93,7d40923,f2fd060 arch=linux-ubuntu22.04-zen2
        ^bzip2@1.0.8%gcc@11.3.0~debug~pic+shared build_system=generic arch=linux-ubuntu22.04-zen2
            ^diffutils@3.8%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^expat@2.5.0%gcc@11.3.0+libbsd build_system=autotools arch=linux-ubuntu22.04-zen2
            ^libbsd@0.11.7%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
                ^libmd@1.0.4%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^gdbm@1.23%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^gettext@0.21.1%gcc@11.3.0+bzip2+curses+git~libunistring+libxml2+tar+xz build_system=autotools arch=linux-ubuntu22.04-zen2
            ^libiconv@1.17%gcc@11.3.0 build_system=autotools libs=shared,static arch=linux-ubuntu22.04-zen2
            ^libxml2@2.10.3%gcc@11.3.0~python build_system=autotools arch=linux-ubuntu22.04-zen2
            ^tar@1.34%gcc@11.3.0 build_system=autotools zip=pigz arch=linux-ubuntu22.04-zen2
                ^pigz@2.7%gcc@11.3.0 build_system=makefile arch=linux-ubuntu22.04-zen2
                ^zstd@1.5.2%gcc@11.3.0+programs build_system=makefile compression=none libs=shared,static arch=linux-ubuntu22.04-zen2
        ^libffi@3.4.4%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^libxcrypt@4.4.33%gcc@11.3.0~obsolete_api build_system=autotools arch=linux-ubuntu22.04-zen2
            ^perl@5.34.0%gcc@11.3.0~cpanm+open+shared+threads build_system=generic arch=linux-ubuntu22.04-zen2
        ^ncurses@6.4%gcc@11.3.0~symlinks+termlib abi=none build_system=autotools arch=linux-ubuntu22.04-zen2
        ^openssl@1.1.1s%gcc@11.3.0~docs~shared build_system=generic certs=mozilla arch=linux-ubuntu22.04-zen2
            ^ca-certificates-mozilla@2023-01-10%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-zen2
        ^pkgconf@1.8.0%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^readline@8.2%gcc@11.3.0 build_system=autotools patches=bbf97f1 arch=linux-ubuntu22.04-zen2
        ^sqlite@3.40.1%gcc@11.3.0+column_metadata+dynamic_extensions+fts~functions+rtree build_system=autotools arch=linux-ubuntu22.04-zen2
        ^util-linux-uuid@2.38.1%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^xz@5.4.1%gcc@11.3.0~pic build_system=autotools libs=shared,static arch=linux-ubuntu22.04-zen2
        ^zlib@1.2.13%gcc@11.3.0+optimize+pic+shared build_system=makefile arch=linux-ubuntu22.04-zen2

Input spec
--------------------------------
py-azure-identity

Concretized
--------------------------------
py-azure-identity@1.12.0%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
    ^py-azure-core@1.26.1%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
        ^py-requests@2.28.1%gcc@11.3.0~socks build_system=python_pip arch=linux-ubuntu22.04-zen2
            ^py-certifi@2022.9.14%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
            ^py-charset-normalizer@2.0.12%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
            ^py-idna@3.4%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
            ^py-urllib3@1.26.12%gcc@11.3.0~brotli~secure~socks build_system=python_pip arch=linux-ubuntu22.04-zen2
        ^py-typing-extensions@4.3.0%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
            ^py-flit-core@3.7.1%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
    ^py-cryptography@38.0.1%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
        ^git@2.39.1%gcc@11.3.0+man+nls+perl+subtree~svn~tcltk build_system=autotools arch=linux-ubuntu22.04-zen2
            ^autoconf@2.69%gcc@11.3.0 build_system=autotools patches=35c4492,7793209,a49dd5b arch=linux-ubuntu22.04-zen2
            ^automake@1.16.5%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
            ^curl@7.87.0%gcc@11.3.0~gssapi~ldap~libidn2~librtmp~libssh~libssh2~nghttp2 build_system=autotools libs=shared,static tls=openssl arch=linux-ubuntu22.04-zen2
            ^libiconv@1.17%gcc@11.3.0 build_system=autotools libs=shared,static arch=linux-ubuntu22.04-zen2
            ^libidn2@2.3.4%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
                ^libunistring@1.1%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
            ^libtool@2.4.7%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
            ^m4@1.4.19%gcc@11.3.0+sigsegv build_system=autotools patches=9dc5fbd,bfdffa7 arch=linux-ubuntu22.04-zen2
                ^libsigsegv@2.13%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
            ^openssh@9.1p1%gcc@11.3.0+gssapi build_system=autotools arch=linux-ubuntu22.04-zen2
                ^krb5@1.20.1%gcc@11.3.0+shared build_system=autotools arch=linux-ubuntu22.04-zen2
                    ^bison@3.8.2%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
                ^libedit@3.1-20210216%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
            ^pcre2@10.42%gcc@11.3.0~jit+multibyte build_system=autotools arch=linux-ubuntu22.04-zen2
            ^perl@5.34.0%gcc@11.3.0~cpanm+open+shared+threads build_system=generic arch=linux-ubuntu22.04-zen2
        ^openssl@1.1.1s%gcc@11.3.0~docs~shared build_system=generic certs=mozilla arch=linux-ubuntu22.04-zen2
            ^ca-certificates-mozilla@2023-01-10%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-zen2
        ^py-cffi@1.15.1%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
            ^py-pycparser@2.21%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
        ^py-setuptools-rust@1.5.1%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
            ^py-semantic-version@2.10.0%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
        ^rust@1.61.0%gcc@11.3.0+analysis+clippy~rls+rustfmt+src build_system=generic extra_targets=none arch=linux-ubuntu22.04-zen2
    ^py-msal@1.20.0%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
        ^py-pyjwt@2.4.0%gcc@11.3.0+crypto build_system=python_pip arch=linux-ubuntu22.04-zen2
    ^py-msal-extensions@1.0.0%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
        ^py-portalocker@1.6.0%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
    ^py-pip@22.2.2%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-zen2
    ^py-setuptools@63.0.0%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-zen2
    ^py-six@1.16.0%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
    ^py-wheel@0.37.1%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-zen2
    ^python@3.10.8%gcc@11.3.0+bz2+crypt+ctypes+dbm~debug+libxml2+lzma~nis~optimizations+pic+pyexpat+pythoncmd+readline+shared+sqlite3+ssl~tkinter+uuid+zlib build_system=generic patches=0d98e93,7d40923,f2fd060 arch=linux-ubuntu22.04-zen2
        ^bzip2@1.0.8%gcc@11.3.0~debug~pic+shared build_system=generic arch=linux-ubuntu22.04-zen2
            ^diffutils@3.8%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^expat@2.5.0%gcc@11.3.0+libbsd build_system=autotools arch=linux-ubuntu22.04-zen2
            ^libbsd@0.11.7%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
                ^libmd@1.0.4%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^gdbm@1.23%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^gettext@0.21.1%gcc@11.3.0+bzip2+curses+git~libunistring+libxml2+tar+xz build_system=autotools arch=linux-ubuntu22.04-zen2
            ^libxml2@2.10.3%gcc@11.3.0~python build_system=autotools arch=linux-ubuntu22.04-zen2
            ^tar@1.34%gcc@11.3.0 build_system=autotools zip=pigz arch=linux-ubuntu22.04-zen2
                ^pigz@2.7%gcc@11.3.0 build_system=makefile arch=linux-ubuntu22.04-zen2
                ^zstd@1.5.2%gcc@11.3.0+programs build_system=makefile compression=none libs=shared,static arch=linux-ubuntu22.04-zen2
        ^libffi@3.4.4%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^libxcrypt@4.4.33%gcc@11.3.0~obsolete_api build_system=autotools arch=linux-ubuntu22.04-zen2
        ^ncurses@6.4%gcc@11.3.0~symlinks+termlib abi=none build_system=autotools arch=linux-ubuntu22.04-zen2
        ^pkgconf@1.8.0%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^readline@8.2%gcc@11.3.0 build_system=autotools patches=bbf97f1 arch=linux-ubuntu22.04-zen2
        ^sqlite@3.40.1%gcc@11.3.0+column_metadata+dynamic_extensions+fts~functions+rtree build_system=autotools arch=linux-ubuntu22.04-zen2
        ^util-linux-uuid@2.38.1%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^xz@5.4.1%gcc@11.3.0~pic build_system=autotools libs=shared,static arch=linux-ubuntu22.04-zen2
        ^zlib@1.2.13%gcc@11.3.0+optimize+pic+shared build_system=makefile arch=linux-ubuntu22.04-zen2

Input spec
--------------------------------
py-tqdm

Concretized
--------------------------------
py-tqdm@4.64.1%gcc@11.3.0~notebook~telegram build_system=python_pip arch=linux-ubuntu22.04-zen2
    ^py-pip@22.2.2%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-zen2
    ^py-setuptools@63.0.0%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-zen2
    ^py-setuptools-scm@7.0.5%gcc@11.3.0+toml build_system=python_pip arch=linux-ubuntu22.04-zen2
        ^py-packaging@23.0%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
            ^py-flit-core@3.7.1%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
        ^py-tomli@2.0.1%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
        ^py-typing-extensions@4.3.0%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
    ^py-wheel@0.37.1%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-zen2
    ^python@3.10.8%gcc@11.3.0+bz2+crypt+ctypes+dbm~debug+libxml2+lzma~nis~optimizations+pic+pyexpat+pythoncmd+readline+shared+sqlite3+ssl~tkinter+uuid+zlib build_system=generic patches=0d98e93,7d40923,f2fd060 arch=linux-ubuntu22.04-zen2
        ^bzip2@1.0.8%gcc@11.3.0~debug~pic+shared build_system=generic arch=linux-ubuntu22.04-zen2
            ^diffutils@3.8%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^expat@2.5.0%gcc@11.3.0+libbsd build_system=autotools arch=linux-ubuntu22.04-zen2
            ^libbsd@0.11.7%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
                ^libmd@1.0.4%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^gdbm@1.23%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^gettext@0.21.1%gcc@11.3.0+bzip2+curses+git~libunistring+libxml2+tar+xz build_system=autotools arch=linux-ubuntu22.04-zen2
            ^libiconv@1.17%gcc@11.3.0 build_system=autotools libs=shared,static arch=linux-ubuntu22.04-zen2
            ^libxml2@2.10.3%gcc@11.3.0~python build_system=autotools arch=linux-ubuntu22.04-zen2
            ^tar@1.34%gcc@11.3.0 build_system=autotools zip=pigz arch=linux-ubuntu22.04-zen2
                ^pigz@2.7%gcc@11.3.0 build_system=makefile arch=linux-ubuntu22.04-zen2
                ^zstd@1.5.2%gcc@11.3.0+programs build_system=makefile compression=none libs=shared,static arch=linux-ubuntu22.04-zen2
        ^libffi@3.4.4%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^libxcrypt@4.4.33%gcc@11.3.0~obsolete_api build_system=autotools arch=linux-ubuntu22.04-zen2
            ^perl@5.34.0%gcc@11.3.0~cpanm+open+shared+threads build_system=generic arch=linux-ubuntu22.04-zen2
        ^ncurses@6.4%gcc@11.3.0~symlinks+termlib abi=none build_system=autotools arch=linux-ubuntu22.04-zen2
        ^openssl@1.1.1s%gcc@11.3.0~docs~shared build_system=generic certs=mozilla arch=linux-ubuntu22.04-zen2
            ^ca-certificates-mozilla@2023-01-10%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-zen2
        ^pkgconf@1.8.0%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^readline@8.2%gcc@11.3.0 build_system=autotools patches=bbf97f1 arch=linux-ubuntu22.04-zen2
        ^sqlite@3.40.1%gcc@11.3.0+column_metadata+dynamic_extensions+fts~functions+rtree build_system=autotools arch=linux-ubuntu22.04-zen2
        ^util-linux-uuid@2.38.1%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^xz@5.4.1%gcc@11.3.0~pic build_system=autotools libs=shared,static arch=linux-ubuntu22.04-zen2
        ^zlib@1.2.13%gcc@11.3.0+optimize+pic+shared build_system=makefile arch=linux-ubuntu22.04-zen2

Input spec
--------------------------------
py-matplotlib

Concretized
--------------------------------
py-matplotlib@3.6.3%gcc@11.3.0~animation~fonts~latex~movies backend=agg build_system=python_pip arch=linux-ubuntu22.04-zen2
    ^freetype@2.11.1%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^bzip2@1.0.8%gcc@11.3.0~debug~pic+shared build_system=generic arch=linux-ubuntu22.04-zen2
            ^diffutils@3.8%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
    ^libpng@1.6.37%gcc@11.3.0 build_system=autotools libs=shared,static arch=linux-ubuntu22.04-zen2
        ^zlib@1.2.13%gcc@11.3.0+optimize+pic+shared build_system=makefile arch=linux-ubuntu22.04-zen2
    ^pkgconf@1.8.0%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
    ^py-certifi@2022.9.14%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
    ^py-contourpy@1.0.5%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
        ^py-build@0.7.0%gcc@11.3.0~virtualenv build_system=python_pip patches=9a151ac arch=linux-ubuntu22.04-zen2
            ^py-pep517@0.12.0%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
        ^py-pybind11@2.10.1%gcc@11.3.0~ipo build_system=cmake build_type=RelWithDebInfo arch=linux-ubuntu22.04-zen2
            ^ninja@1.11.1%gcc@11.3.0+re2c build_system=generic arch=linux-ubuntu22.04-zen2
                ^re2c@2.2%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-zen2
    ^py-cycler@0.11.0%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
    ^py-fonttools@4.37.3%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
    ^py-kiwisolver@1.4.4%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
        ^py-cppy@1.2.1%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
    ^py-numpy@1.24.2%gcc@11.3.0+blas+lapack build_system=python_pip patches=873745d arch=linux-ubuntu22.04-zen2
        ^openblas@0.3.21%gcc@11.3.0~bignuma~consistent_fpcsr+fortran~ilp64+locking+pic+shared build_system=makefile patches=d3d9b15 symbol_suffix=none threads=none arch=linux-ubuntu22.04-zen2
            ^perl@5.34.0%gcc@11.3.0~cpanm+open+shared+threads build_system=generic arch=linux-ubuntu22.04-zen2
        ^py-cython@0.29.32%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
    ^py-packaging@23.0%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
        ^py-flit-core@3.7.1%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
    ^py-pillow@9.2.0%gcc@11.3.0~freetype~imagequant+jpeg~jpeg2000~lcms~raqm~tiff~webp~xcb+zlib build_system=python_pip arch=linux-ubuntu22.04-zen2
        ^libjpeg-turbo@2.1.4%gcc@11.3.0~ipo~jpeg8+shared+static build_system=cmake build_type=RelWithDebInfo arch=linux-ubuntu22.04-zen2
            ^nasm@2.15.05%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
    ^py-pip@22.2.2%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-zen2
    ^py-pyparsing@3.0.9%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
    ^py-python-dateutil@2.8.2%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
        ^py-six@1.16.0%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
    ^py-setuptools@63.0.0%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-zen2
    ^py-setuptools-scm@7.0.5%gcc@11.3.0+toml build_system=python_pip arch=linux-ubuntu22.04-zen2
        ^py-tomli@2.0.1%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
        ^py-typing-extensions@4.3.0%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
    ^py-wheel@0.37.1%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-zen2
    ^python@3.10.8%gcc@11.3.0+bz2+crypt+ctypes+dbm~debug+libxml2+lzma~nis~optimizations+pic+pyexpat+pythoncmd+readline+shared+sqlite3+ssl~tkinter+uuid+zlib build_system=generic patches=0d98e93,7d40923,f2fd060 arch=linux-ubuntu22.04-zen2
        ^expat@2.5.0%gcc@11.3.0+libbsd build_system=autotools arch=linux-ubuntu22.04-zen2
            ^libbsd@0.11.7%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
                ^libmd@1.0.4%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^gdbm@1.23%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^gettext@0.21.1%gcc@11.3.0+bzip2+curses+git~libunistring+libxml2+tar+xz build_system=autotools arch=linux-ubuntu22.04-zen2
            ^libiconv@1.17%gcc@11.3.0 build_system=autotools libs=shared,static arch=linux-ubuntu22.04-zen2
            ^libxml2@2.10.3%gcc@11.3.0~python build_system=autotools arch=linux-ubuntu22.04-zen2
            ^tar@1.34%gcc@11.3.0 build_system=autotools zip=pigz arch=linux-ubuntu22.04-zen2
                ^pigz@2.7%gcc@11.3.0 build_system=makefile arch=linux-ubuntu22.04-zen2
                ^zstd@1.5.2%gcc@11.3.0+programs build_system=makefile compression=none libs=shared,static arch=linux-ubuntu22.04-zen2
        ^libffi@3.4.4%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^libxcrypt@4.4.33%gcc@11.3.0~obsolete_api build_system=autotools arch=linux-ubuntu22.04-zen2
        ^ncurses@6.4%gcc@11.3.0~symlinks+termlib abi=none build_system=autotools arch=linux-ubuntu22.04-zen2
        ^openssl@1.1.1s%gcc@11.3.0~docs~shared build_system=generic certs=mozilla arch=linux-ubuntu22.04-zen2
            ^ca-certificates-mozilla@2023-01-10%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-zen2
        ^readline@8.2%gcc@11.3.0 build_system=autotools patches=bbf97f1 arch=linux-ubuntu22.04-zen2
        ^sqlite@3.40.1%gcc@11.3.0+column_metadata+dynamic_extensions+fts~functions+rtree build_system=autotools arch=linux-ubuntu22.04-zen2
        ^util-linux-uuid@2.38.1%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^xz@5.4.1%gcc@11.3.0~pic build_system=autotools libs=shared,static arch=linux-ubuntu22.04-zen2
    ^qhull@2020.2%gcc@11.3.0~ipo build_system=cmake build_type=RelWithDebInfo arch=linux-ubuntu22.04-zen2
        ^cmake@3.22.1%gcc@11.3.0~doc+ncurses+ownlibs~qt build_system=generic build_type=Release arch=linux-ubuntu22.04-zen2

Input spec
--------------------------------
py-pip

Concretized
--------------------------------
py-pip@22.2.2%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-zen2
    ^python@3.10.8%gcc@11.3.0+bz2+crypt+ctypes+dbm~debug+libxml2+lzma~nis~optimizations+pic+pyexpat+pythoncmd+readline+shared+sqlite3+ssl~tkinter+uuid+zlib build_system=generic patches=0d98e93,7d40923,f2fd060 arch=linux-ubuntu22.04-zen2
        ^bzip2@1.0.8%gcc@11.3.0~debug~pic+shared build_system=generic arch=linux-ubuntu22.04-zen2
            ^diffutils@3.8%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^expat@2.5.0%gcc@11.3.0+libbsd build_system=autotools arch=linux-ubuntu22.04-zen2
            ^libbsd@0.11.7%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
                ^libmd@1.0.4%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^gdbm@1.23%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^gettext@0.21.1%gcc@11.3.0+bzip2+curses+git~libunistring+libxml2+tar+xz build_system=autotools arch=linux-ubuntu22.04-zen2
            ^libiconv@1.17%gcc@11.3.0 build_system=autotools libs=shared,static arch=linux-ubuntu22.04-zen2
            ^libxml2@2.10.3%gcc@11.3.0~python build_system=autotools arch=linux-ubuntu22.04-zen2
            ^tar@1.34%gcc@11.3.0 build_system=autotools zip=pigz arch=linux-ubuntu22.04-zen2
                ^pigz@2.7%gcc@11.3.0 build_system=makefile arch=linux-ubuntu22.04-zen2
                ^zstd@1.5.2%gcc@11.3.0+programs build_system=makefile compression=none libs=shared,static arch=linux-ubuntu22.04-zen2
        ^libffi@3.4.4%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^libxcrypt@4.4.33%gcc@11.3.0~obsolete_api build_system=autotools arch=linux-ubuntu22.04-zen2
            ^perl@5.34.0%gcc@11.3.0~cpanm+open+shared+threads build_system=generic arch=linux-ubuntu22.04-zen2
        ^ncurses@6.4%gcc@11.3.0~symlinks+termlib abi=none build_system=autotools arch=linux-ubuntu22.04-zen2
        ^openssl@1.1.1s%gcc@11.3.0~docs~shared build_system=generic certs=mozilla arch=linux-ubuntu22.04-zen2
            ^ca-certificates-mozilla@2023-01-10%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-zen2
        ^pkgconf@1.8.0%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^readline@8.2%gcc@11.3.0 build_system=autotools patches=bbf97f1 arch=linux-ubuntu22.04-zen2
        ^sqlite@3.40.1%gcc@11.3.0+column_metadata+dynamic_extensions+fts~functions+rtree build_system=autotools arch=linux-ubuntu22.04-zen2
        ^util-linux-uuid@2.38.1%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^xz@5.4.1%gcc@11.3.0~pic build_system=autotools libs=shared,static arch=linux-ubuntu22.04-zen2
        ^zlib@1.2.13%gcc@11.3.0+optimize+pic+shared build_system=makefile arch=linux-ubuntu22.04-zen2

Input spec
--------------------------------
py-domonic

Concretized
--------------------------------
py-domonic@0.9.11%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
    ^py-cssselect@1.1.0%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
    ^py-elementpath@2.5.3%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
    ^py-html5lib@1.1%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
        ^py-six@1.16.0%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
        ^py-webencodings@0.5.1%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
    ^py-pip@22.2.2%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-zen2
    ^py-python-dateutil@2.8.2%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
        ^py-setuptools-scm@7.0.5%gcc@11.3.0+toml build_system=python_pip arch=linux-ubuntu22.04-zen2
            ^py-packaging@23.0%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
            ^py-tomli@2.0.1%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
            ^py-typing-extensions@4.3.0%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
    ^py-requests@2.28.1%gcc@11.3.0~socks build_system=python_pip arch=linux-ubuntu22.04-zen2
        ^py-certifi@2022.9.14%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
        ^py-charset-normalizer@2.0.12%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
        ^py-idna@3.4%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
            ^py-flit-core@3.7.1%gcc@11.3.0 build_system=python_pip arch=linux-ubuntu22.04-zen2
    ^py-setuptools@63.0.0%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-zen2
    ^py-urllib3@1.26.12%gcc@11.3.0~brotli~secure~socks build_system=python_pip arch=linux-ubuntu22.04-zen2
    ^py-wheel@0.37.1%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-zen2
    ^python@3.10.8%gcc@11.3.0+bz2+crypt+ctypes+dbm~debug+libxml2+lzma~nis~optimizations+pic+pyexpat+pythoncmd+readline+shared+sqlite3+ssl~tkinter+uuid+zlib build_system=generic patches=0d98e93,7d40923,f2fd060 arch=linux-ubuntu22.04-zen2
        ^bzip2@1.0.8%gcc@11.3.0~debug~pic+shared build_system=generic arch=linux-ubuntu22.04-zen2
            ^diffutils@3.8%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^expat@2.5.0%gcc@11.3.0+libbsd build_system=autotools arch=linux-ubuntu22.04-zen2
            ^libbsd@0.11.7%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
                ^libmd@1.0.4%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^gdbm@1.23%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^gettext@0.21.1%gcc@11.3.0+bzip2+curses+git~libunistring+libxml2+tar+xz build_system=autotools arch=linux-ubuntu22.04-zen2
            ^libiconv@1.17%gcc@11.3.0 build_system=autotools libs=shared,static arch=linux-ubuntu22.04-zen2
            ^libxml2@2.10.3%gcc@11.3.0~python build_system=autotools arch=linux-ubuntu22.04-zen2
            ^tar@1.34%gcc@11.3.0 build_system=autotools zip=pigz arch=linux-ubuntu22.04-zen2
                ^pigz@2.7%gcc@11.3.0 build_system=makefile arch=linux-ubuntu22.04-zen2
                ^zstd@1.5.2%gcc@11.3.0+programs build_system=makefile compression=none libs=shared,static arch=linux-ubuntu22.04-zen2
        ^libffi@3.4.4%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^libxcrypt@4.4.33%gcc@11.3.0~obsolete_api build_system=autotools arch=linux-ubuntu22.04-zen2
            ^perl@5.34.0%gcc@11.3.0~cpanm+open+shared+threads build_system=generic arch=linux-ubuntu22.04-zen2
        ^ncurses@6.4%gcc@11.3.0~symlinks+termlib abi=none build_system=autotools arch=linux-ubuntu22.04-zen2
        ^openssl@1.1.1s%gcc@11.3.0~docs~shared build_system=generic certs=mozilla arch=linux-ubuntu22.04-zen2
            ^ca-certificates-mozilla@2023-01-10%gcc@11.3.0 build_system=generic arch=linux-ubuntu22.04-zen2
        ^pkgconf@1.8.0%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^readline@8.2%gcc@11.3.0 build_system=autotools patches=bbf97f1 arch=linux-ubuntu22.04-zen2
        ^sqlite@3.40.1%gcc@11.3.0+column_metadata+dynamic_extensions+fts~functions+rtree build_system=autotools arch=linux-ubuntu22.04-zen2
        ^util-linux-uuid@2.38.1%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-zen2
        ^xz@5.4.1%gcc@11.3.0~pic build_system=autotools libs=shared,static arch=linux-ubuntu22.04-zen2
        ^zlib@1.2.13%gcc@11.3.0+optimize+pic+shared build_system=makefile arch=linux-ubuntu22.04-zen2

