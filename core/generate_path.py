# generate_path.py
import os
import sys
from utils.logging_config import app_logger

'''
-----------------------------------------------------------------
Example of use:
from core.generate_path import get_base_path

get_base_path("Exemple/app.log")
-----------------------------------------------------------------
'''

def get_base_path(relative_path):
    """Returns the correct file path"""
    try:
        base_path = sys._MEIPASS

        # Logging
        app_logger.debug(f"Running from build (Pyinstaller): {base_path}")
    except AttributeError:
        base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

        # Logging
        app_logger.debug(f"Running from local: {base_path}")

    full_path = os.path.join(base_path, relative_path)

    # Logging
    app_logger.info(f"Full path generated: {full_path}")

    return full_path.replace("\\", "/")
