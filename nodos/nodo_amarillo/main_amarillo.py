from utils.serial_connection import connect_serial, read_battery_data
from utils.camera import take_photo
from utils.sensors import read_sensor_data
from utils.server_upload import upload_to_server, delete_photos
from utils.logger import log_action
from utils.monitoring import send_monitoring_data
from utils.shutdown import shutdown_system


def main():
    try:
        ser = connect_serial()
        filepath, filename = take_photo()

        # Leer datos de la batería desde Arduino
        bateriaArduino, bateriaPi = read_battery_data(ser)

        # Usar valores predeterminados si no se han leído valores válidos de la batería
        if bateriaArduino == -1 or bateriaPi == -1:
            log_action("Usando valores predeterminados para la batería.")

        # Enviar datos de monitorización con los argumentos especificados
        # send_monitoring_data(
        #     filename=filename,
        #     bateriaArduino=bateriaArduino,
        #     bateriaPi=bateriaPi,
        # )

        # Subir archivos al servidor
        upload_to_server()
        # Eliminar fotos después de subirlas
        delete_photos()

        # Apagar el sistema
        # shutdown_system()

    except Exception as e:
        log_action(f"Error en el proceso principal: {e}")


if __name__ == "__main__":
    main()
