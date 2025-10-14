# file_manager.py
from utils.logging_config import app_logger
from core.generate_path import get_base_path
import requests
import os
import time
import zipfile
import shutil


def download_file(url, filename=''):
    """
    -----------------------------------------------------------------

    :param url: Url for download
    :param filename: Filename for download, default = getting auto file name from url
    :returns: (True, path for zip file)
    -----------------------------------------------------------------
    """

    if filename:
        pass  # if there is a filename, then pass
        app_logger.debug(f"File name: {filename}")  # logging
    else:
        filename = url.split('/')[-1]  # get the file name from url
        app_logger.debug(f"File name: {filename}")  # logging

    # Generate the path for temp folder
    temp_folder = get_base_path("temp")
    app_logger.debug(f"Temp folder path: {temp_folder}")  # logging

    # Create the folder or not
    create_dir(temp_folder)

    # Generate the full path for the zip file, where to download
    full_temp_path = os.path.join(temp_folder, filename).replace("\\", "/")
    app_logger.debug(f"Full temp zip file path: {full_temp_path}")
    print(f"\nDownloaded path: {full_temp_path}")

    start = time.time()  # start timer
    req = requests.get(url, stream=True)  # get the req

    if req.status_code == 200:

        try:
            app_logger.info(f"Starting download: {filename}")  # logging
            print(f"\nStarting download: {filename} ....")

            with open(full_temp_path, 'wb') as f:
                for chunk in req.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)

            end = time.time()  # stop timer
            app_logger.info(f"Finished download: {filename}\nFullpath: {full_temp_path}\n"
                            f"Download time: {end - start}")  # logging

            print(f"\nFinished download: {filename}\nFullpath: {full_temp_path}\n"
                            f"Download time: {end - start}")
            return True, full_temp_path

        except Exception as e:
            app_logger.error(e)
            print(e)# logging
            raise Exception(e)


    else:
        app_logger.error(f'Download failed, status code: {req.status_code}')  # logging
        print(f'\nDownload failed, status code: {req.status_code}')
        raise Exception(f'Download failed, status code: {req.status_code}')



def create_dir(path):
    # Check if there is or not a folder at that path
    if not os.path.exists(path):
        os.makedirs(path, exist_ok=True)  # Create one


def delete_file(file_path):
    """ ---------------------------------------
    Return:  True, if deleted the file
                False, if wasn't deleted
    --------------------------------------- """

    app_logger.debug(f"File name: {file_path}")  # logging
    print(f"\nFile name for deleting: {file_path}")

    if os.path.exists(file_path):
        os.remove(file_path)
        app_logger.info(f"Successful deleted file: {file_path}")  # logging
        print(f"\nSuccessful deleted file: {file_path}")
        return True

    else:
        app_logger.warning(f"File does not exist: {file_path}")  # logging
        print(f"\nFile does not exist: {file_path}")
        return False


def unzip(zip_file_path, output_dir=''):
    """ ---------------------------------------
    Give the - full path of the zip file
             - output dir, default = temp, folder

    :param zip_file_path: file path for zip
    :param output_dir: output dir for unzipped files, default = temp
    :returns (True, path_folder)
    --------------------------------------- """

    if output_dir:
        pass
    else:
        output_dir = get_base_path("temp")  # Getting the path for temp folder

        #print(output_dir)
        app_logger.debug(f"Output dir: {output_dir}")  # logging
        print(f"Output dir: {output_dir}")

    # Unzip the file
    try:
        # Timer
        start_timer = time.time()

        with zipfile.ZipFile(zip_file_path, "r") as zip_file:
            app_logger.debug(f"Unzipping file....: {zip_file_path}")
            print(f"\nUnzipping file....: {zip_file_path}")
            zip_file.extractall(output_dir)

            #print(zip_file.namelist())
        app_logger.info(f"Successful unzipped file: {zip_file_path}")
        print(f"\nSuccessful unzipped file: {zip_file_path}")

        # Cleaning the zip file
        app_logger.debug(f"Deleting zip file: {zip_file_path}")
        print(f"\nDeleting zip file: {zip_file_path}")
        delete_file(zip_file_path)  # Deleting the zip file
        app_logger.info(f"Successful deleted file: {zip_file_path}")
        print(f"\nSuccessful deleted file: {zip_file_path}")

        # Timer
        stop_time = time.time()
        app_logger.info(f"Total time: {stop_time - start_timer}")
        print(f"Total time unzipping: {stop_time - start_timer}")

        unzip_filename = zip_file_path.split("/")[-1]
        unzip_filename = unzip_filename.split(".")[0]

        return True, output_dir + "/" + unzip_filename

    except Exception as e:
        app_logger.error(e)
        print(e)
        raise Exception(e)


def deploy_files(src, dst, copy_entire_folder=True):
    """ ---------------------------------------
    :param src: source of the folder
    :param dst: destination of the folder
    :param copy_entire_folder: default: True
                                   True: copy entire folder, ex: ab/assets -> copied: ex/assets
                                   False: copy only the subfolders/files, ex: ab/assets -> copied: assets
    --------------------------------------- """

    try:
        if os.path.exists(src):

            if copy_entire_folder:
                shutil.copytree(src, dst, dirs_exist_ok=True)  # Copy the entire folder
                print("Debug")
                # logging
                app_logger.info(f"Successfully deployed, entire folder {dst}")
                print(f"\nSuccessfully deployed, entire folder, here: {dst}")

                return True

            else:
                shutil.copytree(src, dst, copy_function=shutil.copy,
                                dirs_exist_ok=True)  # Copy only the subfolders/files
                print("Debug")
                # logging
                app_logger.info(f"Successfully deployed, subfolders {dst}")
                print(f"\nSuccessfully deployed, subfolders here {dst}")

                return True

        else:
            app_logger.warning(f"File does not exist: {src}")
            print(f"\nFile does not exist, {src}")
            return False

    except Exception as e:
        app_logger.error(f"Failed to deploy \n Src: {src} \n Dst: {dst}\n"
                         f"Error: {e}")
        print(f"Failed to deploy \n Src: {src} \n Dst: {dst}\n"
                         f"Error: {e}")
        raise Exception(e)


# Testing
#download_file("https://github.com/Kerolly/Fixy-The_Maintainer_Tool/releases/download/v0.0.1/Fixy.zip")
#unzip("../temp/Fixy.zip")

# Entire folder
#deploy_files("../temp/Fixy", "../TestFixy")

# Subfolders
#deploy_files("../temp/Fixy", "../", False)
