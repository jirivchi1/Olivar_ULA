import os
import subprocess
from datetime import datetime
from config import LOCAL_DIRECTORY
from utils.logger import log_action


def take_photo():
    os.makedirs(LOCAL_DIRECTORY, exist_ok=True)
    filename = datetime.now().strftime("%Y%m%d_%H%M%S") + "_banda_RP06" + ".jpg"
    filepath = f"{LOCAL_DIRECTORY}/{filename}"
    subprocess.run(["fswebcam", "-r", "1280x720", "--no-banner", filepath], check=True)
    log_action(f"Photo {filename} taken.")

    return filepath, filename
