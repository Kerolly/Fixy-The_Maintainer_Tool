from tkinter import *
from ui.style import *


#header builder
def build_header(root):
    # header frame
    header_frame = Frame(root, height=50)
    header_frame.pack_propagate(False)
    header_frame.pack(fill='x')

    # bottom border
    bottom_border = Frame(header_frame, bg='black', width=2)
    bottom_border.pack(side='bottom', fill='x')

    # header title
    header_title = Label(header_frame, text="Fixy-The Maintainer Tool", font=TITLE_FONT)
    header_title.pack(side='left')

    # header buttons
    buttons_frame = Frame(header_frame, padx='20')  # buttons frame
    buttons_frame.pack(side='right', fill='x')

    header_update_button = Button(buttons_frame, text="Update", font=BUTTON_FONT)  # update button
    header_update_button.pack(side='left', padx='20')

    header_launch_button = Button(buttons_frame, text="Launch", font=BUTTON_FONT)  # launch button
    header_launch_button.pack(side='right')
