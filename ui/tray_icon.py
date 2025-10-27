# tray_icon.py

import pystray
import PIL.Image
import sys
import threading



_window = None
_icon_path = None
_icon = None

# Get the window and icon path
def setup_tray(window, icon_path):
    """
    :param window: The window from TK
    :param icon_path: Icon path for systray
    """
    global _window, _icon_path
    _window = window
    _icon_path = icon_path

    _window.protocol("WM_DELETE_WINDOW", hide_to_tray)

def hide_to_tray():
    # noinspection PyUnresolvedReferences
    _window.withdraw()

    # noinspection PyTypeChecker
    image_tray = PIL.Image.open(_icon_path)

    menu = (
        pystray.MenuItem("Open Fixy", show_window),
        pystray.MenuItem("Exit Fixy", exit_window)
    )

    global _icon
    _icon = pystray.Icon("Fixy", image_tray, "Fixy_The Maintainer Tool", menu)
    #_icon.on_clicked = show_window
    threading.Thread(target=_icon.run, daemon=True).start()

def show_window(icon, item):
    icon.stop()

    # noinspection PyUnresolvedReferences
    _window.after(50, _window.deiconify)


def exit_window(icon, item):
    icon.stop()

    # noinspection PyUnresolvedReferences
    _window.destroy()
    sys.exit(0)


