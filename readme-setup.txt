----------------1. Windows: building wheels----------------
NOTE: By default this build works only on WINDOWS due to setup.py platform settings

-------- building requirements for python--------

-  install "wheel" and "setuptools" via pip

--------preparing the code--------

-  run the fmipp source code with cmake to build the libraries

-  copy the libraries accordingly to the README.txt files or as below:
    -  <cmake-folder>/import/swig/fmippim.py              ->  <fmipp-folder>/fmipp/fmippim.py
    -  <cmake-folder>/export/swig/fmippex.py              ->  <fmipp-folder>/fmipp/export/fmippex.py
    -  <cmake-folder>/import/swig/Release/_fmippim.pyd    ->  <fmipp-folder>/fmipp/lib/_fmippim.pyd
    -  <cmake-folder>/import/swig/Release/_fmippex.pyd    ->  <fmipp-folder>/fmipp/lib/_fmippex.pyd
    -  <cmake-folder>/Release/fmippim.dll                 ->  <fmipp-folder>/lib/fmippim.dll
    -  <cmake-folder>/Release/fmippex.dll                 ->  <fmipp-folder>/lib/fmippex.dll
    -  <cmake-folder>/Release/fmi2.dll                    ->  <fmipp-folder>/export/bin/fmi2.dll
    -  <cmake-folder>/Release/libfmipp_fmu_frontend.lib   ->  <fmipp-folder>/export/bin/libfmipp_fmu_frontend.lib
    -  <sundials-directory>/sundials_cvode.lib            ->  <fmipp-folder>/lib/sundials_cvode.lib
    -  <sundials-directory>/sundials_nvecserial.lib       ->  <fmipp-folder>/lib/sundials_nvecserial.lib
    -  <boost-directory>/boost_filesystem-<version>.lib   ->  <fmipp-folder>/lib/boost_filesystem-<version>.lib
    -  <boost-directory>/boost_system-<version>.lib       ->  <fmipp-folder>/lib/boost_system-<version>.lib

    -  NOTE: the build-win.py file can be used IF adapted accordingly

-  run "setup.py bdist_wheel --python-tag py<X.Y> -p <platform_tag>" in the command line, where:
    - <X.Y> is the python version used (i.e. "3.6")
    - <platform_tag> refers to the platform used (i.e. "win32" or "win_amd64")


-------- Installation --------

-  run "python -m pip install \path\to\wheel\fmipp-<version>-<pyX.Y>-none-<platform-tag>.whl" to install the wheel, 
    -  it might be nescessary to set the flag "--prefer-binaries" if pip chooses to install not a wheel but source distribution as default
    -  to redownload the package instead of using a cached version, set the flag "--no-cache-dir"

-  alternatively: use "python -m pip install fmipp" to install the wheel from the Python Package Index  





----------------2. Linux: creating source distribution----------------
NOTE: By default this build works only on LINUX due to setup.py platform settings

-------- requirements --------

-  make sure to have installed (i.e. via aptitude):
    -  python (python-dev) (recommended: version 3.5 (or higher))
    -  swig (swig)
    -  sundials (libsundials-serial-dev)
    -  BOOST (libboost-all-dev)
    -  pip (python-pip)
    -  git (git)

-  download the fmipp source code into ".\source\"


-------- generating the source distribution--------

-  run "python setup.py sdist" in the command line to create the "fmipp-<version>.tar.gz" source distribution file

-------- Installation --------

-  run "python -m pip install \path\to\sdist\fmipp-<version>.tar.gz" to install the source distribution

-  alternatively: use "python -m pip install fmipp" to install the source distribution from the Python Package Index


