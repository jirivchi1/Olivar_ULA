import os
import shutil
import subprocess
from datetime import datetime
from utils.logger import log_action

def take_photo(local_directory, archivo, name_foto):
    os.makedirs(local_directory, exist_ok=True)  # Crear la carpeta local si no existe
    
    # Obtener el directorio base del usuario actual
    home_directory = os.path.expanduser("~")
    backup_directory = os.path.join(home_directory, "photos_backup")  # Directorio de respaldo dinámico
    os.makedirs(backup_directory, exist_ok=True)  # Crear la carpeta de respaldo si no existe

   # Obtener fecha y hora actuales con milisegundos
    now = datetime.now()
    timestamp = now.strftime("%Y%m%d_%H%M%S") + f"_{now.microsecond//1000:03d}" + name_foto + ".jpg"
    
    filepath = os.path.join(local_directory, timestamp)
    backup_filepath = os.path.join(backup_directory, timestamp)

    try:
        # Intentar tomar la foto
        subprocess.run(["libcamera-jpeg","--nopreview", "-o", filepath, "--width","3280","--height","2464"], check=True)
        
        # Verificar si el archivo se creó
        if os.path.exists(filepath):
            # Copiar la foto al directorio de respaldo
            shutil.copy(filepath, backup_filepath)
            log_action(f"Photo {filename} successfully taken and saved to {filepath}. Backup saved to {backup_filepath}.", archivo)
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
