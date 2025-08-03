# main.py
import os
import sys

from core.admin_check import run_as_admin, is_admin
from ui.main_window import create_main_window
from utils.logging_config import app_logger


def main():

    #Logging
    print("[DEBUG] Am I admin?", is_admin())
    print("[DEBUG] Current folder:", os.getcwd())

    app_logger.debug(f"Am I admin? {is_admin()}")
    app_logger.debug(f"Current folder: {os.getcwd()}")
    app_logger.debug("Workinggg!")
    app_logger.info("Starting the app!")

    try:
        print("[DEBUG] Window is opennn!")
        create_main_window()

        # Logging
        app_logger.info("Window is open")

    except Exception as e:
        print("[CRITICAL ERROR]", e)
        # Logging
        app_logger.error(e)

        #input("Enter -> close ...")
        # if "--admin" in sys.argv:
        #     subprocess.Popen(["pythonw.exe", "main.py", "--admin"], creationflags=subprocess.DETACHED_PROCESS)
        #     sys.exit()
        os.system("pause")


if __name__ == "__main__":
    if "--admin" in sys.argv:
        main()
    else:
        # Logging
        app_logger.warning("Something went wrong!")
        app_logger.info("Try running the admin rights script....")
        run_as_admin()
        app_logger.info("Window opened with admin rights")