import os
import sys
from core.admin_check import *
from tkinter import messagebox

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
HOSTS_PATH = r"C:\Windows\System32\drivers\etc\hosts"
BLOCKED_SITES_PATH = os.path.join(BASE_DIR, "..", "core", "blocked_sites.txt")


def write_blocked_site_in_hosts_file():


    if not is_admin():
        print("Error: This app isn't running with admin!")
        messagebox.showwarning("Warning", "This app isn't running with admin!")
    else:
        try:
            with open(BLOCKED_SITES_PATH, "r") as blocked_file:
                print("[DEBUG] Red from blocked sites...")
                blocked_sites = blocked_file.readlines()

        except FileNotFoundError as e:
            print(f"[Error]: File not found\n {e}")
        except PermissionError as e:
            print(f"[Error]: You don't have permissions to modify\n {e}")
        except IOError as e:
            print(f"[Error]: Can not read the file!\n {e}")
        except Exception as e:
            print(f"[Unknown error]: {e}")

        try:
            with open(HOSTS_PATH, "r") as hosts_file:
                existing_hosts_file = hosts_file.read()

            with open(HOSTS_PATH, "a") as hosts_file:
                print("[DEBUG] Writing the hosts file...")
                count_new_blocked_sites = 0
                hosts_file.write("\n\nBlocked sites:\n")
                for site in blocked_sites:
                    if f"127.0.0.1 {site}" in existing_hosts_file:
                        print("This site exist!")
                    else:
                        hosts_file.write(f"127.0.0.1 {site.strip()}\n")
                        count_new_blocked_sites += 1
                print(f"[LOG] Successful written {count_new_blocked_sites}")
        except PermissionError as e:
            print(f"[Error]: You don't have permissions to modify\n {e}")
        except IOError as e:
            print(f"[Error]: Can not read the file!\n {e}")
        except Exception as e:
            print(f"[Unknown error]:\n {e}")



def check_is_admin():
    if is_admin():
        print("Am drepturi de admin")
    else:
        print("NU am drepturi de admin")


if __name__ == "__main__":
    run_as_admin()
    write_blocked_site_in_hosts_file()


def run_hosts_block():

    if not is_admin():
        print("Error: This app isn't running with admin!")
        messagebox.showwarning("Warning", "This app isn't running with admin!")
    else:
        write_blocked_site_in_hosts_file()
        messagebox.showinfo("Succes", "Site-urile au fost blocate cu succes!")

