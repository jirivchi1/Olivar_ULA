import os
import shutil
import subprocess
from datetime import datetime
from utils.logger import log_action

def take_photo(local_directory, archivo, name_foto):
    print(f"Creando directorio local: {local_directory}")
    os.makedirs(local_directory, exist_ok=True)  # Crear la carpeta local si no existe
    
    # Obtener el directorio base del usuario actual
    home_directory = os.path.expanduser("~")
    print(f"Directorio base del usuario actual: {home_directory}")
    backup_directory = os.path.join(home_directory, "photos_backup")  # Directorio de respaldo dinámico
    print(f"Creando directorio de respaldo: {backup_directory}")
    os.makedirs(backup_directory, exist_ok=True)  # Crear la carpeta de respaldo si no existe

    filename = datetime.now().strftime("%Y%m%d_%H%M%S") + name_foto + ".jpg"
    filepath = os.path.join(local_directory, filename)
    backup_filepath = os.path.join(backup_directory, filename)
    print(f"Nombre del archivo: {filename}")
    print(f"Ruta completa del archivo: {filepath}")
    print(f"Ruta de respaldo: {backup_filepath}")

    try:
        print("Intentando tomar la foto...")
        subprocess.run(["fswebcam", "-r", "1280x720", "--no-banner", filepath], check=True)
        
        # Verificar si el archivo se creó
        if os.path.exists(filepath):
            print(f"Archivo creado exitosamente: {filepath}")
            # Copiar la foto al directorio de respaldo
            shutil.copy(filepath, backup_filepath)
            print(f"Archivo copiado a la carpeta de respaldo: {backup_filepath}")
            log_action(f"Photo {filename} successfully taken and saved to {filepath}. Backup saved to {backup_filepath}.", archivo)
            return filepath, filename
        else:
            print(f"El archivo no se creó: {filepath}")
            log_action(f"Photo {filename} could not be saved despite no errors.", archivo)
            return None, None
    except subprocess.CalledProcessError as e:
        print(f"Error al tomar la foto: {e}")
        log_action(f"Failed to take photo {filename}. Error: {str(e)}", archivo)
        return None, None
    except Exception as e:
        print(f"Error inesperado: {e}")
        log_action(f"Unexpected error while taking photo {filename}. Error: {str(e)}", archivo)
        return None, None
