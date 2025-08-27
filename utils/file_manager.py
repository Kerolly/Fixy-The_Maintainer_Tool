# file_manager.py
from utils.logging_config import updater_logger
from core.generate_path import get_base_path
import requests
import os
import time

'''
-----------------------------------------------------------------
Example of use:
from utils.file_manager import download_file(), create_dir()

download_file(url, filename)
create_dir()
-----------------------------------------------------------------
'''


def download_file(url, filename=''):
    if filename:
        pass # if there is a filename, then pass
        updater_logger.debug(f"File name: {filename}") # logging
    else:
        filename = url.split('/')[-1] # get the file name from url
        updater_logger.debug(f"File name: {filename}") # logging

    # Generate the path for temp folder
    temp_folder = get_base_path("temp")
    updater_logger.debug(f"Temp folder path: {temp_folder}") # logging

    # Create the folder or not
    create_dir(temp_folder)

    # Generate the full path for the zip file, where to download
    full_temp_path = os.path.join(temp_folder, filename).replace("\\", "/")
    updater_logger.debug(f"Full temp zip file path: {full_temp_path}")
    print(temp_folder)

    start = time.time() # start timer
    req = requests.get(url, stream=True) # get the req

    if req.status_code == 200:

        try:
            updater_logger.info(f"Starting download: {filename}") # logging

            with open(full_temp_path, 'wb') as f:
                for chunk in req.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)

            end = time.time()  # stop timer
            updater_logger.info(f"Finished download: {filename}\nFullpath: {full_temp_path}\n"
                                f"Download time: {end - start}") # logging

            print(f"Total downloaded time: {end - start}\n")
        except Exception as e:
            updater_logger.error(e) # logging

    else:
        updater_logger.error(f'Download failed, status code: {req.status_code}') # logging


def create_dir(path):
    # Check if there is or not a folder at that path
    if not os.path.exists(path):
        os.makedirs(path, exist_ok=True) # Create one



# Testing
#download_file("https://github.com/Kerolly/Fixy-The_Maintainer_Tool/releases/download/v0.0.1/Fixy.zip")