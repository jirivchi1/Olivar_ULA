import os
import subprocess
from utils.logger import log_action

# Configuración dinámica del directorio de métricas
from config import SERVER_USER, SERVER_IP

# Obtener el directorio base del usuario actual dinámicamente
HOME_DIRECTORY = os.path.expanduser("~")
METRICS_DIRECTORY = os.path.join(HOME_DIRECTORY, "metrics")


def upload_to_server(server_dir, local_dir, archivo):
    try:
        print(f"Subiendo imágenes desde {local_dir} al servidor {SERVER_IP}:{server_dir}")
        # Subir todas las imágenes en el directorio local
        for filename in os.listdir(local_dir):
            filepath = os.path.join(local_dir, filename)
            if filename.endswith(".jpg"):
                subprocess.run(
                    ["scp", filepath, f"{SERVER_USER}@{SERVER_IP}:{server_dir}"],
                    check=True,
                )
                print(f"Imagen {filename} subida al servidor.")

        # Subir archivo de log
        log_file_path = os.path.join(METRICS_DIRECTORY, archivo)
        print(f"Subiendo archivo de log: {log_file_path}")
        subprocess.run(
            [
                "scp",
                log_file_path,
                f"{SERVER_USER}@{SERVER_IP}:{server_dir}/{archivo}",
            ],
            check=True,
        )
        print("Archivo de log subido al servidor.")
        log_action("Todas las imágenes, datos de sensores y archivo de log subidos.", archivo)

    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"Error al subir archivos al servidor: {e}")


def delete_photos(local_dir, archivo):
    try:
        print(f"Eliminando imágenes del directorio local: {local_dir}")
        for filename in os.listdir(local_dir):
            filepath = os.path.join(local_dir, filename)
            if filename.endswith(".jpg"):
                os.remove(filepath)
                print(f"Imagen {filename} eliminada.")
        print("Todas las imágenes eliminadas.")
        log_action("Fotos eliminadas después de subirlas.", archivo)

    except Exception as e:
        raise RuntimeError(f"Error al eliminar las fotos: {e}")
