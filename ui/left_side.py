from tkinter import *
from ui.style import *

def build_left_side(root):

    # left side frame
    left_content_main_frame = Frame(root, width=235, bg='#D9D9D9')
    left_content_main_frame.pack(side='left', fill='y')
    left_content_main_frame.propagate(False)

    # left side buttons---------------------------------
    # buttons variables
    week_maintanance_button = IntVar()
    super_clean_button = IntVar()
    logicamp_apps_button = IntVar()
    new_setup_button = IntVar()

    # button frame
    left_content_buttons_frame = Frame(left_content_main_frame, bg='#D9D9D9')
    left_content_buttons_frame.pack(pady=(20, 0), fill='x')

    # week maintanance checkbox
    week_maintanance_checkbox = Checkbutton(left_content_buttons_frame,
                                            text='Week Maintanance',
                                            variable=week_maintanance_button)
    week_maintanance_checkbox.config(font=LABEL_FONT,
                                     bg='#D9D9D9',
                                     activebackground='#D9D9D9')
    week_maintanance_checkbox.pack(anchor='w', padx=(15, 0))

    # super clean checkbox
    super_clean_checkbox = Checkbutton(left_content_buttons_frame,
                                       text='Super Clean',
                                       variable=super_clean_button)
    super_clean_checkbox.config(font=LABEL_FONT,
                                bg='#D9D9D9',
                                activebackground='#D9D9D9')
    super_clean_checkbox.pack(anchor='w', padx=(15, 0), pady=(15, 0))

    # logicamp apps checkbox
    logicamp_apps_checkbox = Checkbutton(left_content_buttons_frame,
                                         text='Logicamp Apps',
                                         variable=logicamp_apps_button)
    logicamp_apps_checkbox.config(font=LABEL_FONT,
                                  bg='#D9D9D9',
                                  activebackground='#D9D9D9')
    logicamp_apps_checkbox.pack(anchor='w', padx=(15, 0), pady=(15, 0))

    # new setup checkbox
    new_setup_checkbox = Checkbutton(left_content_buttons_frame,
                                     text='New Setup',
                                     variable=new_setup_button)
    new_setup_checkbox.config(font=LABEL_FONT,
                              bg='#D9D9D9',
                              activebackground='#D9D9D9')
    new_setup_checkbox.pack(anchor='w', padx=(15, 0), pady=(15, 0))

# -------------------------------------------