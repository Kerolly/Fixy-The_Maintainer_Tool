from tkinter import *

title_font = ("Roboto", 18, 'bold')
label_font = ("Roboto", 15, 'semibold')
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

    #right side frame
    right_content_main_frame = Frame(main_frame, bg='red')
    right_content_main_frame.pack(fill='both', expand=True)

    #footer frame
    footer_frame = Frame(window, height=30)
    footer_frame.pack_propagate(False)
    footer_frame.pack(side='bottom', fill='x')

    footer_top_border = Frame(footer_frame, height=2, bg='black')
    footer_top_border.pack(side='top', fill='x')

    window.mainloop()

if __name__ == "__main__":
    create_main_window()
