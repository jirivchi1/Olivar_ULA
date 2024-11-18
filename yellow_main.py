from utils.serial_connection import connect_serial, read_battery_data
from utils.camera import take_photo
from utils.server_upload import upload_to_server, delete_photos
from utils.logger import log_action
from utils.monitoring import send_monitoring_data_yellow
from utils.shutdown import shutdown_system
from config import LOCAL_DIRECTORY_YELLOW, SERVER_DIR_YELLOW


def main():
    try:
        ser = connect_serial()

        filepath, filename = take_photo(
            LOCAL_DIRECTORY_YELLOW, "log_yellow.txt", "_yellow_RP04"
        )

        # Subir archivos al servidor
        upload_to_server(SERVER_DIR_YELLOW, LOCAL_DIRECTORY_YELLOW, "log_yellow.txt")

        # Leer datos de la batería desde Arduino
        bateriaArduino, bateriaPi = read_battery_data(ser, "log_yellow.txt")

        # Enviar datos de monitorización con los argumentos especificados
        send_monitoring_data_yellow(
            filename=filename,
            bateriaArduino=bateriaArduino,
            bateriaPi=bateriaPi,
            archivo="log_yellow.txt",
        )

        # Eliminar fotos después de subirlas
        delete_photos(LOCAL_DIRECTORY_YELLOW, "log_yellow.txt")

        # Apagar el sistema
        shutdown_system()

    except Exception as e:
        log_action(f"Error en el proceso principal: {e}", "log_yellow.txt")


if __name__ == "__main__":
    main()
