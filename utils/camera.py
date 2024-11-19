import os
import cv2
from datetime import datetime
from utils.logger import log_action


def take_photo(local_directory, archivo, name_foto):
    try:
        # Crear el directorio si no existe
        os.makedirs(local_directory, exist_ok=True)
        
        # Configurar la cámara
        camera = cv2.VideoCapture(0)  # /dev/video0 por defecto
        if not camera.isOpened():
            raise Exception("Error: Cámara no encontrada o no disponible.")
        
        # Leer un frame de la cámara
        ret, frame = camera.read()
        if not ret:
            raise Exception("Error: No se pudo capturar una imagen.")
        
        # Crear el nombre y la ruta del archivo
        filename = datetime.now().strftime("%Y%m%d_%H%M%S") + name_foto + ".jpg"
        filepath = os.path.join(local_directory, filename)
        
        # Guardar la imagen
        cv2.imwrite(filepath, frame)
        
        # Liberar la cámara
        camera.release()
        
        # Registrar en el log
        log_action(f"Photo {filename} taken.", archivo)
        return filepath, filename

    except Exception as e:
        # Manejo de errores
        error_message = f"{datetime.now()}: {str(e)}"
        log_action(error_message, archivo)
        return None, None
