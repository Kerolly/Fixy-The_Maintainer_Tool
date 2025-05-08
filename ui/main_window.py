from tkinter import *
from PIL import Image as PILImage, ImageTk as PILImageTk
from core.version import VERSION
from ui.style import *
from ui.header import build_header
from ui.left_side import build_left_side
from ui.right_side import build_right_side
from ui.footer import build_footer


def create_main_window():
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

if __name__ == "__main__":
    create_main_window()
