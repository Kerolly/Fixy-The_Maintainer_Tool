from tkinter import *
from core.version import VERSION


def build_footer(root):
    # footer frame
    footer_frame = Frame(root, height=30)
    footer_frame.pack_propagate(False)
    footer_frame.pack(side='bottom', fill='x')

    footer_top_border = Frame(footer_frame, height=2, bg='black')
    footer_top_border.pack(side='top', fill='x')

    # footer -------

    made_by_title = Label(footer_frame,
                          text="Made by Țicărat Andrei")
    made_by_title.pack(side="left", padx=(25, 0))

    version_title = Label(footer_frame,
                          text="Version: " + VERSION)
    version_title.pack()