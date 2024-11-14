import os
from datetime import datetime
from config import METRICS_DIRECTORY


def log_action_banda(message):
    with open(f"{METRICS_DIRECTORY}/log_banda.txt", "a") as log_file:
        log_file.write(f"{datetime.now()}: {message}\n")


def log_action_yellow(message):
    with open(f"{METRICS_DIRECTORY}/log_yellow.txt", "a") as log_file:
        log_file.write(f"{datetime.now()}: {message}\n")


def log_action_green(message):
    with open(f"{METRICS_DIRECTORY}/log_green.txt", "a") as log_file:
        log_file.write(f"{datetime.now()}: {message}\n")


def log_action(message, arhivo):
    with open(f"{METRICS_DIRECTORY}/{arhivo}", "a") as log_file:
        log_file.write(f"{datetime.now()}: {message}\n")
