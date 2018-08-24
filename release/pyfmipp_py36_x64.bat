@ECHO OFF

REM ##################################################################################################
REM Settings.
REM ##################################################################################################

REM Setting specific to this wheel.
SET BUILD_DIR=C:\Production\build_py36_x64
SET CMAKE_TARGET="Visual Studio 14 2015 Win64"
SET SUNDIALS_LIBRARY_DIR=C:\Tools\sundials-2.5.0\lib64-msvc-14.0
SET BOOST_LIBRARY_DIR=C:\Tools\boost_1_68_0\lib64-msvc-14.0
SET BOOST_VERSION=vc140-mt-x64-1_68
SET PYTHON_DIR=C:\Python36-x64
SET PYTHON_TAG=cp36
SET PLATFORM_TAG=win_amd64

REM General settings.
SET CMAKE_BIN_DIR="C:\Program Files\CMake\bin"
SET PY_FMIPP_DIR=C:\Production\py-fmipp
SET FMIPP_DIR=%PY_FMIPP_DIR%\source\fmipp
SET SWIG_DIR=C:\Tools\swigwin-3.0.12
SET BOOST_INCLUDE_DIR=C:\Tools\boost_1_68_0
SET SUNDIALS_INCLUDE_DIR=C:\Tools\sundials-2.5.0\include

CALL %PY_FMIPP_DIR%\release\build_vc140.bat