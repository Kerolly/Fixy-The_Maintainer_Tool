# version_manager.py
from utils.logging_config import updater_logger
from packaging import version
from core.generate_path import get_base_path
import json
import requests



def check_versions(local_data='', remote_data='', version_for=''):

    """
    Checking the local and remote versions
    :param version_for: updater/ fixy/ bootstrapper
    :param local_data: local version of, default = getting automate version
    :param remote_data: remote version, default = getting automate version
    :return: tuple(True/False, download_link, local_version, remote_version)
    """

    global version_remote, version_local, download_link
    local_data_bool = False
    remote_data_bool = False

    if local_data == '':
        local_data = get_local_version()
        #print(f"[Debug] Local version: {local_data}")
        #updater_logger.debug(f"Local version: {local_data}")

    if remote_data == '':
        remote_data = get_remote_version()
        #print(f"[Debug] Remote version: {remote_data}")
        #updater_logger.debug(f"Remote version: {remote_data}")


    if version_for == '':
        updater_logger.warning("version_for cannot be empty")
        raise Exception("version_for cannot be empty")
    elif version_for == 'updater':
        target = 'updater'
    elif version_for == 'fixy':
        target = 'fixy'
    elif version_for == 'bootstrapper':
        target = 'bootstrapper'
    else:
        updater_logger.error(f"Unknown version for: {version_for}")
        raise Exception(f"Unknown version for: {version_for}")


    # get the local versions
    if local_data:
        version_local = local_data.get(f"{target}_version")
        local_data_bool = True

    # get the remote versions
    if remote_data:
        version_remote = remote_data.get(f"{target}_version")
        download_link = remote_data.get(f"{target}_zip_url")
        remote_data_bool = True

    # checking if is an update
    if local_data_bool == True and remote_data_bool == True:
        if version.parse(version_remote) > version.parse(version_local):
            updater_logger.info(f"Update available for {target}, version: {version_remote}")
            print(f"Update available for {target}")

            return True, download_link, version_local, version_remote

        else:
            updater_logger.info(f"Update not available for {target}")
            print(f"No update for {target} !")

            return False, download_link, version_local, version_remote

    else:
        raise Exception(f"Versions data corrupted \n"
                        f"Local data: {local_data}\n"
                        f"Remote data: {remote_data}\n")



def get_local_version():

    #open the json version file
    try:
        local_version_path = get_base_path("versions.json")
        with open(local_version_path, "r") as f:
            local_data = json.load(f)
            updater_logger.info("Successfully read versions.json") #logging
    except FileNotFoundError:
        local_data = None
        updater_logger.error("No versions.json found") #logging

    return local_data



def get_remote_version():
    URL = "https://raw.githubusercontent.com/Kerolly/Fixy-The_Maintainer_Tool/main/versions.json"
    response = requests.get(URL)

    if response.status_code == 200:
        remote_data = response.json()
        updater_logger.info("Server response: OK, getting the data") #logging

    else:
        updater_logger.error(f"Server response: {response.status_code}") #logging
        remote_data = None

    return remote_data

def update_local_version(version_for, new_version, json_path=''):
    """

    :param version_for: updater/ fixy/ bootstrapper
    :param new_version: New version from remote server
    :param json_path: Path for the json file

    Updates the local version of the json file \n
    If json_path is empty, is getting automated path for the json file
    """

    # Getting auto json path
    if json_path == '':
        json_path = get_base_path("versions.json")

    # Prepare the target to write new version
    if version_for == 'updater':
        target = "updater_version"
    elif version_for == 'fixy':
        target = "fixy_version"
    elif version_for == 'bootstrapper':
        target = "bootstrapper_version"
    else:
        raise Exception(f"Unknown version for: {version_for} to update the local version json")

    print(f"Updating local version json for {target}")
    updater_logger.info(f"Updating local version for {target}")

    try:
        with open(json_path, "r") as f:
            data = json.load(f)

        data[target] = new_version # write the new version in json

        with open(json_path, "w") as f:
            json.dump(data, f)

        print(f"Successfully updated local version json for {target}")
        updater_logger.info(f"Successfully updated local version for {target}")

    except Exception as e:
        print(f"Error updating local version json for {target}: {e}")
        updater_logger.error(f"Error updating local version json for {target}: {e}")


# Testing
#check_versions(get_local_version(), get_remote_version(), version_for='updater')
#update_local_version("updater", "0.2")