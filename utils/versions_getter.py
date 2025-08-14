# versions_getter
import json
import requests
from utils.logging_config import updater_logger


'''
-----------------------------------------------------------------
Example of use:
from utils.versions_getter import get_local_version, get_remote_version
-----------------------------------------------------------------
'''



def get_local_version():

    #open the json version file
    try:
        with open("../versions.json", "r") as f:
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