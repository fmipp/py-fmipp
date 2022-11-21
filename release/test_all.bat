@ECHO OFF

SETLOCAL

REM General settings.
SET PY_FMIPP_DIR=C:\Development\fmipp-dev\py-fmipp
SET PY_FMIPP_VERSION=2.0.2

REM Run tests for all versions.

SET PWD=%CD%
CD %PY_FMIPP_DIR%\test

ECHO ###### Python37-x64 ######
ECHO y | C:\Python37-x64\Scripts\pip.exe uninstall fmipp
C:\Python37-x64\Scripts\pip.exe install %PY_FMIPP_DIR%\dist\fmipp-%PY_FMIPP_VERSION%-cp37-none-win_amd64.whl
C:\Python37-x64\Scripts\pytest.exe %PY_FMIPP_DIR%\test\test_pyfmipp.py

ECHO ###### Python38-x64 ######
ECHO y | C:\Python38-x64\Scripts\pip.exe uninstall fmipp
C:\Python38-x64\Scripts\pip.exe install %PY_FMIPP_DIR%\dist\fmipp-%PY_FMIPP_VERSION%-cp38-none-win_amd64.whl
C:\Python38-x64\Scripts\pytest.exe %PY_FMIPP_DIR%\test\test_pyfmipp.py

ECHO ###### Python39-x64 ######
ECHO y | C:\Python39-x64\Scripts\pip.exe uninstall fmipp
C:\Python39-x64\Scripts\pip.exe install %PY_FMIPP_DIR%\dist\fmipp-%PY_FMIPP_VERSION%-cp39-none-win_amd64.whl
C:\Python39-x64\Scripts\pytest.exe %PY_FMIPP_DIR%\test\test_pyfmipp.py

ECHO ###### Python310-x64 ######
ECHO y | C:\Python310-x64\Scripts\pip.exe uninstall fmipp
C:\Python310-x64\Scripts\pip.exe install %PY_FMIPP_DIR%\dist\fmipp-%PY_FMIPP_VERSION%-cp310-none-win_amd64.whl
C:\Python310-x64\Scripts\pytest.exe %PY_FMIPP_DIR%\test\test_pyfmipp.py

CD %PWD%

ENDLOCAL