import os
import subprocess
from datetime import datetime
from utils.logger import log_action


def take_photo(local_directory, archivo, name_foto):
    try:
        # Crear el directorio si no existe
        os.makedirs(local_directory, exist_ok=True)
        
        # Crear el nombre y ruta del archivo
        filename = datetime.now().strftime("%Y%m%d_%H%M%S") + name_foto + ".jpg"
        filepath = f"{local_directory}/{filename}"
        
        # Intentar tomar la foto con fswebcam
        subprocess.run(["fswebcam", "-r", "1280x720", "--no-banner", filepath], check=True)
        
        # Registrar en el log si la foto se tomó correctamente
        log_action(f"Photo {filename} taken.", archivo)
        return filepath, filename

    except subprocess.CalledProcessError as e:
        # Capturar errores relacionados con fswebcam
        error_message = f"{datetime.now()}: Error al tomar la foto - {str(e)}"
        log_action(error_message, archivo)
        print(error_message)
        return None, None

    except Exception as e:
        # Capturar cualquier otro tipo de error
        error_message = f"{datetime.now()}: Error inesperado - {str(e)}"
        log_action(error_message, archivo)
        print(error_message)
        return None, None
