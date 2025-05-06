from tkinter import *
from PIL import Image as PILImage, ImageTk as PILImageTk

title_font = ("Roboto", 18, 'bold')
label_font = ("Roboto", 15, 'normal')
label_bold_font = ("Roboto", 15, 'bold')
button_font = ("Roboto", 14, 'normal')
checkbox_font = ("Roboto", 11, 'normal')

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

    right_content_row = Frame(right_content_main_frame)
    right_content_row.pack(side='left', anchor='n')

    #system clean box
    system_clean_frame = Frame(right_content_row, bg='blue')
    system_clean_frame.grid(row=0, column=0, sticky='n',pady=(30, 0), padx=(60, 0))

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

    # buttons variables
    temp_file_clean_button = IntVar()
    download_folder_clean_button = IntVar()
    recycle_bin_clean_button = IntVar()
    windows_update_button = IntVar()
    disk_clean_button = IntVar()


    #system clean content frame
    #system_clean_content_frame = Frame(system_clean_frame)
    #system_clean_content_frame.pack()

    #system clean content
    temp_file_clean_checkbox = Checkbutton(system_clean_frame,
                                           text="Clean temp file",
                                           variable=temp_file_clean_button,
                                           font=checkbox_font)

    temp_file_clean_checkbox.pack(anchor='w', padx=(15, 0), pady=(3, 0))

    #clean download file
    download_folder_clean_checkbox = Checkbutton(system_clean_frame,
                                           text="Clean download folder",
                                           variable=download_folder_clean_button,
                                           font=checkbox_font)

    download_folder_clean_checkbox.pack(anchor='w', padx=(15, 0), pady=(3, 0))

    # clean recycle bin
    recycle_bin_clean_checkbox = Checkbutton(system_clean_frame,
                                                 text="Clean recycle bin",
                                                 variable=recycle_bin_clean_button,
                                                 font=checkbox_font)

    recycle_bin_clean_checkbox.pack(anchor='w', padx=(15, 0), pady=(3, 0))

    # verif & install Windows update
    windows_update_checkbox = Checkbutton(system_clean_frame,
                                             text="Windows update",
                                             variable=windows_update_button,
                                             font=checkbox_font)

    windows_update_checkbox.pack(anchor='w', padx=(15, 0), pady=(3, 0))

    # disk clean
    disk_clean_checkbox = Checkbutton(system_clean_frame,
                                          text="Disk cleanUp",
                                          variable=disk_clean_button,
                                          font=checkbox_font)

    disk_clean_checkbox.pack(anchor='w', padx=(15, 0), pady=(3, 0))

    #------------------------------------------

    # maintenance box content
    maintenance_frame = Frame(right_content_row, bg='blue')
    maintenance_frame.grid(row=0, column=1, sticky='n',pady=(30, 0), padx=(120, 0))

    # icon
    icon_maintenance = PILImage.open("../assets/icons/maintenance_icon.png")
    icon_maintenance = icon_maintenance.resize((25, 25))
    icon_maintenance = PILImageTk.PhotoImage(icon_maintenance)

    # title
    maintenance_title = Label(maintenance_frame,
                               text='Maintenance',
                               image=icon_maintenance,
                               compound="left",
                               padx=10)

    maintenance_title.config(font=label_bold_font)
    maintenance_title.pack()

    # buttons variables
    desktop_clean_button = IntVar()
    mouse_speed_button = IntVar()


    # desktop clean
    desktop_clean_checkbox = Checkbutton(maintenance_frame,
                                           text="Desktop clean",
                                           variable=desktop_clean_button,
                                           font=checkbox_font)

    desktop_clean_checkbox.pack(anchor='w', padx=(15, 0), pady=(3, 0))

    # mouse speed
    mouse_speed_checkbox = Checkbutton(maintenance_frame,
                                                 text="Mouse speed",
                                                 variable=mouse_speed_button,
                                                 font=checkbox_font)

    mouse_speed_checkbox.pack(anchor='w', padx=(15, 0), pady=(3, 0))


# -------------------------------------------
    window.mainloop()

if __name__ == "__main__":
    create_main_window()
