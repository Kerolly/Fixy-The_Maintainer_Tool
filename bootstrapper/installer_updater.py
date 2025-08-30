# installer_updater.py
from utils.logging_config import updater_logger
import shutil
import os


""" ---------------------------------------
Give the - updater_path_src, source of the updater folder
         - updater_path_dst, destination of the updater folder
--------------------------------------- """

def deploy_updater(updater_path_src, updater_path_dst):

    try:
        if os.path.exists(updater_path_src):
            shutil.copytree(updater_path_src, updater_path_dst, dirs_exist_ok=True) # Copy the entire dir
            print("Debug")
            # logging
            updater_logger.info(f"Successfully deployed {updater_path_dst}")
            print("Successfully deployed")

        else:
            updater_logger.warning(f"File does not exist: {updater_path_src}")
            print("File does not exist")

    except Exception as e:
        updater_logger.error(f"Failed to deploy \n Src: {updater_path_src} \n Dst: {updater_path_dst}\n"
                             f"Error: {e}")
        print(e)


# Testing

deploy_updater("../temp/Fixy", "../TestFixy")