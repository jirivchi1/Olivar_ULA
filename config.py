import os
from dotenv import load_dotenv

load_dotenv()

# GENERAL
SERVER_USER = os.getenv("SERVER_USER")
SERVER_IP = os.getenv("SERVER_IP")
METRICS_DIRECTORY = os.getenv("METRICS_DIRECTORY")
API_PASSWORD = os.getenv("API_PASSWORD")

# INDIVIDUAL
SERVER_DIR_YELLOW = os.getenv("SERVER_DIR_YELLOW")
SERVER_DIR_BANDA = os.getenv("SERVER_DIR_BANDA")
SERVER_DIR_GREEN = os.getenv("SERVER_DIR_GREEN")
SERVER_DIR_GREEN_2 = os.getenv("SERVER_DIR_GREEN_2")

LOCAL_DIRECTORY_YELLOW = os.getenv("LOCAL_DIRECTORY_YELLOW")
LOCAL_DIRECTORY_BANDA = os.getenv("LOCAL_DIRECTORY_BANDA")
LOCAL_DIRECTORY_GREEN = os.getenv("LOCAL_DIRECTORY_GREEN")
LOCAL_DIRECTORY_GREEN_2 = os.getenv("LOCAL_DIRECTORY_GREEN_2")



MONITORING_URL_YELLOW = os.getenv("MONITORING_URL_YELLOW")
MONITORING_URL_BANDA = os.getenv("MONITORING_URL_BANDA")
MONITORING_URL_GREEN = os.getenv("MONITORING_URL_GREEN")

DEVICE_ID_YELLOW = os.getenv("DEVICE_ID_YELLOW")
DEVICE_ID_BANDA = os.getenv("DEVICE_ID_BANDA")
DEVICE_ID_GREEN = os.getenv("DEVICE_ID_GREEN")
DEVICE_ID_GREEN_2 = os.getenv("DEVICE_ID_GREEN_2")



# Configuración del puerto serial y reintentos de conexión con Arduino
port = (
    "/dev/serial0"  # Asegúrate de que este puerto coincida con el puerto de tu Arduino
)
baud_rate = 9600
