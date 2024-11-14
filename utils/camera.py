import os
import subprocess
from datetime import datetime
from config import LOCAL_DIRECTORY_BANDA, LOCAL_DIRECTORY_YELLOW, LOCAL_DIRECTORY_GREEN
from utils.logger import log_action


def take_photo_banda():
    os.makedirs(LOCAL_DIRECTORY_BANDA, exist_ok=True)
    filename = datetime.now().strftime("%Y%m%d_%H%M%S") + "_banda_RP06" + ".jpg"
    filepath = f"{LOCAL_DIRECTORY_BANDA}/{filename}"
    subprocess.run(["fswebcam", "-r", "1280x720", "--no-banner", filepath], check=True)
    log_action(f"Photo {filename} taken.")

    return filepath, filename


def take_photo_yellow():
    os.makedirs(LOCAL_DIRECTORY_YELLOW, exist_ok=True)
    filename = datetime.now().strftime("%Y%m%d_%H%M%S") + "_banda_RP06" + ".jpg"
    filepath = f"{LOCAL_DIRECTORY_YELLOW}/{filename}"
    subprocess.run(["fswebcam", "-r", "1280x720", "--no-banner", filepath], check=True)
    log_action(f"Photo {filename} taken.")

    return filepath, filename


def take_photo_green():
    os.makedirs(LOCAL_DIRECTORY_GREEN, exist_ok=True)
    filename = datetime.now().strftime("%Y%m%d_%H%M%S") + "_banda_RP06" + ".jpg"
    filepath = f"{LOCAL_DIRECTORY_GREEN}/{filename}"
    subprocess.run(["fswebcam", "-r", "1280x720", "--no-banner", filepath], check=True)
    log_action(f"Photo {filename} taken.")

    return filepath, filename
