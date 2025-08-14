#version_checker
from utils.logging_config import updater_logger
from utils.versions_getter import get_local_version, get_remote_version
from packaging import version



def check_versions(local_data, remote_data):

    global updater_version_remote, updater_version_local
    local_data_bool = False
    remote_data_bool = False

    # get the local versions
    if local_data:
        updater_version_local = local_data.get("updater_version")
        local_data_bool = True

    # get the remote versions
    if remote_data:
        updater_version_remote = remote_data.get("updater_version")
        updater_link = remote_data.get("updater_link")
        remote_data_bool = True

    # checking if is an update
    if local_data_bool == True and remote_data_bool == True:
        if version.parse(updater_version_remote) > version.parse(updater_version_local):
            updater_logger.info("Update available")
            print("Update disponibil")

            # return a true value + link for download
        else:
            updater_logger.info("Update not available")
            print("Nu este update!")

            # return a false value
    else:
        updater_logger.error("Versions data corrupted")



check_versions(get_local_version(), get_remote_version())