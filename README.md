Building wheels for Windows
===========================

NOTE: By default, this works only on Windows due to platform settings in file *setup.py*.

Requirements for Python
-----------------------

* install packages `wheel` and `setuptools` using pip:
```
        pip install wheel setuptools
```


Building the wheel
------------------

* build the FMI++ library (using CMake and Visual Studio)

* copy the libraries accordingly to the README.txt files or as below:
  * *\<fmipp-build-dir\>\export\swig\fmippex.py* : copy to  *\<py-fmipp-dir\>\fmipp\export*
  * *\<fmipp-build-dir\>\import\swig\fmippim.py* : copy to *\<py-fmipp-dir\>\fmipp*
  * *\<fmipp-build-dir\>\import\swig\Release\_fmippim.pyd* : copy to  *\<py-fmipp-dir\>\fmipp\lib*
  * *\<fmipp-build-dir\>\import\swig\Release\_fmippex.pyd* : copy to  *\<py-fmipp-dir\>\fmipp\lib*
  * *\<fmipp-build-dir\>\Release\fmippim.dll* : copy to  *\<py-fmipp-dir\>\fmipp\lib*
  * *\<fmipp-build-dir\>\Release\fmippex.dll* : copy to  *\<py-fmipp-dir\>\fmipp\lib*
  * *\<fmipp-build-dir\>\Release\fmi2.dll* : copy to  *\<py-fmipp-dir\>\fmipp\export\bin*
  * *\<fmipp-build-dir\>\Release\libfmipp_fmu_frontend.lib* : copy to  *\<py-fmipp-dir\>\fmipp\export\bin*
  * *\<sundials-lib-dir\>\sundials_cvode.dll* : copy to  *\<py-fmipp-dir\>\fmipp\lib*
  * *\<sundials-lib-dir\>\sundials_nvecserial.dll* : copy to  *\<py-fmipp-dir\>\fmipp\lib*
  * *\<boost-lib-dir\>\boost_filesystem-<version>.dll* : copy to  *\<py-fmipp-dir\>\fmipp\lib*
  * *\<boost-lib-dir\>\boost_system-<version>.dll* : copy to  *\<py-fmipp-dir\>\fmipp\lib*
  * MSVC runtime libraries (e.g., *msvcp140.dll* & *vcruntime.dll*) : copy to  *\<py-fmipp-dir\>\fmipp\lib*

* run `python setup.py bdist_wheel --python-tag <python_tag> -p <platform_tag>` in the command line, where:
  * `<python_tag>` is the python version used (e.g. `cp37`)
  * `<platform_tag>` refers to the platform used (i.e. `win32` or `win_amd64`)

**NOTE**: There are batch scripts available in subfolder *release* for automating the build for several configurations (win32/win_amd64, cp27/cp36/cp37).
  
Installation from local
-----------------------

* run `pip install path\to\wheel\fmipp-<version>-<python_tag>-none-<platform_tag>.whl` to install the wheel



Creating source distribution packages for Linux
===============================================

NOTE: By default, this works only on Linux due to platform settings in file *setup.py*.

Requirements
------------

* make sure to have installed (e.g. via `apt-get` or `aptitude`):
  * Python (package *python-dev*)
  * pip (package *python-pip*)
  * git (package *git*)
* install package `setuptools` using `pip`
```
        pip install setuptools
```
* download the FMI++ source code into subfolder *source* (*./source/fmipp*) using `git`
```
        git clone https://git.code.sf.net/p/fmipp/code fmipp
```



Generating the source distribution package
------------------------------------------

* run `python setup.py sdist` in the command line to create the *fmipp-\<version\>.tar.gz* source distribution file


Installation from local
-----------------------

* make sure to have installed (e.g. via `apt-get` or `aptitude`):
  * SWIG (package *swig*)
  * SUNDIALS (package *libsundials-serial-dev*)
  * Boost (package *libboost-all-dev*)
* run `pip install /path/to/sdist/fmipp-<version>.tar.gz` to install the source distribution



Uploading to PyPI
=================

* install twine via `pip install twine`
* run `twine upload dist\*`



Installation from PyPI
======================

Windows
-------

* run `pip install fmipp --prefer-binaries`
* to re-download the package instead of using a cached version, set the flag `--no-cache-dir`


Linux
-----

* Requirements: make sure to have installed (e.g. via `apt-get` or `aptitude`):
  * Python (package *python-dev*)
  * SWIG (package *swig*)
  * SUNDIALS (package *libsundials-serial-dev*)
  * Boost (package *libboost-all-dev*)
  * pip (package *python-pip*)
* run `pip install fmipp`
