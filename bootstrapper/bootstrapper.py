# bootstrapper.py
import os
import sys


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) # added to sys.path
from utils.logging_config import updater_logger
from utils.version_manager import check_versions, update_local_version
from utils.file_manager import download_file, unzip, deploy_files
from utils.generate_path import get_base_path
from utils.subprocess_manager import run_subprocess

def bootstrapper():
    print("Bootstrapper started")
    updater_logger.info("Bootstrapper started")

    try:
        versions_results = check_versions(version_for='updater')

        if versions_results[0] == True:

            # get the returns from download function
            download_results = download_file(versions_results[1])
            if download_results[0] == True:
                print("Download successful, updater")
                updater_logger.info("Download successful, updater")
                # getting the path for zip file
                zip_file_path = download_results[1]

                # getting the results from unzipping
                success_unzip, unzipped_path = unzip(zip_file_path)
                if success_unzip:
                    print(f"Unzip successful {unzipped_path}")
                    updater_logger.info(f"Unzip successful {unzipped_path}")

                    # getting the dst folder for updater
                    dst_folder = get_base_path("") # root of the app
                    if deploy_files(unzipped_path, dst_folder, copy_entire_folder=False):
                        print(f"Deploy successful, here {dst_folder}")
                        updater_logger.info(f"Deploy successful, here {dst_folder}")

                        # writing the new version to json
                        update_local_version(version_for="updater", new_version=versions_results[3])

        run_updater()

    except Exception as e:
        print(f"Bootstrapper error: {e}")
        updater_logger.error(f"Bootstrapper error: {e}")

def run_updater():

    try:
        # Call the updater
        if getattr(sys, 'frozen', False):
            # Run if is exe
            updater_path = "updater"
        else:
            # Run if is dev mode
            updater_path = "updater/updater"

        process = run_subprocess(updater_path, wait=False, silent=False)
        print("exit code:", process.returncode)
        print(f"PID is {process.pid}")

    except Exception as e:
        print(f"Bootstrapper try to open updater error: {e}")
        updater_logger.error(f"Bootstrapper try to open updater error: {e}")




if __name__ == '__main__':
    bootstrapper()

