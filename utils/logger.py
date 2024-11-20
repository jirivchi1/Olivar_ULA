import os
from datetime import datetime

# Obtener el directorio base del usuario actual dinámicamente
METRICS_DIRECTORY = os.path.join(os.path.expanduser("~"), "metrics")

def log_action(message, archivo):
    # Asegurar que el directorio de métricas exista
    os.makedirs(METRICS_DIRECTORY, exist_ok=True)
    
    # Crear o abrir el archivo de log y escribir el mensaje
    with open(f"{METRICS_DIRECTORY}/{archivo}", "a") as log_file:
        log_file.write(f"{datetime.now()}: {message}\n")
