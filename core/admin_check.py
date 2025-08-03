# admin_check.py
import os
import sys
import ctypes
from utils.logging_config import app_logger


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


def run_as_admin():
    if not is_admin():
        try:
            print("[DEBUG] Relansăm cu admin...", flush=True)  # flush=True forțează afișarea

            # Logging
            app_logger.info("Relaunch the admin")

            # Get the abs path
            script = os.path.abspath(sys.argv[0])

            # Keep params --admin
            params = " ".join([f'"{arg}"' for arg in sys.argv[1:]] + ["--admin"])

            # Run with admin
            ctypes.windll.shell32.ShellExecuteW(
                None,
                "runas",
                sys.executable,
                f'"{script}" {params}',
                None,
                1  # SW_SHOWNORMAL
            )
            sys.exit(0)
        except Exception as e:
            app_logger.error(e)