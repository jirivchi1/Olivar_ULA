import os
import subprocess
from utils.logger import log_action


from config import (
    SERVER_USER,
    SERVER_IP,
    METRICS_DIRECTORY,
)


def upload_to_server(server_dir, local_dir, archivo):
    try:
        # Subir todas las imágenes en el directorio LOCAL_DIRECTORY_BANDA
        for filename in os.listdir(local_dir):
            filepath = os.path.join(local_dir, filename)
            if filename.endswith(".jpg"):
                subprocess.run(
                    ["scp", filepath, f"{SERVER_USER}@{SERVER_IP}:{server_dir}"],
                    check=True,
                )
                print(f"Image {filename} uploaded to the server.")

        # Subir archivo de log_banda.txt
        log_file_path = os.path.join(METRICS_DIRECTORY, "log_banda.txt")
        subprocess.run(
            [
                "scp",
                log_file_path,
                f"{SERVER_USER}@{SERVER_IP}:{server_dir}/log_banda.txt",
            ],
            check=True,
        )
        print("Log file uploaded to the server.")
        print("All images, sensor data, and log file uploaded.")
        log_action("All images, sensor data, and log file uploaded.", archivo)

    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"Error al subir archivos al servidor: {e}")


def delete_photos(local_dir, archivo):
    try:
        for filename in os.listdir(local_dir):
            filepath = os.path.join(local_dir, filename)
            if filename.endswith(".jpg"):
                os.remove(filepath)
                print(f"Image {filename} deleted.")
        print("All images deleted.")
        log_action("Fotos eliminadas después de subirlas.", archivo)

    except Exception as e:
        raise RuntimeError(f"Error al eliminar las fotos: {e}")
