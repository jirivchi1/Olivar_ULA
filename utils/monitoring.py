import requests
from datetime import datetime
import pytz
from config import (
    MONITORING_URL_YELLOW,
    MONITORING_URL_BANDA,
    MONITORING_URL_GREEN,
    DEVICE_ID_BANDA,
    DEVICE_ID_GREEN,
    DEVICE_ID_YELLOW,
    API_PASSWORD,
)
from utils.logger import log_action_green, log_action_banda, log_action_yellow


def send_monitoring_data_banda(filename, temp, humid, bateriaArduino, bateriaPi):
    try:
        time_part = filename.split("_")[1]
        minutes = time_part[2:4]
        seconds = time_part[4:6]

        zona_horaria = pytz.timezone("Europe/Madrid")
        now = datetime.now(zona_horaria)
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S CEST%z")

        data = {
            "name": "irivera",
            "password": API_PASSWORD,
            "device_id": DEVICE_ID_BANDA,
            "timestamp": timestamp,
            "segundos": int(minutes + seconds),
            "temperatura": temp,
            "humedad": humid,
            "bateriaArduino": bateriaArduino,
            "bateriaPi": bateriaPi,
        }

        response = requests.post(
            MONITORING_URL_BANDA,
            json=data,
            headers={"Content-Type": "application/json"},
        )

        if response.status_code == 200:
            print("Datos de monitorización enviados correctamente.")
            log_action_banda("Monitorización: datos enviados correctamente.")
        else:
            raise RuntimeError(
                f"Error al enviar datos de monitorización. Código: {response.status_code}"
            )
    except requests.RequestException as e:
        raise RuntimeError(f"Error al enviar datos de monitorización: {e}")


def send_monitoring_data_yellow(filename, bateriaArduino, bateriaPi):
    try:
        time_part = filename.split("_")[1]
        minutes = time_part[2:4]
        seconds = time_part[4:6]

        zona_horaria = pytz.timezone("Europe/Madrid")
        now = datetime.now(zona_horaria)
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S CEST%z")

        data = {
            "name": "irivera",
            "password": API_PASSWORD,
            "device_id": DEVICE_ID_YELLOW,
            "timestamp": timestamp,
            "segundos": int(minutes + seconds),
            "bateriaArduino": bateriaArduino,
            "bateriaPi": bateriaPi,
        }

        response = requests.post(
            MONITORING_URL_YELLOW,
            json=data,
            headers={"Content-Type": "application/json"},
        )

        if response.status_code == 200:
            print("Datos de monitorización enviados correctamente.")
            log_action_yellow("Monitorización: datos enviados correctamente.")
        else:
            raise RuntimeError(
                f"Error al enviar datos de monitorización. Código: {response.status_code}"
            )
    except requests.RequestException as e:
        raise RuntimeError(f"Error al enviar datos de monitorización: {e}")


def send_monitoring_data_green(filename, bateriaArduino, bateriaPi):
    try:
        time_part = filename.split("_")[1]
        minutes = time_part[2:4]
        seconds = time_part[4:6]

        zona_horaria = pytz.timezone("Europe/Madrid")
        now = datetime.now(zona_horaria)
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S CEST%z")

        infrared_count = None
        # Evaluar el valor de infrarrojo antes de crear el diccionario
        valor_infrarrojo = infrared_count if infrared_count is not None else 1

        data = {
            "name": "irivera",
            "password": API_PASSWORD,
            "device_id": DEVICE_ID_GREEN,
            "timestamp": timestamp,
            "segundos": int(minutes + seconds),
            "infrarrojo": valor_infrarrojo,
            "bateriaArduino": bateriaArduino,
            "bateriaPi": bateriaPi,
        }

        response = requests.post(
            MONITORING_URL_GREEN,
            json=data,
            headers={"Content-Type": "application/json"},
        )

        if response.status_code == 200:
            print("Datos de monitorización enviados correctamente.")
            log_action_green("Monitorización: datos enviados correctamente.")
        else:
            raise RuntimeError(
                f"Error al enviar datos de monitorización. Código: {response.status_code}"
            )
    except requests.RequestException as e:
        raise RuntimeError(f"Error al enviar datos de monitorización: {e}")
