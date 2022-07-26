Installation
============

Installation on Windows
-----------------------

Use ``pip`` to install the FMI++ Python Interface as pre-compiled binary package (Python wheel)

.. code::

   pip install fmipp --prefer-binary

``--prefer-binary`` should guarantee that binary distributions (wheels) are chosen over source distributions for the installation.
Alternatively ``--only-binary :all:`` can be used instead to force installing from binary distribution.

Installation on Linux (Ubuntu 20.04)
------------------------------------

Make sure to have installed the following prerequisites(e.g. via ``apt``, see package names in brackets below):

  * python (python3) (recommended: version 3.7 or higher)
  * pip (python3-pip)
  * distutils (python3-setuptools)
  * GCC compiler toolchain (build-essential)
  * swig (swig)
  * SUNDIALS library (libsundials-dev)
  * Boost library (libboost-all-dev)

Use ``pip`` to install the FMI++ Python Interface via source distribution

.. code::

   python3 -m pip install fmipp