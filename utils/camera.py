import cv2
import datetime

def take_photo():
    try:
        # Intentar abrir la cámara
        camera = cv2.VideoCapture(0)  # /dev/video0

        if not camera.isOpened():
            raise Exception("Error: Cámara no encontrada o no disponible.")
        
        # Leer un frame de la cámara
        ret, frame = camera.read()
        if not ret:
            raise Exception("Error: No se pudo capturar una imagen.")
        
        # Generar un nombre de archivo con la fecha y hora actual
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{timestamp}_banda_RP06.jpg"
        
        # Guardar la imagen
        cv2.imwrite(filename, frame)
        print(f"Foto {filename} tomada.")
        
        # Liberar la cámara
        camera.release()
        
        return filename

    except Exception as e:
        # Manejo de errores
        error_message = f"{datetime.datetime.now()}: {str(e)}"
        print(error_message)
        
        # Escribir el error en un archivo de log
        with open("log_banda.txt", "a") as log_file:
            log_file.write(error_message + "\n")
        return None

if __name__ == "__main__":
    photo = take_photo()
    if photo:
        print(f"Foto guardada como {photo}.")
    else:
        print("No se pudo tomar la foto.")
