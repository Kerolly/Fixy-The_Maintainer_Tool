# main_window.py
from core.admin_check import run_as_admin
from tkinter import *
from ui.header import build_header
from ui.left_side import build_left_side
from ui.right_side import build_right_side
from ui.footer import build_footer
from utils.logging_config import app_logger


def create_main_window():
    try:
        # initiate the window
        window = Tk()
        window.title("Fixy-The Maintainer Tool") #window title
        window.geometry("850x600") #window size

        #header builder
        build_header(window)

        #main frame
        main_frame = Frame(window)
        main_frame.pack(fill='both', expand=True)

        #left side builder
        build_left_side(main_frame)

        #right side builder
        build_right_side(main_frame)

        #footer builder
        build_footer(window)

        # -------------------------------------------
        window.mainloop()

    except Exception as e:
        # logging
        app_logger.error(e)




if __name__ == "__main__":
    # logging
    app_logger.info("Running the admin script")
    run_as_admin()
    create_main_window()
    app_logger.info("Opened the main window with admin")

