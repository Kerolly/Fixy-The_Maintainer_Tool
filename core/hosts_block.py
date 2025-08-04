# hosts_block.py
import os
import sys
from core.generate_path import get_base_path
from core.admin_check import *
from tkinter import messagebox
from utils.logging_config import app_logger

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
HOSTS_PATH = r"C:\Windows\System32\drivers\etc\hosts"
BLOCKED_SITES_PATH = get_base_path("core/blocked_sites.txt")


def write_blocked_site_in_hosts_file():

    if not is_admin():
        # logging
        print("Error: This app isn't running with admin!")
        app_logger.error("Error: This app isn't running with admin!")
        messagebox.showwarning("Warning", "This app isn't running with admin!")
    else:
        try:
            with open(BLOCKED_SITES_PATH, "r") as blocked_file:
                print("[DEBUG] Read from blocked sites...")
                app_logger.debug("Read from blocked sites...")
                blocked_sites = blocked_file.readlines()

        except FileNotFoundError as e:
            print(f"[Error]: File not found\n {e}")
            app_logger.error(f"File not found: {e}")
        except PermissionError as e:
            print(f"[Error]: You don't have permissions to modify\n {e}")
            app_logger.error(f"You don't have permissions to modify\n {e}")
        except IOError as e:
            print(f"[Error]: Can not read the file!\n {e}")
            app_logger.error(f"Can not read the file!\n {e}")
        except Exception as e:
            print(f"[Unknown error]: {e}")
            app_logger.error(f"Unknown error: {e}")

        try:
            with open(HOSTS_PATH, "r") as hosts_file:
                existing_hosts_file = hosts_file.read()
                app_logger.debug("Read from hosts file...")

            with open(HOSTS_PATH, "a") as hosts_file:
                print("[DEBUG] Writing the hosts file...")
                app_logger.debug("Writing the hosts file...")
                count_new_blocked_sites = 0
                hosts_file.write("\n\nBlocked sites:\n")

                for site in blocked_sites:
                    if f"127.0.0.1 {site}" in existing_hosts_file:
                        print("This site exist!")
                        app_logger.info(f"This site exist! {site}")
                    else:
                        hosts_file.write(f"127.0.0.1 {site.strip()}\n")
                        count_new_blocked_sites += 1
                print(f"[LOG] Successful written {count_new_blocked_sites}")
                app_logger.info(f"Successful written {count_new_blocked_sites}")
        except PermissionError as e:
            print(f"[Error]: You don't have permissions to modify\n {e}")
            app_logger.error(f"You don't have permissions to modify\n {e}")
        except IOError as e:
            print(f"[Error]: Can not read the file!\n {e}")
            app_logger.error(f"Can not read the file!\n {e}")
        except Exception as e:
            print(f"[Unknown error]:\n {e}")
            app_logger.error(f"Unknown error: {e}")



def check_is_admin():
    if is_admin():
        print("I have admin")
        app_logger.info("I have admin")
    else:
        print("NOO admin")
        app_logger.info("NOO admin")


if __name__ == "__main__":
    run_as_admin()
    write_blocked_site_in_hosts_file()


def run_hosts_block():

    if not is_admin():
        print("Error: This app isn't running with admin!")
        app_logger.error("Error: This app isn't running with admin!")
        messagebox.showwarning("Warning", "This app isn't running with admin!")
    else:
        write_blocked_site_in_hosts_file()
        messagebox.showinfo("Succes", "Site-urile au fost blocate cu succes!")
        app_logger.info("Successful! Sites were blocked!")

