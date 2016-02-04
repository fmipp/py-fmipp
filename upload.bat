@ECHO OFF

REM Set environment variable HOME to the directory containing file '.pypirc'
SET HOME=%~DP0

REM Register.
python setup.py register

REM Upload.
python setup.py bdist_wininst upload