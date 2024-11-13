import os
import subprocess
from utils.logger import log_action


from config import (
    SERVER_USER,
    SERVER_IP,
    SERVER_DIR,
    LOCAL_DIRECTORY,
    SENSOR_DATA_FILE,
    METRICS_DIRECTORY,
)


def upload_to_server():
    try:
        # Subir todas las imágenes en el directorio LOCAL_DIRECTORY
        for filename in os.listdir(LOCAL_DIRECTORY):
            filepath = os.path.join(LOCAL_DIRECTORY, filename)
            if filename.endswith(".jpg"):
                subprocess.run(
                    ["scp", filepath, f"{SERVER_USER}@{SERVER_IP}:{SERVER_DIR}"],
                    check=True,
                )
                print(f"Image {filename} uploaded to the server.")

        # Subir datos del sensor
        subprocess.run(
            [
                "scp",
                SENSOR_DATA_FILE,
                f"{SERVER_USER}@{SERVER_IP}:{SERVER_DIR}/datos_sensor.txt",
            ],
            check=True,
        )
        print("Sensor data uploaded to the server.")

        # Subir archivo de log_banda.txt
        log_file_path = os.path.join(METRICS_DIRECTORY, "log_banda.txt")
        subprocess.run(
            [
                "scp",
                log_file_path,
                f"{SERVER_USER}@{SERVER_IP}:{SERVER_DIR}/log_banda.txt",
            ],
            check=True,
        )
        print("Log file uploaded to the server.")

        print("All images, sensor data, and log file uploaded.")

    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"Error al subir archivos al servidor: {e}")


def delete_photos():
    try:
        for filename in os.listdir(LOCAL_DIRECTORY):
            filepath = os.path.join(LOCAL_DIRECTORY, filename)
            if filename.endswith(".jpg"):
                os.remove(filepath)
                print(f"Image {filename} deleted.")
        print("All images deleted.")
        log_action("Fotos eliminadas después de subirlas.")

    except Exception as e:
        raise RuntimeError(f"Error al eliminar las fotos: {e}")
