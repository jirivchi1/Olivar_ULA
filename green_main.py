from utils.serial_connection import connect_serial, read_battery_data
from utils.camera import take_photo
from utils.server_upload import upload_to_server, delete_photos
from utils.logger import log_action
from config import SERVER_DIR_GREEN

from utils.monitoring import send_monitoring_data_green
from utils.shutdown import shutdown_system

import os

# Obtener el directorio base dinámicamente
LOCAL_DIRECTORY_GREEN = os.path.join(os.path.expanduser("~"), "olivarv2", "fotos_green")
os.makedirs(LOCAL_DIRECTORY_GREEN, exist_ok=True)


def main():
    try:
        ser = connect_serial()

        filepath, filename = take_photo(
            LOCAL_DIRECTORY_GREEN, "log_green.txt", "_verde_1"
        )
        
        if filepath is None or filename is None:
            log_action("No se pudo tomar la foto; se omitirán pasos relacionados con ella.", "log_green.txt")
    
        # Subir archivos al servidor
        upload_to_server(SERVER_DIR_GREEN, LOCAL_DIRECTORY_GREEN, "log_green.txt")

        # Leer datos de la batería desde Arduino
        bateriaArduino, bateriaPi = read_battery_data(ser, "log_green.txt")

        # Enviar datos de monitorización con los argumentos especificados
        send_monitoring_data_green(
            filename=filename,
            bateriaArduino=bateriaArduino,
            bateriaPi=bateriaPi,
            archivo="log_green.txt",
        )

        # Eliminar fotos después de subirlas
        delete_photos(LOCAL_DIRECTORY_GREEN, "log_green.txt")

        # Apagar el sistema
        shutdown_system()

    except Exception as e:
        log_action(f"Error en el proceso principal: {e}", "log_green.txt")


if __name__ == "__main__":
    main()
