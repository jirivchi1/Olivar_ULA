from utils.serial_connection import connect_serial, read_battery_data
from utils.camera import take_photo_yellow
from utils.server_upload import upload_to_server_yellow, delete_photos_yellow
from utils.logger import log_action
from utils.monitoring import send_monitoring_data_yellow
from utils.shutdown import shutdown_system


def main():
    try:
        ser = connect_serial()
        filepath, filename = take_photo_yellow()

        # Leer datos de la batería desde Arduino
        bateriaArduino, bateriaPi = read_battery_data(ser)

        # Enviar datos de monitorización con los argumentos especificados
        send_monitoring_data_yellow(
            filename=filename,
            bateriaArduino=bateriaArduino,
            bateriaPi=bateriaPi,
        )

        # Subir archivos al servidor
        upload_to_server_yellow()
        # Eliminar fotos después de subirlas
        delete_photos_yellow()

        # Apagar el sistema
        # shutdown_system()

    except Exception as e:
        log_action(f"Error en el proceso principal: {e}")


if __name__ == "__main__":
    main()
