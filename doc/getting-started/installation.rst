Installation
============

Installation on Windows
-----------------------

Use ``pip`` to install the FMI++ Python Interface as pre-compiled binary package (Python wheel)

.. code::

   pip install fmipp --prefer-binary

``--prefer-binary`` should guarantee that binary distributions (wheels) are chosen over source distributions for the installation.
Alternatively ``--only-binary :all:`` can be used instead to force installing from binary distribution.

Installation on Linux
---------------------

Pre-built wheels target manylinux2014 (glibc 2.17) and run on Ubuntu 20.04 and later, Debian 10 and later, and RHEL 7 and later. SUNDIALS 3.1.2 and Boost are linked into the wheel, so ``libsundials-dev`` and ``libboost-all-dev`` are not required:

.. code::

   python3 -m pip install fmipp

To build those wheels, from the repository root (Docker required; the FMI++ sources are the sibling directory ``fmipp``):

.. code::

   docker build -f py-fmipp/release/manylinux/Dockerfile -t fmipp-manylinux py-fmipp/release/manylinux
   docker run --rm -v "<repo-root>:/io" fmipp-manylinux

Wheels are written to ``py-fmipp/dist``. For aarch64, pass ``--build-arg BASE_IMAGE=quay.io/pypa/manylinux2014_aarch64``.

A source install still needs a compiler and the following packages (Ubuntu package names in brackets). SUNDIALS must be version 3.1.2, which current Ubuntu releases do not ship:

  * python (python3) (recommended: version 3.10 or higher)
  * pip (python3-pip)
  * setuptools (python3-setuptools)
  * GCC compiler toolchain (build-essential)
  * swig (swig)
  * SUNDIALS library (libsundials-dev, version 3.1.2)
  * Boost library (libboost-all-dev)

.. code::

   python3 -m pip install fmipp