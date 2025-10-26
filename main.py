# main.py
import os
import sys
from core.admin_check import run_as_admin, is_admin
from ui.main_window import create_main_window
from utils.logging_config import app_logger
from utils.subprocess_manager import run_subprocess


def main():

    #logging
    print("[DEBUG] Am I admin?", is_admin())
    print("[DEBUG] Current folder:", os.getcwd())

    app_logger.debug(f"Am I admin? {is_admin()}")
    app_logger.debug(f"Current folder: {os.getcwd()}")
    app_logger.debug("Workinggg!")
    app_logger.info("Starting the app!")

    try:
        #print(get_base_path("bootstrapper/bootstrapper"))

        # Call the bootstrapper
        if getattr(sys, 'frozen', False):
            # Run if is exe
            bootstrapper_path = "bootstrapper"
        else:
            # Run if is dev mode
            bootstrapper_path = "bootstrapper/bootstrapper"

        process = run_subprocess(bootstrapper_path, wait=False, silent=False)
        print("exit code:", process.returncode)
        print(f"PID is {process.pid}")

        print("[DEBUG] Window is opennn!")
        create_main_window()
        # Do not put code below


    except Exception as e:
        print("[CRITICAL ERROR]", e)
        # logging
        app_logger.error(e)

        #input("Enter -> close ...")
        # if "--admin" in sys.argv:
        #     subprocess.Popen(["pythonw.exe", "main.py", "--admin"], creationflags=subprocess.DETACHED_PROCESS)
        #     sys.exit()
        os.system("pause")


if __name__ == "__main__":
    #if "--admin" in sys.argv:
    if is_admin():
        main()
    else:
        # logging
        app_logger.warning("Something went wrong!")
        app_logger.info("Try running the admin rights script....")
        run_as_admin()
        app_logger.info("Window opened with admin rights")