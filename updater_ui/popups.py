# popups.py

from tkinter import *
from tkinter import messagebox
from utils.logging_config import updater_logger



def create_update_found_window():
    try:
        window = Tk()
        window.title("Fixy Updater")
        window.withdraw()
        window.attributes('-topmost',True)

        res = messagebox.askyesno("Fixy Updater", "New update found\nDo you want to install?")

        window.destroy()

        return res

    except Exception as e:
        print(f"[ERROR]: Failed to create main window. {e}")
        updater_logger.error(e)


def create_loading_window():
    window = Tk()
    window.geometry("420x200")
    window.withdraw()
    window.attributes('-topmost', True)

    messagebox.showinfo("Fixy Updater", "Loading ...")

    window.destroy()


def create_finish_window():
    window = Tk()
    window.geometry("420x200")
    window.withdraw()
    window.attributes('-topmost', True)

    messagebox.showinfo("Fixy Updater", "Update finished, successful!\nPlease open the app")
    window.destroy()


# def center_window(window, width=420, height=220):
#     screen_width = window.winfo_screenwidth()
#     screen_height = window.winfo_screenheight()
#     x = int((screen_width / 2) - (width / 2))
#     y = int((screen_height / 2) - (height / 2))
#     window.geometry(f"{width}x{height}+{x}+{y}")

if __name__ == "__main__":
    create_update_found_window()