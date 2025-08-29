# file_manager.py
from utils.logging_config import app_logger
from core.generate_path import get_base_path
import requests
import os
import time
import zipfile

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
        app_logger.debug(f"File name: {filename}") # logging
    else:
        filename = url.split('/')[-1] # get the file name from url
        app_logger.debug(f"File name: {filename}") # logging

    # Generate the path for temp folder
    temp_folder = get_base_path("temp")
    app_logger.debug(f"Temp folder path: {temp_folder}") # logging

    # Create the folder or not
    create_dir(temp_folder)

    # Generate the full path for the zip file, where to download
    full_temp_path = os.path.join(temp_folder, filename).replace("\\", "/")
    app_logger.debug(f"Full temp zip file path: {full_temp_path}")
    print(temp_folder)

    start = time.time() # start timer
    req = requests.get(url, stream=True) # get the req

    if req.status_code == 200:

        try:
            app_logger.info(f"Starting download: {filename}") # logging

            with open(full_temp_path, 'wb') as f:
                for chunk in req.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)

            end = time.time()  # stop timer
            app_logger.info(f"Finished download: {filename}\nFullpath: {full_temp_path}\n"
                                f"Download time: {end - start}") # logging

            print(f"Total downloaded time: {end - start}\n")
        except Exception as e:
            app_logger.error(e) # logging

    else:
        app_logger.error(f'Download failed, status code: {req.status_code}') # logging


def create_dir(path):
    # Check if there is or not a folder at that path
    if not os.path.exists(path):
        os.makedirs(path, exist_ok=True) # Create one


""" ---------------------------------------
Return:  True, if deleted the file
            False, if wasn't deleted
--------------------------------------- """
def delete_file(file_path):
    app_logger.debug(f"File name: {file_path}") # logging

    if os.path.exists(file_path):
        os.remove(file_path)
        app_logger.info(f"Successful deleted file: {file_path}") # logging
        return True

    else:
        app_logger.warning(f"File does not exist: {file_path}") # logging
        return False




""" ---------------------------------------
Give the - full path of the zip file
         - output dir, default = temp, folder
--------------------------------------- """

def unzip(zip_file_path, output_dir=''):
    if output_dir:
        pass
    else:
        output_dir = get_base_path("temp")  # Getting the path for temp folder

        print(output_dir)
        app_logger.debug(f"Output dir: {output_dir}")  # logging

    # Unzip the file
    try:
        # Timer
        start_timer = time.time()

        with zipfile.ZipFile(zip_file_path, "r") as zip_file:
            app_logger.debug(f"Unzipping file....: {zip_file_path}")
            zip_file.extractall(output_dir)

            print(zip_file.namelist())
        app_logger.info(f"Successful unzipped file: {zip_file_path}")

        # Cleaning the zip file
        app_logger.debug(f"Deleting zip file: {zip_file_path}")
        delete_file(zip_file_path) # Deleting the zip file
        app_logger.info(f"Successful deleted file: {zip_file_path}")

        # Timer
        stop_time = time.time()
        app_logger.info(f"Total time: {stop_time - start_timer}")
        print(f"Total time unzipping: {stop_time - start_timer}")
    except Exception as e:
        app_logger.error(e)
        print(e)





# Testing
download_file("https://github.com/Kerolly/Fixy-The_Maintainer_Tool/releases/download/v0.0.1/Fixy.zip")
unzip("../temp/Fixy.zip")