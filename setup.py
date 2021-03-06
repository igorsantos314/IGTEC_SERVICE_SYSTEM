import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os"], "includes": ["tkinter", "sqlite3", "pylab", "numpy", "matplotlib.pyplot"]}

# GUI applications require a different base on Windows (the default is for
# a console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="Service System",
    version="1.0",
    description="Sistema para Gerenciar Serviços de Manicure, Pedicure e Sobrancelhas",
    options={"build_exe": build_exe_options},
    executables=[Executable("App.py", base=base, icon="pything_icon.ico")]
)