# launch_tasks.py
from tkinter import messagebox
import core.state
from core.hosts_block import run_hosts_block
from utils.logging_config import app_logger

def launch_selected_tasks():

    #get the selected tasks from launch dict
    selected_tasks = []
    for key, value in core.state.launch_options.items():
        if value.get() == 1:
            selected_tasks.append(key)

    app_logger.debug(f"Selected tasks: {selected_tasks}") # Logging


    if not selected_tasks:
        app_logger.warning("No tasks selected") # Logging
        messagebox.showwarning("Warning", "Please select at least one option to continue")
        return


    try:
        for task in selected_tasks:
            match task:
                case "temp_file_clean":
                    app_logger.info("Running temp file_clean") # Logging
                    messagebox.showinfo("Succes", "Temp file cleaning")
                    app_logger.info("Successfully cleaned temp file") # Logging
                case "host_block":
                    app_logger.info("Running host block") # Logging
                    run_hosts_block()
                    app_logger.info("Successfully ran host block") # Logging



    except Exception as e:
        messagebox.showerror("Error", "Something went wrong!")
        app_logger.error(e) # Logging

