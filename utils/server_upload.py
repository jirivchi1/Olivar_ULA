import os
import subprocess
import time
from utils.logger import log_action

# Configuración dinámica del directorio de métricas
from config import SERVER_USER, SERVER_IP

# Obtener el directorio base del usuario actual dinámicamente
HOME_DIRECTORY = os.path.expanduser("~")
METRICS_DIRECTORY = os.path.join(HOME_DIRECTORY, "metrics")


def upload_to_server(server_dir, local_dir, archivo):
    """
    Sube las imágenes en 'local_dir' y el archivo de log 'archivo'
    al servidor remoto, con reintentos y logs de cada intento.
    """
    try:
        print(f"Subiendo imágenes desde {local_dir} al servidor {SERVER_IP}:{server_dir}")
        
        for filename in os.listdir(local_dir):
            if filename.endswith(".jpg"):
                filepath = os.path.join(local_dir, filename)
                
                # Intentamos subir la imagen en hasta 3 intentos
                for attempt in range(3):  # 0,1,2
                    try:
                        subprocess.run(
                            ["scp", filepath, f"{SERVER_USER}@{SERVER_IP}:{server_dir}"],
                            check=True,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE
                        )
                        # Log de éxito indicando en qué intento se subió
                        msg = f"Imagen {filename} subida al servidor en el intento {attempt+1}."
                        print(msg)
                        log_action(msg, archivo)
                        break  # Si funcionó, salimos del for de intentos
                    except subprocess.CalledProcessError as e:
                        # Log de error indicando el intento fallido
                        err_msg = (f"Error subiendo imagen {filename} en el intento {attempt+1}: {e}")
                        print(err_msg)
                        log_action(err_msg, archivo)
                        
                        # Si no es el último intento, esperamos antes de reintentar
                        if attempt < 2:
                            time.sleep(5)
                        else:
                            # Si agotamos los 3 intentos, lanzamos el error
                            raise RuntimeError(f"No se pudo subir {filename} después de 3 intentos.")

        # Subir archivo de log en hasta 3 intentos
        log_file_path = os.path.join(METRICS_DIRECTORY, archivo)
        print(f"Subiendo archivo de log: {log_file_path}")
        for attempt in range(3):
            try:
                subprocess.run(
                    [
                        "scp",
                        log_file_path,
                        f"{SERVER_USER}@{SERVER_IP}:{server_dir}/{archivo}",
                    ],
                    check=True,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE
                )
                msg = f"Archivo de log '{archivo}' subido en el intento {attempt+1}."
                print(msg)
                log_action(msg, archivo)
                break
            except subprocess.CalledProcessError as e:
                err_msg = (f"Error subiendo archivo de log en el intento {attempt+1}: {e}")
                print(err_msg)
                log_action(err_msg, archivo)
                if attempt < 2:
                    time.sleep(5)
                else:
                    raise RuntimeError(f"No se pudo subir el archivo de log después de 3 intentos.")
        
        final_msg = "Todas las imágenes, datos de sensores y archivo de log subidos correctamente."
        print(final_msg)
        log_action(final_msg, archivo)

    except Exception as e:
        raise RuntimeError(f"Error al subir archivos al servidor: {e}")
                

def delete_photos(local_dir, archivo):
    """
    Elimina todas las imágenes con extensión .jpg en 'local_dir'
    y deja un registro de la acción en los logs.
    """
    try:
        print(f"Eliminando imágenes del directorio local: {local_dir}")
        for filename in os.listdir(local_dir):
            if filename.endswith(".jpg"):
                filepath = os.path.join(local_dir, filename)
                os.remove(filepath)
                msg = f"Imagen {filename} eliminada."
                print(msg)
                log_action(msg, archivo)
        print("Todas las imágenes eliminadas.")
        log_action("Fotos eliminadas después de subirlas.", archivo)

    except Exception as e:
        raise RuntimeError(f"Error al eliminar las fotos: {e}")
