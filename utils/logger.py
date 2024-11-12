import os
from datetime import datetime
from config import METRICS_DIRECTORY


def log_action(message):
    with open(f"{METRICS_DIRECTORY}/log_banda.txt", "a") as log_file:
        log_file.write(f"{datetime.now()}: {message}\n")
