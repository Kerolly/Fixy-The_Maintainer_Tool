# generate_path.py
from pathlib import Path
import sys

"""
-----------------------------------------------------------------
Example of use:
from core.generate_path import get_base_path

get_base_path("exemple/app.log")
-----------------------------------------------------------------
"""

def get_app_root() -> Path:
    """
    Returns the absolute path to the application's root directory.

    When running from a frozen executable (cx_Freeze),
    this points to the directory containing the .exe file.

    When running in dev mode (from source code),
    this points to the directory containing this script.
    """
    if getattr(sys, "frozen", False):
        # Run from exe
        exe_dir = Path(sys.executable).resolve().parent
    else:
        # Run in dev mode
        exe_dir = Path(__file__).resolve().parent.parent

    return exe_dir


def get_base_path(relative_path:str) -> str:
    """
    Returns the absolute path to a file or directory
    relative to the application's root directory.

     Example:
        >>> get_base_path("assets/logo.png")
        'C:\\Path\\To\\App\\assets\\logo.png'
    """
    return str((get_app_root() / relative_path).resolve())
