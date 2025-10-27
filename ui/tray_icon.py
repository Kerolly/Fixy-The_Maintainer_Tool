# tray_icon.py

import pystray
import PIL.Image
import sys
import threading
from utils.logging_config import app_logger



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
    """
    Hide to tray icon
    """
    try:
        app_logger.debug(f"Hide to tray icon")
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

    except Exception as e:
        app_logger.error(f"There is an error: {e}")

def show_window(icon, item):
    """
    Show the window
    """
    try:
        app_logger.debug(f"Show the window")
        icon.stop()

        # noinspection PyUnresolvedReferences
        _window.after(50, _window.deiconify)
    except Exception as e:
        app_logger.error(f"There is an error: {e}")


def exit_window(icon, item):
    """
    Exit the application
    """
    try:
        app_logger.debug(f"Exit the window")
        icon.stop()

        # noinspection PyUnresolvedReferences
        _window.destroy()
        sys.exit(0)
    except Exception as e:
        app_logger.error(f"There is an error: {e}")

