# bootstrapper.py
import os
import sys


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) # added to sys.path
from utils.logging_config import updater_logger
from utils.version_checker import check_versions
from utils.file_manager import download_file, unzip, deploy_files
from core.generate_path import get_base_path

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
                    dst_folder = get_base_path("updater")
                    if deploy_files(unzipped_path, dst_folder, copy_entire_folder=False):
                        print(f"Deploy successful, here {dst_folder}")
                        updater_logger.info(f"Deploy successful, here {dst_folder}")

    except Exception as e:
        print(f"Bootstrapper error: {e}")
        updater_logger.error(f"Bootstrapper error: {e}")












if __name__ == '__main__':
    bootstrapper()
