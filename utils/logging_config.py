# logging_config.py
import logging
from core.generate_path import get_base_path
import os

'''
-----------------------------------------------------------------
Example of use:
from utils.logger_config import app_logger, updater_logger
-----------------------------------------------------------------
'''


APP_LOG_FILE_PATH = get_base_path("Logging/app.log") #full abs path for app log
UPDATER_LOG_FILE_PATH = get_base_path("Logging/updaters.log") #full abs path for updaters log

logging.basicConfig(level=logging.DEBUG,
                    handlers=[])

#file size checking
def file_size_check(log_file_path):
    # get the size of log file
    if os.path.getsize(log_file_path) >= 1048576: # 1048576Bytes -> 1Mb
        os.remove(log_file_path)



#log file check if exist
def log_file_check(log_file_path):
    if not os.path.exists(log_file_path):
        with open(log_file_path, "x") as log_file:
            log_file.close()
            return True
    return False


def setup_updater_logger():

    updater_logger = logging.getLogger("updater_logger")
    updater_file_handler = logging.FileHandler(UPDATER_LOG_FILE_PATH, encoding="utf-8")

    updater_formatter = logging.Formatter("\n%(asctime)s: [%(levelname)s]: "
                                          "\n[File: %(module)s-%(lineno)d]: %(message)s",
                                          datefmt="%Y-%m-%d %H:%M:%S")

    updater_file_handler.setFormatter(updater_formatter)
    updater_logger.addHandler(updater_file_handler)

    return updater_logger


def setup_app_logger():
    app_logger = logging.getLogger("app_logger")
    app_file_handler = logging.FileHandler(APP_LOG_FILE_PATH, encoding="utf-8")

    app_formatter = logging.Formatter("\n%(asctime)s: [%(levelname)s]: "
                                      "\n[File: %(module)s-%(lineno)d]: %(message)s",
                                      datefmt="%Y-%m-%d %H:%M:%S")

    app_file_handler.setFormatter(app_formatter)
    app_logger.addHandler(app_file_handler)

    return app_logger


#-------------------------------------------
'''Create loggers for use'''

#call the file size and exist checkers
log_file_check(APP_LOG_FILE_PATH)
file_size_check(APP_LOG_FILE_PATH)

#initialization app_logger
app_logger = setup_app_logger()
app_logger.debug("Initializing the app logger")

try:
    x = 1/0
except Exception as e:
    app_logger.error(f"Error {e}")


#-------------------------------------------
#call the file size and exist checkers
log_file_check(UPDATER_LOG_FILE_PATH)
file_size_check(UPDATER_LOG_FILE_PATH)

# initialization updater_logger
updater_logger = setup_updater_logger()
updater_logger.debug("Initializing the updater logger")





