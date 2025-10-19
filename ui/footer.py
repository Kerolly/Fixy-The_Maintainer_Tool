# footer.py
from tkinter import *
from utils.file_manager import read_from_json
from utils.generate_path import get_base_path


def build_footer(root):
    data = read_from_json(get_base_path("versions.json"))

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
                          text="Version: " + data["fixy_version"])
    version_title.pack()