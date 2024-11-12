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
        log_action(f"1.Photo {filename} taken.")

        # Leer datos del sensor de temperatura y humedad
        temp, humid = read_sensor_data()

        # Leer datos de la batería desde Arduino
        bateriaArduino, bateriaPi = read_battery_data(ser)

        # Enviar datos de monitorización, utilizando valores predeterminados si es necesario
        if temp is None or humid is None:
            temp, humid = -1, -1  # Valores predeterminados si el sensor falló
        
        # Subir archivos al servidor
        upload_to_server()

        # Enviar datos de monitorización con los argumentos especificados
        # send_monitoring_data(
        #     filename=filename,
        #     temp=temp,
        #     humid=humid,
        #     bateriaArduino=bateriaArduino,
        #     bateriaPi=bateriaPi,
        # )

        # Eliminar fotos después de subirlas
        delete_photos()
        log_action("2.Fotos eliminadas después de subirlas.")

        # Apagar el sistema
        shutdown_system()
        log_action("Sistema apagado correctamente")

    except Exception as e:
        log_action(f"Error en el proceso principal: {e}")


if __name__ == "__main__":
    main()
