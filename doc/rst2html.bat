REM To run this script, install 'doctutils' and 'pygments' for Python first!

SET PYTHON_DIR=C:\Python37-x64

%PYTHON_DIR%\python.exe %PYTHON_DIR%\Scripts\rst2html.py --stylesheet=pygments-long.css,style.css doc.txt index.html