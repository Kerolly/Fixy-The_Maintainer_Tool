#generate_path.py
import os
import sys

def get_base_path(relative_path):
    """Returns the correct file path"""
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

    full_path = os.path.join(base_path, relative_path)
    return full_path.replace("\\", "/")
