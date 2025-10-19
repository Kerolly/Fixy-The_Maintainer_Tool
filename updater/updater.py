# updater.py
import os
import sys
import psutil

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) # added to sys.path
from updater_ui.popups import *
from utils.logging_config import updater_logger
from utils.version_manager import check_versions, update_local_version
from utils.file_manager import download_file, unzip, deploy_files
from utils.generate_path import get_base_path


def updater():
    print("\nChecking for update ...")
    updater_logger.info("Checking for update ...")

    try:
        version_results = check_versions(version_for="fixy")
        #print(version_results)

        if version_results[0]:
            answer = create_update_found_window()

            if answer:
                print("\nUpdater started ...")
                updater_logger.info("Updater started ...")

                # closing the fixy, main app
                close_fixy()

                # creating the loading pop up ui
                create_loading_window()

                # get the returns from download function
                downloaded_results = download_file(version_results[1])
                #print(downloaded_results)

                if downloaded_results[0] == True:
                    print("Download successful, fixy")
                    updater_logger.info("Download successful, fixy")
                    # getting the path for zip file
                    zip_file_path = downloaded_results[1]

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
                            update_local_version(version_for="fixy", new_version=version_results[3])

                            # creating the finish pop up ui
                            create_finish_window()

            else:
                print("Update refused, by user")
                updater_logger.info("Update refused, by user")
                return 1

    except Exception as e:
        print(f"\nError occurred while updating Fixy ... {e}")
        updater_logger.error(f"Error occurred while updating Fixy ... {e}")


def close_fixy():
    closed = False
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            if proc.info['name'] and 'Fixy.exe' in proc.info['name']:
                proc.terminate()  # send shut down signal
                proc.wait(5)      # wait 5 sec
                closed = True
                updater_logger.info(f"Closed {proc.info['name']}")
                print("[INFO] Fixy.exe was closed.")
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass
    if not closed:
        print("[INFO] Fixy.exe not running.")
        updater_logger.info("Fixy.exe not running.")


def updater_bootstrapper():
    print("\nChecking bootstrapper for update ...")
    updater_logger.info("\nChecking bootstrapper for update ...")

    try:
        version_results = check_versions(version_for="bootstrapper")

        if version_results[0]:
            print("\nUpdater bootstrapper started ...")
            updater_logger.info("Updater bootstrapper started ...")

            # get the returns from download function
            downloaded_results = download_file(version_results[1])
            # print(downloaded_results)

            if downloaded_results[0] == True:
                print("Download successful, bootstrapper")
                updater_logger.info("Download successful, bootstrapper")
                # getting the path for zip file
                zip_file_path = downloaded_results[1]

                # getting the results from unzipping
                success_unzip, unzipped_path = unzip(zip_file_path)
                if success_unzip:
                    print(f"Unzip successful {unzipped_path}")
                    updater_logger.info(f"Unzip successful {unzipped_path}")

                    # getting the dst folder for updater
                    dst_folder = get_base_path("")  # root of the app
                    if deploy_files(unzipped_path, dst_folder, copy_entire_folder=False):
                        print(f"Deploy successful, here {dst_folder}")
                        updater_logger.info(f"Deploy successful, here {dst_folder}")

                        # writing the new version to json
                        update_local_version(version_for="bootstrapper", new_version=version_results[3])

    except Exception as e:
        print(f"\nError occurred while updating bootstrapper ... {e}")
        updater_logger.error(f"Error occurred while updating bootstrapper ... {e}")


if __name__ == "__main__":
    updater()
    updater_bootstrapper()