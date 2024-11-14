import os
import subprocess
from datetime import datetime
from utils.logger import log_action


def take_photo(local_directory, archivo, name_foto):
    os.makedirs(local_directory, exist_ok=True)
    filename = datetime.now().strftime("%Y%m%d_%H%M%S") + {name_foto} + ".jpg"
    filepath = f"{local_directory}/{filename}"
    subprocess.run(["fswebcam", "-r", "1280x720", "--no-banner", filepath], check=True)
    log_action(f"Photo {filename} taken.", archivo)
    print("foto hecha")
    return filepath, filename
