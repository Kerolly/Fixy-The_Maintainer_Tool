# subprocess_manager.py
import subprocess
import sys
import os
from core.generate_path import get_base_path
from utils.logging_config import app_logger

"""
Exemple of use:
from utils.subprocess_manager import run_subprocess
    # Run child.py, wait to finish
    code = run_subprocess("testing/child", wait=True, silent=False)
    print(f"Child finished with exit code: {code}")
    
    # Run child.py in background (asynchronous)
    process = run_subprocess("testing/child", wait=False, silent=False)
    print(f"Child started asynchronously with PID: {process.pid}")
"""


def run_subprocess(path, wait=True, silent=False):
    """
    Run a subprocess and return its output
    It could be .exe or script (.py)

    :param path: relative path for the subprocess
    :param wait: True -> wait to finish the subprocess, False -> run asynchronously
    :param silent: True -> no console or GUI, False -> with console or GUI
    :return: exit code (int) if wait=True, or subprocess.Popen object if wait=False
    """
    app_logger.debug(f"args: {path, wait, silent}")

    abs_path = get_base_path(path)
    app_logger.debug(f"abs_path: {abs_path}")

    start_up_info = None

    try:

        # Checking if is in dev mode or in exe to create the cmd for subprocess
        if getattr(sys, 'frozen', False):
            abs_path = abs_path + ".exe" # create the extension for .exe
            cmd = [abs_path]
        else:
            abs_path = abs_path + ".py" # create the extension for .py
            cmd = [sys.executable, abs_path]

        if silent:
            # Create an STARTUPINFO obj, which can config the window process
            start_up_info = subprocess.STARTUPINFO()
            # Set the dwFlags to indicate that we want to use the wShowWindow setting
            #* |= is a bitwise OR operator, which allows adding on top of the other existing settings (without overwriting)
            start_up_info.dwFlags |= subprocess.STARTF_USESHOWWINDOW
            # Set wShowWindow to SW_HIDE, so that the process window is completely hidden (no console or GUI)
            start_up_info.wShowWindow = subprocess.SW_HIDE

        if wait:
            result = subprocess.run(cmd, startupinfo=start_up_info, cwd=os.path.dirname(sys.executable))
            app_logger.debug(f"Full path for run: {abs_path}")
            app_logger.info(f"Subprocess exit code: {result.returncode}")
            return result.returncode
        else:
            process = subprocess.Popen(cmd, startupinfo=start_up_info, cwd=os.path.dirname(sys.executable))
            app_logger.debug(f"Full path for popen: {abs_path}")
            app_logger.info(f"Subprocess PID code: {process.pid}")
            return process

    except Exception as e:
        app_logger.error(f"Could not run subprocess: {e}")
        print(f"[ERROR] Could not run subprocess: {e}")





