import os
import subprocess
from datetime import datetime
from utils.logger import log_action

def take_photo(local_directory, archivo, name_foto):
    os.makedirs(local_directory, exist_ok=True)
    filename = datetime.now().strftime("%Y%m%d_%H%M%S") + name_foto + ".jpg"
    filepath = os.path.join(local_directory, filename)
    
    try:
        # Intentar tomar la foto
        subprocess.run(["fswebcam", "-r", "1280x720", "--no-banner", filepath], check=True)
        
        # Verificar si el archivo se creó
        if os.path.exists(filepath):
            log_action(f"Photo {filename} successfully taken and saved to {filepath}.", archivo)
            return filepath, filename
        else:
            log_action(f"Photo {filename} could not be saved despite no errors.", archivo)
            return None, None
    except subprocess.CalledProcessError as e:
        log_action(f"Failed to take photo {filename}. Error: {str(e)}", archivo)
        return None, None
    except Exception as e:
        log_action(f"Unexpected error while taking photo {filename}. Error: {str(e)}", archivo)
        return None, None
