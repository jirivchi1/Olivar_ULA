from utils.serial_connection import connect_serial, read_battery_data
from utils.camera import take_photo
from utils.sensors import read_sensor_data
from utils.server_upload import upload_to_server, delete_photos
from utils.logger import log_action
from config import SERVER_DIR_BANDA

from utils.monitoring import send_monitoring_data_banda
from utils.shutdown import shutdown_system

import os

# Obtener el directorio base dinámicamente
LOCAL_DIRECTORY_BANDA = os.path.join(os.path.expanduser("~"), "olivarv2", "fotos_banda")
os.makedirs(LOCAL_DIRECTORY_BANDA, exist_ok=True)


def main():
    try:
        ser = connect_serial()

        filepath, filename = take_photo(
            LOCAL_DIRECTORY_BANDA, "log_banda.txt", "_banda_RP06"
        )

        # Subir archivos al servidor
        upload_to_server(SERVER_DIR_BANDA, LOCAL_DIRECTORY_BANDA, "log_banda.txt")

        # Leer datos del sensor de temperatura y humedad
        temp, humid = read_sensor_data("log_banda.txt")

        # Leer datos de la batería desde Arduino
        bateriaArduino, bateriaPi = read_battery_data(ser, "log_banda.txt")

        log_action(
            f"Valores bateria Pi:{bateriaPi}, arduino: {bateriaArduino}",
            "log_banda.txt",
        )

        # Enviar datos de monitorización con los argumentos especificados
        send_monitoring_data_banda(
            filename=filename,
            temp=temp,
            humid=humid,
            bateriaArduino=bateriaArduino,
            bateriaPi=bateriaPi,
            archivo="log_banda.txt",
        )

        # Eliminar fotos después de subirlas
        delete_photos(LOCAL_DIRECTORY_BANDA, "log_banda.txt")

        # Apagar el sistema
        # shutdown_system()

    except Exception as e:
        log_action(f"Error en el proceso principal: {e}", "log_banda.txt")


if __name__ == "__main__":
    main()
