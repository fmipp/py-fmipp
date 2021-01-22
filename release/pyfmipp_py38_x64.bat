@ECHO OFF

REM ##################################################################################################
REM Settings.
REM ##################################################################################################

REM Setting specific to this wheel.
SET BUILD_DIR=%~dp0\build_py38_x64
SET CMAKE_TARGET="Visual Studio 16 2019"
SET SUNDIALS_LIBRARY_DIR=C:\Tools\sundials-2.6.0\lib64-msvc-14.2
SET BOOST_LIBRARY_DIR=C:\Tools\boost_1_72_0\lib64-msvc-14.2
SET BOOST_VERSION=vc142-mt-x64-1_72
SET PYTHON_DIR=C:\Python38_x64
SET PYTHON_TAG=cp38
SET PLATFORM_TAG=win_amd64

REM General settings.
SET CMAKE_BIN_DIR=C:\Tools\CMake\bin
SET PY_FMIPP_DIR=C:\Development\fmipp-dev\py-fmipp
SET FMIPP_DIR=C:\Development\fmipp-dev\fmipp
SET SWIG_DIR=C:\Tools\swigwin-3.0.12
SET BOOST_INCLUDE_DIR=C:\Tools\boost_1_72_0
SET SUNDIALS_INCLUDE_DIR=C:\Tools\sundials-2.6.0\include

CALL %PY_FMIPP_DIR%\release\build_vc142.bat