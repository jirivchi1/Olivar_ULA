import os
import subprocess
from utils.logger import log_action


from config import (
    SERVER_USER,
    SERVER_IP,
    SERVER_DIR_BANDA,
    SERVER_DIR_GREEN,
    SERVER_DIR_YELLOW,
    LOCAL_DIRECTORY_BANDA,
    LOCAL_DIRECTORY_GREEN,
    LOCAL_DIRECTORY_YELLOW,
    METRICS_DIRECTORY,
)


def upload_to_server_banda():
    try:
        # Subir todas las imágenes en el directorio LOCAL_DIRECTORY_BANDA
        for filename in os.listdir(LOCAL_DIRECTORY_BANDA):
            filepath = os.path.join(LOCAL_DIRECTORY_BANDA, filename)
            if filename.endswith(".jpg"):
                subprocess.run(
                    ["scp", filepath, f"{SERVER_USER}@{SERVER_IP}:{SERVER_DIR_BANDA}"],
                    check=True,
                )
                print(f"Image {filename} uploaded to the server.")

        # Subir archivo de log_banda.txt
        log_file_path = os.path.join(METRICS_DIRECTORY, "log_banda.txt")
        subprocess.run(
            [
                "scp",
                log_file_path,
                f"{SERVER_USER}@{SERVER_IP}:{SERVER_DIR_BANDA}/log_banda.txt",
            ],
            check=True,
        )
        print("Log file uploaded to the server.")

        print("All images, sensor data, and log file uploaded.")

    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"Error al subir archivos al servidor: {e}")


def delete_photos_banda():
    try:
        for filename in os.listdir(LOCAL_DIRECTORY_BANDA):
            filepath = os.path.join(LOCAL_DIRECTORY_BANDA, filename)
            if filename.endswith(".jpg"):
                os.remove(filepath)
                print(f"Image {filename} deleted.")
        print("All images deleted.")
        log_action("Fotos eliminadas después de subirlas.")

    except Exception as e:
        raise RuntimeError(f"Error al eliminar las fotos: {e}")


def upload_to_server_green():
    try:
        # Subir todas las imágenes en el directorio LOCAL_DIRECTORY
        for filename in os.listdir(LOCAL_DIRECTORY_GREEN):
            filepath = os.path.join(LOCAL_DIRECTORY_GREEN, filename)
            if filename.endswith(".jpg"):
                subprocess.run(
                    ["scp", filepath, f"{SERVER_USER}@{SERVER_IP}:{SERVER_DIR_GREEN}"],
                    check=True,
                )
                print(f"Image {filename} uploaded to the server.")

        # Subir archivo de log_banda.txt
        log_file_path = os.path.join(METRICS_DIRECTORY, "log_green.txt")
        subprocess.run(
            [
                "scp",
                log_file_path,
                f"{SERVER_USER}@{SERVER_IP}:{SERVER_DIR_GREEN}/log_green.txt",
            ],
            check=True,
        )
        print("Log file uploaded to the server.")

        print("All images, sensor data, and log file uploaded.")

    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"Error al subir archivos al servidor: {e}")


def delete_photos_green():
    try:
        for filename in os.listdir(LOCAL_DIRECTORY_GREEN):
            filepath = os.path.join(LOCAL_DIRECTORY_GREEN, filename)
            if filename.endswith(".jpg"):
                os.remove(filepath)
                print(f"Image {filename} deleted.")
        print("All images deleted.")
        log_action("Fotos eliminadas después de subirlas.")

    except Exception as e:
        raise RuntimeError(f"Error al eliminar las fotos: {e}")


def upload_to_server_yellow():
    try:
        # Subir todas las imágenes en el directorio LOCAL_DIRECTORY
        for filename in os.listdir(LOCAL_DIRECTORY_YELLOW):
            filepath = os.path.join(LOCAL_DIRECTORY_YELLOW, filename)
            if filename.endswith(".jpg"):
                subprocess.run(
                    ["scp", filepath, f"{SERVER_USER}@{SERVER_IP}:{SERVER_DIR_YELLOW}"],
                    check=True,
                )
                print(f"Image {filename} uploaded to the server.")

        # Subir archivo de log_banda.txt
        log_file_path = os.path.join(METRICS_DIRECTORY, "log_banda.txt")
        subprocess.run(
            [
                "scp",
                log_file_path,
                f"{SERVER_USER}@{SERVER_IP}:{SERVER_DIR_YELLOW}/log_banda.txt",
            ],
            check=True,
        )
        print("Log file uploaded to the server.")

        print("All images, sensor data, and log file uploaded.")

    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"Error al subir archivos al servidor: {e}")


def delete_photos_yellow():
    try:
        for filename in os.listdir(LOCAL_DIRECTORY_YELLOW):
            filepath = os.path.join(LOCAL_DIRECTORY_YELLOW, filename)
            if filename.endswith(".jpg"):
                os.remove(filepath)
                print(f"Image {filename} deleted.")
        print("All images deleted.")
        log_action("Fotos eliminadas después de subirlas.")

    except Exception as e:
        raise RuntimeError(f"Error al eliminar las fotos: {e}")
