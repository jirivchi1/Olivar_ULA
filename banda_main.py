from utils.serial_connection import connect_serial, read_battery_data
from utils.camera import take_photo
from utils.sensors import read_sensor_data
from utils.server_upload import upload_to_server_banda, delete_photos_banda
from utils.logger import log_action
from utils.monitoring import send_monitoring_data_banda
from utils.shutdown import shutdown_system


def main():
    try:
        ser = connect_serial()
        filepath, filename = take_photo()

        # Leer datos del sensor de temperatura y humedad
        temp, humid = read_sensor_data()

        # Leer datos de la batería desde Arduino
        bateriaArduino, bateriaPi = read_battery_data(ser)

        # Enviar datos de monitorización con los argumentos especificados
        send_monitoring_data_banda(
            filename=filename,
            temp=temp,
            humid=humid,
            bateriaArduino=bateriaArduino,
            bateriaPi=bateriaPi,
        )

        # Subir archivos al servidor
        upload_to_server_banda()
        # Eliminar fotos después de subirlas
        delete_photos_banda()

        # Apagar el sistema
        # shutdown_system()

    except Exception as e:
        log_action(f"Error en el proceso principal: {e}")


if __name__ == "__main__":
    main()
