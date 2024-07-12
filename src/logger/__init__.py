import logging    # record the messega like errors
import os, sys    # intract with the system and files
from datetime import datetime  # 


LOG_DIR = 'logs'
LOG_DIR = os.path.join(os.getcwd(), LOG_DIR)

os.makedirs(LOG_DIR, exist_ok=True) 

CURRENT_TIME_STAMP = f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"
file_name = f"log_{CURRENT_TIME_STAMP}.log"


log_file_path = os.path.join(LOG_DIR, file_name)
# This combines the path to logs directory

logging.basicConfig(filename = log_file_path,
                    filemode= "w",
                    format ='[%(asctime)s] %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO )
                    # logging configuration

