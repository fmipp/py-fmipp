# manylinux2014 (glibc 2.17) image with static SUNDIALS 3.1.2 and Boost 1.72.
# The default base is x86_64. For aarch64 pass:
#   --build-arg BASE_IMAGE=quay.io/pypa/manylinux2014_aarch64

ARG BASE_IMAGE=quay.io/pypa/manylinux2014_x86_64
FROM ${BASE_IMAGE}

ENV SUNDIALS_ROOT=/opt/sundials-3.1.2 \
    BOOST_ROOT=/opt/boost-1.72

RUN yum install -y pcre-devel unzip cmake3 \
    && ln -sfn /usr/bin/cmake3 /usr/local/bin/cmake \
    && yum clean all

# SWIG 4.0.2 matches the Windows builds. The CentOS 7 package is too old.
RUN curl -fsSL -o /tmp/swig.tar.gz https://sourceforge.net/projects/swig/files/swig/swig-4.0.2/swig-4.0.2.tar.gz/download \
    && tar -xzf /tmp/swig.tar.gz -C /tmp \
    && cd /tmp/swig-4.0.2 \
    && ./configure --prefix=/usr/local \
    && make -j"$(nproc)" \
    && make install \
    && rm -rf /tmp/swig-4.0.2 /tmp/swig.tar.gz \
    && swig -version

# Boost.Filesystem and Boost.System as PIC static libraries. ODEINT is header-only.
RUN curl -fsSL -o /tmp/boost.tar.gz https://archives.boost.io/release/1.72.0/source/boost_1_72_0.tar.gz \
    && tar -xzf /tmp/boost.tar.gz -C /tmp \
    && cd /tmp/boost_1_72_0 \
    && ./bootstrap.sh --with-libraries=filesystem,system \
    && ./b2 -j"$(nproc)" cxxflags="-fPIC -std=c++11" cflags="-fPIC" link=static runtime-link=shared threading=multi --layout=system --prefix=/opt/boost-1.72 --libdir=/opt/boost-1.72/lib install \
    && rm -rf /tmp/boost_1_72_0 /tmp/boost.tar.gz

# SUNDIALS 3.1.2 static libraries, position-independent so they can be linked into the extensions.
RUN curl -fsSL -o /tmp/sundials.tar.gz https://github.com/LLNL/sundials/releases/download/v3.1.2/sundials-3.1.2.tar.gz \
    && tar -xzf /tmp/sundials.tar.gz -C /tmp \
    && cmake -S /tmp/sundials-3.1.2 -B /tmp/sundials-build \
        -DCMAKE_BUILD_TYPE=Release \
        -DCMAKE_INSTALL_PREFIX=/opt/sundials-3.1.2 \
        -DCMAKE_INSTALL_LIBDIR=lib \
        -DCMAKE_POSITION_INDEPENDENT_CODE=ON \
        -DBUILD_SHARED_LIBS=OFF \
        -DBUILD_STATIC_LIBS=ON \
        -DEXAMPLES_ENABLE=OFF \
        -DEXAMPLES_ENABLE_C=OFF \
        -DEXAMPLES_ENABLE_CXX=OFF \
        -DEXAMPLES_INSTALL=OFF \
        -DBUILD_CVODES=OFF \
        -DBUILD_IDA=OFF \
        -DBUILD_IDAS=OFF \
        -DBUILD_KINSOL=OFF \
    && cmake --build /tmp/sundials-build --parallel "$(nproc)" \
    && cmake --install /tmp/sundials-build \
    && rm -rf /tmp/sundials-3.1.2 /tmp/sundials-build /tmp/sundials.tar.gz

ENTRYPOINT ["/bin/bash", "/io/py-fmipp/release/manylinux/build_wheels.sh"]
