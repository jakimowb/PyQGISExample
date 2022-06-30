:: this script stats PyCharm in a requested QGIS environment
call "%~dp0\qgis_env.bat" qgis-ltr
start "PYCHARM" /B %PYCHARM_EXE%
