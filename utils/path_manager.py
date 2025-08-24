# path_manager.py

import os
import sys

def get_logging_path(file_name):
    if hasattr(sys, '_MEIPASS'):
        base_path = os.path.dirname(sys.executable) # Get the path from exe folder
    else:
        base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

    logging_folder = os.path.join(base_path, "logging")
    os.makedirs(logging_folder, exist_ok=True)

    return os.path.join(logging_folder, file_name).replace("\\", "/")
