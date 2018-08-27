@ECHO OFF

REM General settings.
SET PY_FMIPP_DIR=C:\Production\py-fmipp
SET PY_FMIPP_VERSION=1.4.1

REM Run tests for all versions.

SET PWD=%CD%
CD %PY_FMIPP_DIR%\test

ECHO ###### Python27-x64 ######
ECHO y | C:\Python27-x64\Scripts\pip.exe uninstall fmipp
C:\Python27-x64\Scripts\pip.exe install %PY_FMIPP_DIR%\dist\fmipp-%PY_FMIPP_VERSION%-cp27-none-win_amd64.whl
C:\Python27-x64\Scripts\pytest.exe %PY_FMIPP_DIR%\test\test_pyfmipp.py

ECHO ###### Python27-x86 ######
ECHO y | C:\Python27-x86\Scripts\pip.exe uninstall fmipp
C:\Python27-x86\Scripts\pip.exe install %PY_FMIPP_DIR%\dist\fmipp-%PY_FMIPP_VERSION%-cp27-none-win32.whl
C:\Python27-x86\Scripts\pytest.exe %PY_FMIPP_DIR%\test\test_pyfmipp.py

ECHO ###### Python36-x64 ######
ECHO y | C:\Python36-x64\Scripts\pip.exe uninstall fmipp
C:\Python36-x64\Scripts\pip.exe install %PY_FMIPP_DIR%\dist\fmipp-%PY_FMIPP_VERSION%-cp36-none-win_amd64.whl
C:\Python36-x64\Scripts\pytest.exe %PY_FMIPP_DIR%\test\test_pyfmipp.py

ECHO ###### Python36-x86 ######
ECHO y | C:\Python36-x86\Scripts\pip.exe uninstall fmipp
C:\Python36-x86\Scripts\pip.exe install %PY_FMIPP_DIR%\dist\fmipp-%PY_FMIPP_VERSION%-cp36-none-win32.whl
C:\Python36-x86\Scripts\pytest.exe %PY_FMIPP_DIR%\test\test_pyfmipp.py

ECHO ###### Python37-x64 ######
ECHO y | C:\Python37-x64\Scripts\pip.exe uninstall fmipp
C:\Python37-x64\Scripts\pip.exe install %PY_FMIPP_DIR%\dist\fmipp-%PY_FMIPP_VERSION%-cp37-none-win_amd64.whl
C:\Python37-x64\Scripts\pytest.exe %PY_FMIPP_DIR%\test\test_pyfmipp.py

ECHO ###### Python37-x86 ######
ECHO y | C:\Python37-x86\Scripts\pip.exe uninstall fmipp
C:\Python37-x86\Scripts\pip.exe install %PY_FMIPP_DIR%\dist\fmipp-%PY_FMIPP_VERSION%-cp37-none-win32.whl
C:\Python37-x86\Scripts\pytest.exe %PY_FMIPP_DIR%\test\test_pyfmipp.py

CD %PWD%