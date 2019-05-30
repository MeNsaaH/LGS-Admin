import sys
from cx_Freeze import setup, Executable 


build_exe_options = {'packages': ['os'],
                    "excludes": ["PyQt5.QtSql", 
                                  "PyQt5.QtNetwork", "PyQt5.QtBluetooth",
                                  "PyQt5.QtScript", "PyQt5.QtDBus",
                                  "PyQt5.QtDesigner", "PyQt5.QtHelp", 
                                  "PyQt5.QtLocation", "PyQt5.QtMultimedia", 
                                  "PyQt5.QtNfc", "PyQt5.QtOpenGl",
                                  "PyQt5.QtQuick", "PyQt5.QtQml", 
                                  "PyQt5.QtSensors", "PyQt5.QtSerialPort",
                                  "PyQt5.QtSvg", "PyQt5.QtTest",
                                  "PyQt5.QtXml", "PyQt5.QtWebSockets",
                                  ],
                     "optimize": 2}


base = None 
if sys.platform == 'win32':
    base = 'Win32GUI'

target = Executable(
    script = '__init__.py',
    base = base,
    icon = 'images/icon.ico',
    shortcutName = 'iLecture Grading System',
    copyright = 'Software Engineering II Group 1, FUT Minna 2018',
    trademarks = 'Copy Right 2018- FUTMinna',
    targetName = "iLGS.exe",
    )

setup(
    name = 'iLecture Grading System', 
    version = '1.0.0',
    description = "Connecting Students Lecturer view to the school Admin",
    author = 'Group 1, SE II Futminna',
    #publisher = 'Mensaah Corps',
    options = {'build_exe': build_exe_options},
    executables = [target]
    )