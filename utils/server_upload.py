import os
import subprocess
from utils.logger import log_action

# Configuración dinámica del directorio de métricas
from config import SERVER_USER, SERVER_IP

# Obtener el directorio base del usuario actual dinámicamente
HOME_DIRECTORY = os.path.expanduser("~")
METRICS_DIRECTORY = os.path.join(HOME_DIRECTORY, "metrics")


def upload_to_server(server_dir, local_dir, archivo, max_retries=3, retry_delay=10):
    import time
    retry_count = 0
    
    while retry_count < max_retries:
        try:
            print(f"Intento {retry_count+1} de {max_retries}: Subiendo imágenes desde {local_dir} al servidor {SERVER_IP}:{server_dir}")
            
            # Verificar conexión de red antes de intentar SCP
            check_network = subprocess.run(["ping", "-c", "1", SERVER_IP], capture_output=True)
            if check_network.returncode != 0:
                log_action(f"Red no disponible, reintentando en {retry_delay} segundos...", archivo)
                time.sleep(retry_delay)
                retry_count += 1
                continue
                
            # Resto del código de upload_to_server sin cambios
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
            return True  # Éxito
            
        except subprocess.CalledProcessError as e:
            log_action(f"Error al subir archivos (intento {retry_count+1}/{max_retries}): {e}", archivo)
            retry_count += 1
            if retry_count < max_retries:
                log_action(f"Reintentando en {retry_delay} segundos...", archivo)
                time.sleep(retry_delay)
            else:
                raise RuntimeError(f"Error al subir archivos al servidor después de {max_retries} intentos: {e}")
                
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
