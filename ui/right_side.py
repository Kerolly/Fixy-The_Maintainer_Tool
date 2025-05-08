from tkinter import *
from ui.style import *
from PIL import Image as PILImage, ImageTk as PILImageTk


def build_right_side(root):

    # right side frame
    right_content_main_frame = Frame(root)
    right_content_main_frame.pack(fill='both', expand=True)

    # right content

    right_content_row = Frame(right_content_main_frame)
    right_content_row.pack(side='left', anchor='n')

    # system clean box
    system_clean_frame = Frame(right_content_row)
    system_clean_frame.grid(row=0, column=0, sticky='n', pady=(30, 0), padx=(60, 0))

    # icon
    icon_system_clean = PILImage.open("../assets/icons/system_clean_icon.png")
    icon_system_clean = icon_system_clean.resize((25, 25))
    icon_system_clean = PILImageTk.PhotoImage(icon_system_clean)

    # title
    system_clean_title = Label(system_clean_frame,
                               text='System Clean',
                               image=icon_system_clean,
                               compound="left",
                               padx=10)

    system_clean_title.config(font=LABEL_BOLD_FONT)
    system_clean_title.image = icon_system_clean
    system_clean_title.pack()

    # buttons variables
    temp_file_clean_button = IntVar()
    download_folder_clean_button = IntVar()
    recycle_bin_clean_button = IntVar()
    windows_update_button = IntVar()
    disk_clean_button = IntVar()

    # system clean content
    temp_file_clean_checkbox = Checkbutton(system_clean_frame,
                                           text="Clean temp file",
                                           variable=temp_file_clean_button,
                                           font=CHECKBOX_FONT)

    temp_file_clean_checkbox.pack(anchor='w', padx=(15, 0), pady=(3, 0))

    # clean download file
    download_folder_clean_checkbox = Checkbutton(system_clean_frame,
                                                 text="Clean download folder",
                                                 variable=download_folder_clean_button,
                                                 font=CHECKBOX_FONT)

    download_folder_clean_checkbox.pack(anchor='w', padx=(15, 0), pady=(3, 0))

    # clean recycle bin
    recycle_bin_clean_checkbox = Checkbutton(system_clean_frame,
                                             text="Clean recycle bin",
                                             variable=recycle_bin_clean_button,
                                             font=CHECKBOX_FONT)

    recycle_bin_clean_checkbox.pack(anchor='w', padx=(15, 0), pady=(3, 0))

    # verif & install Windows update
    windows_update_checkbox = Checkbutton(system_clean_frame,
                                          text="Windows update",
                                          variable=windows_update_button,
                                          font=CHECKBOX_FONT)

    windows_update_checkbox.pack(anchor='w', padx=(15, 0), pady=(3, 0))

    # disk clean
    disk_clean_checkbox = Checkbutton(system_clean_frame,
                                      text="Disk cleanUp",
                                      variable=disk_clean_button,
                                      font=CHECKBOX_FONT)

    disk_clean_checkbox.pack(anchor='w', padx=(15, 0), pady=(3, 0))

    # ------------------------------------------

    # maintenance box content
    maintenance_frame = Frame(right_content_row)
    maintenance_frame.grid(row=0, column=1, sticky='n', pady=(30, 0), padx=(120, 0))

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

    maintenance_title.config(font=LABEL_BOLD_FONT)
    maintenance_title.image = icon_maintenance
    maintenance_title.pack()

    # buttons variables
    desktop_clean_button = IntVar()
    mouse_speed_button = IntVar()
    host_block_button = IntVar()

    # desktop clean
    desktop_clean_checkbox = Checkbutton(maintenance_frame,
                                         text="Desktop clean",
                                         variable=desktop_clean_button,
                                         font=CHECKBOX_FONT)

    desktop_clean_checkbox.pack(anchor='w', padx=(15, 0), pady=(3, 0))

    # mouse speed
    mouse_speed_checkbox = Checkbutton(maintenance_frame,
                                       text="Mouse speed",
                                       variable=mouse_speed_button,
                                       font=CHECKBOX_FONT)

    mouse_speed_checkbox.pack(anchor='w', padx=(15, 0), pady=(3, 0))

    # host block
    host_block_checkbox = Checkbutton(maintenance_frame,
                                      text="Host block",
                                      variable=host_block_button,
                                      font=CHECKBOX_FONT)

    host_block_checkbox.pack(anchor='w', padx=(15, 0), pady=(3, 0))
    # -------------------------------------------

    # chrome content box ----------------------
    chrome_frame = Frame(right_content_row)
    chrome_frame.grid(row=1, column=0, sticky='n', pady=(30, 0), padx=(60, 0))

    # icon
    icon_chrome = PILImage.open("../assets/icons/chrome_icon.png")
    icon_chrome = icon_chrome.resize((25, 25))
    icon_chrome = PILImageTk.PhotoImage(icon_chrome)

    # title
    chrome_title = Label(chrome_frame,
                         text='Chrome',
                         image=icon_chrome,
                         compound="left",
                         padx=10)

    chrome_title.config(font=LABEL_BOLD_FONT)
    chrome_title.image = icon_chrome
    chrome_title.pack()

    # buttons variables
    auto_opening_site_button = IntVar()
    dark_mode_chrome_button = IntVar()
    clean_history_button = IntVar()
    auto_cookie_delete_button = IntVar()
    set_background_button = IntVar()

    # auto opening site: www.mylogiscool.com
    auto_opening_site_checkbox = Checkbutton(chrome_frame,
                                             text="Auto opening mylogiscool",
                                             variable=auto_opening_site_button,
                                             font=CHECKBOX_FONT)

    auto_opening_site_checkbox.pack(anchor='w', padx=(15, 0), pady=(3, 0))

    # chrom dark mode
    dark_mode_chrome_checkbox = Checkbutton(chrome_frame,
                                            text="Dark Mode Chrome",
                                            variable=dark_mode_chrome_button,
                                            font=CHECKBOX_FONT)

    dark_mode_chrome_checkbox.pack(anchor='w', padx=(15, 0), pady=(3, 0))

    # clean history
    clean_history_checkbox = Checkbutton(chrome_frame,
                                         text="Clean history",
                                         variable=clean_history_button,
                                         font=CHECKBOX_FONT)

    clean_history_checkbox.pack(anchor='w', padx=(15, 0), pady=(3, 0))

    # auto cookie delete
    auto_cookie_delete_checkbox = Checkbutton(chrome_frame,
                                              text="Auto Cookie Delete",
                                              variable=auto_cookie_delete_button,
                                              font=CHECKBOX_FONT)

    auto_cookie_delete_checkbox.pack(anchor='w', padx=(15, 0), pady=(3, 0))

    # set background
    set_background_checkbox = Checkbutton(chrome_frame,
                                          text="Set background",
                                          variable=set_background_button,
                                          font=CHECKBOX_FONT)

    set_background_checkbox.pack(anchor='w', padx=(15, 0), pady=(3, 0))

    # ------------------------------------------

    # install apps box content ----------------------
    install_apps_frame = Frame(right_content_row)
    install_apps_frame.grid(row=1, column=1, sticky='n', pady=(30, 0), padx=(60, 0))

    # icon
    icon_install_apps = PILImage.open("../assets/icons/install_apps_icon.png")
    icon_install_apps = icon_install_apps.resize((25, 25))
    icon_install_apps = PILImageTk.PhotoImage(icon_install_apps)

    # title
    install_apps_title = Label(install_apps_frame,
                               text='Install Apps',
                               image=icon_install_apps,
                               compound="left",
                               padx=10)

    install_apps_title.config(font=LABEL_BOLD_FONT)
    install_apps_title.image = icon_install_apps
    install_apps_title.pack()

    # buttons variables
    python_app_button = IntVar()
    pycharm_app_button = IntVar()

    # python app
    python_app_checkbox = Checkbutton(install_apps_frame,
                                      text="Python",
                                      variable=python_app_button,
                                      font=CHECKBOX_FONT)

    python_app_checkbox.pack(anchor='w', padx=(15, 0), pady=(3, 0))

    # pycharm app
    pycharm_app_checkbox = Checkbutton(install_apps_frame,
                                       text="Pycharm",
                                       variable=pycharm_app_button,
                                       font=CHECKBOX_FONT)

    pycharm_app_checkbox.pack(anchor='w', padx=(15, 0), pady=(3, 0))

    # ------------------------------------------

