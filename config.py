import os
from dotenv import load_dotenv

load_dotenv()

SERVER_USER = os.getenv("SERVER_USER")
SERVER_IP = os.getenv("SERVER_IP")
SERVER_DIR = os.getenv("SERVER_DIR")
LOCAL_DIRECTORY = os.getenv(
    "LOCAL_DIRECTORY")
METRICS_DIRECTORY = os.getenv("METRICS_DIRECTORY")
SENSOR_DATA_FILE = os.getenv(
    "SENSOR_DATA_FILE")
MONITORING_URL = os.getenv("MONITORING_URL")
DEVICE_ID = os.getenv("DEVICE_ID")
API_PASSWORD = os.getenv("API_PASSWORD")


# Configuración del puerto serial y reintentos de conexión con Arduino
port = (
    "/dev/serial0"  # Asegúrate de que este puerto coincida con el puerto de tu Arduino
)
baud_rate = 9600
