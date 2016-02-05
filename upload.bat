@ECHO OFF

REM Set environment variable HOME to the directory containing file '.pypirc'
SET HOME=%~DP0

REM Register.
python.exe "%~DP0\setup.py" bdist_wininst --no-target-compile --no-target-optimize --title "FMI++ Python Interface for Windows" --bitmap logo\logo_py_fmipp.bmp register

REM Manual upload is preferred, since it allows to specify the Python version!
REM python.exe "%~DP0\setup.py" bdist_wininst --no-target-compile --no-target-optimize --title "FMI++ Python Interface for Windows" --bitmap logo\logo_py_fmipp.bmp upload