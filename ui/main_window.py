from tkinter import *
from PIL import Image as PILImage, ImageTk as PILImageTk

title_font = ("Roboto", 18, 'bold')
label_font = ("Roboto", 15, 'normal')
label_bold_font = ("Roboto", 15, 'bold')
button_font = ("Roboto", 14, 'normal')

def create_main_window():
    # initiate the window
    window = Tk()
    window.title("Fixy-The Maintainer Tool") #window title
    window.geometry("800x600") #window size

    #header frame
    header_frame = Frame(window, height=50)
    header_frame.pack_propagate(False)
    header_frame.pack(fill='x')

    #bottom border
    bottom_border = Frame(header_frame, bg='black', width=2)
    bottom_border.pack(side='bottom', fill='x')

    #header title
    header_title = Label(header_frame, text="Fixy-The Maintainer Tool", font=title_font)
    header_title.pack(side='left')

    #header buttons
    buttons_frame = Frame(header_frame, padx='20') #buttons frame
    buttons_frame.pack(side='right', fill='x')

    header_update_button = Button(buttons_frame, text="Update", font=button_font) #update button
    header_update_button.pack(side='left', padx='20')

    header_launch_button = Button(buttons_frame, text="Launch", font=button_font)  # launch button
    header_launch_button.pack(side='right')

    #main frame
    main_frame = Frame(window)
    main_frame.pack(fill='both', expand=True)

    #left side frame
    left_content_main_frame = Frame(main_frame, width=235, bg='#D9D9D9')
    #left_content_main_frame.pack_propagate(False)
    left_content_main_frame.pack(side='left', fill='y')
    left_content_main_frame.propagate(False)

    #right side frame
    right_content_main_frame = Frame(main_frame, bg='red')
    right_content_main_frame.pack(fill='both', expand=True)

    #footer frame
    footer_frame = Frame(window, height=30)
    footer_frame.pack_propagate(False)
    footer_frame.pack(side='bottom', fill='x')

    footer_top_border = Frame(footer_frame, height=2, bg='black')
    footer_top_border.pack(side='top', fill='x')

    #left side buttons---------------------------------
    #buttons variables
    week_maintanance_button = IntVar()
    super_clean_button = IntVar()
    logicamp_apps_button = IntVar()
    new_setup_button = IntVar()


    #button frame
    left_content_buttons_frame = Frame(left_content_main_frame, bg='#D9D9D9')
    left_content_buttons_frame.pack(pady=(20, 0), fill='x')


    #week maintanance checkbox
    week_maintanance_checkbox = Checkbutton(left_content_buttons_frame,
                                            text='Week Maintanance',
                                            variable=week_maintanance_button)
    week_maintanance_checkbox.config(font=label_font,
                                     bg='#D9D9D9',
                                     activebackground='#D9D9D9')
    week_maintanance_checkbox.pack(anchor='w', padx=(15, 0))


    # super clean checkbox
    super_clean_checkbox = Checkbutton(left_content_buttons_frame,
                                            text='Super Clean',
                                            variable=super_clean_button)
    super_clean_checkbox.config(font=label_font,
                                     bg='#D9D9D9',
                                     activebackground='#D9D9D9')
    super_clean_checkbox.pack(anchor='w', padx=(15, 0), pady=(15, 0))


    # logicamp apps checkbox
    logicamp_apps_checkbox = Checkbutton(left_content_buttons_frame,
                                       text='Logicamp Apps',
                                       variable=logicamp_apps_button)
    logicamp_apps_checkbox.config(font=label_font,
                                bg='#D9D9D9',
                                activebackground='#D9D9D9')
    logicamp_apps_checkbox.pack(anchor='w', padx=(15, 0), pady=(15, 0))


    # new setup checkbox
    new_setup_checkbox = Checkbutton(left_content_buttons_frame,
                                         text='New Setup',
                                         variable=new_setup_button)
    new_setup_checkbox.config(font=label_font,
                                  bg='#D9D9D9',
                                  activebackground='#D9D9D9')
    new_setup_checkbox.pack(anchor='w', padx=(15, 0), pady=(15, 0))

#-------------------------------------------

    #right content

    #system clean box
    system_clean_frame = Frame(right_content_main_frame, bg='blue')
    system_clean_frame.pack(side='left', anchor='n', pady=(30, 0), padx=(60, 0))

    #icon
    icon_system_clean = PILImage.open("../assets/icons/system_clean_icon.png")
    icon_system_clean = icon_system_clean.resize((25,25))
    icon_system_clean = PILImageTk.PhotoImage(icon_system_clean)
    #title
    system_clean_title = Label(system_clean_frame,
                               text='System Clean',
                               image=icon_system_clean,
                               compound="left",
                               padx=10)

    system_clean_title.config(font=label_bold_font)
    system_clean_title.pack()


# -------------------------------------------
    window.mainloop()

if __name__ == "__main__":
    create_main_window()
