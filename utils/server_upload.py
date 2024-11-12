import os
import subprocess
from config import SERVER_USER, SERVER_IP, SERVER_DIR, LOCAL_DIRECTORY, SENSOR_DATA_FILE


def upload_to_server():
    try:
        for filename in os.listdir(LOCAL_DIRECTORY):
            filepath = os.path.join(LOCAL_DIRECTORY, filename)
            if filename.endswith(".jpg"):
                subprocess.run(
                    ["scp", filepath, f"{SERVER_USER}@{SERVER_IP}:{SERVER_DIR}"],
                    check=True,
                )
                print(f"Image {filename} uploaded to the server.")
        subprocess.run(
            [
                "scp",
                SENSOR_DATA_FILE,
                f"{SERVER_USER}@{SERVER_IP}:{SERVER_DIR}/datos_sensor.txt",
            ],
            check=True,
        )
        print("Sensor data uploaded to the server.")
        print("All images and sensor data uploaded.")
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
    except Exception as e:
        raise RuntimeError(f"Error al eliminar las fotos: {e}")
