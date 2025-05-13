from core.admin_check import run_as_admin, is_admin
from ui.main_window import create_main_window
import sys
import os


def main():
    print("[DEBUG] Am I admin?", is_admin())
    print("[DEBUG] Current folder:", os.getcwd())

    try:
        create_main_window()
        print("[DEBUG] Window is opennn!")
    except Exception as e:
        print("[CRITICAL ERROR]", e)
        input("Enter -> close ...")


if __name__ == "__main__":
    if "--admin" in sys.argv:
        main()
    else:
        run_as_admin()