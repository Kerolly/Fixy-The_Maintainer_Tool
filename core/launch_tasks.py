from tkinter import messagebox
import core.state
from core.hosts_block import run_hosts_block

def launch_selected_tasks():

    #get the selected tasks from launch dict
    selected_tasks = []
    for key, value in core.state.launch_options.items():
        if value.get() == 1:
            selected_tasks.append(key)


    if not selected_tasks:
        messagebox.showwarning("Warning", "Please select at least one option to continue")
        return


    try:
        for task in selected_tasks:
            match task:
                case "temp_file_clean":
                    messagebox.showinfo("Succes", "Temp file cleaning")
                case "host_block":
                    run_hosts_block()



    except Exception as e:
        messagebox.showerror("Error", "Something went wrong!")

