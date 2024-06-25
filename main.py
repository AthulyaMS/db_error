# import requests
# import logging
# from datetime import datetime
# import time

# # Configuration
# URL = "https://stagingapi.vachanengine.org/"  
# CHECK_INTERVAL = 600  # Check every 60 seconds

# # Set up logging
# logging.basicConfig(filename='staging_status.log', level=logging.INFO,
#                     format='%(asctime)s - %(levelname)s - %(message)s')

# def check_staging():
#     logging.debug("Starting a new check...")
#     try:
#         response = requests.get(URL)
#         if response.status_code == 200:
#             logging.info("Staging is UP")
#         else:
#             logging.warning(f"Staging is DOWN - Status Code: {response.status_code}")
#     except requests.ConnectionError:
#         logging.error("Staging is DOWN - Connection Error")
#     except Exception as e:
#         logging.error(f"An error occurred: {e}")

# def main():
#     logging.info("Starting staging status checker...")
#     while True:
#         check_staging()
#         logging.debug("Sleeping for the next interval...")
#         time.sleep(CHECK_INTERVAL)

# if __name__ == "__main__":
#     main()

import requests
import logging
from datetime import datetime
import time

# Configuration
URL = "https://stagingapi.vachanengine.org/"  
CHECK_INTERVAL = 600  # Check every 10 minutes (600 seconds)

# Set up general logging to 'staging_status.log'
general_handler = logging.FileHandler('staging_status.log')
general_handler.setLevel(logging.INFO)
general_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
general_handler.setFormatter(general_formatter)

# Set up error logging to 'staging_errors.log'
error_handler = logging.FileHandler('staging_errors.log')
error_handler.setLevel(logging.ERROR)
error_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
error_handler.setFormatter(error_formatter)

# Get the root logger and configure it
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logger.addHandler(general_handler)
logger.addHandler(error_handler)

def check_staging():
    logger.debug("Starting a new check...")
    try:
        response = requests.get(URL)
        if response.status_code == 200:
            logger.info("Staging is UP")
        else:
            logger.warning(f"Staging is DOWN - Status Code: {response.status_code}")
    except requests.ConnectionError:
        logger.error("Staging is DOWN - Connection Error")
    except Exception as e:
        logger.error(f"An error occurred: {e}")

def main():
    logger.info("Starting staging status checker...")
    while True:
        check_staging()
        logger.debug("Sleeping for the next interval...")
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    main()
