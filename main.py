from core.admin_check import run_as_admin, is_admin
from ui.main_window import create_main_window
import sys
import os
import subprocess


def main():
    print("[DEBUG] Am I admin?", is_admin())
    print("[DEBUG] Current folder:", os.getcwd())

    try:
        print("[DEBUG] Window is opennn!")
        create_main_window()

    except Exception as e:
        print("[CRITICAL ERROR]", e)
        #input("Enter -> close ...")
        # if "--admin" in sys.argv:
        #     subprocess.Popen(["pythonw.exe", "main.py", "--admin"], creationflags=subprocess.DETACHED_PROCESS)
        #     sys.exit()
        os.system("pause")


if __name__ == "__main__":
    if "--admin" in sys.argv:
        main()
    else:
        run_as_admin()