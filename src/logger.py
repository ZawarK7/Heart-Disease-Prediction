import logging 
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_directory = os.path.join(os.getcwd(), "logs")  # Directory where log files will be stored
os.makedirs(logs_directory, exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_directory, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
