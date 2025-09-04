# version_checker.py
from utils.logging_config import updater_logger
from utils.versions_getter import get_local_version, get_remote_version
from packaging import version



def check_versions(local_data, remote_data, version_for=''):

    """
    Checking the local and remote versions
    :param version_for: updater/ fixy/ bootstrapper
    :param local_data: local version of Updater
    :param remote_data: remote version of Updater
    :return: tuple(True/False, updater_link, local_version, remote_version)
    """

    global version_remote, version_local, updater_link
    local_data_bool = False
    remote_data_bool = False

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
        updater_link = remote_data.get(f"{target}_version")
        remote_data_bool = True

    # checking if is an update
    if local_data_bool == True and remote_data_bool == True:
        if version.parse(version_remote) > version.parse(version_local):
            updater_logger.info(f"Update available for {target}, version: {version_remote}")
            print(f"Update available for {target}")

            return True, updater_link, version_local, version_remote

        else:
            updater_logger.info(f"Update not available for {target}")
            print(f"No update for {target} !")

            return False, updater_link, version_local, version_remote

    else:
        updater_logger.error("Versions data corrupted")
        raise Exception("Versions data corrupted")


# Testing
#check_versions(get_local_version(), get_remote_version(), version_for='updater')