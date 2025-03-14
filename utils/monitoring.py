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
    DEVICE_ID_GREEN_2,
    API_PASSWORD,
)
from utils.logger import log_action


def extract_time_from_filename(filename, archivo):
    try:
        time_part = filename.split("_")[1]
        minutes = time_part[2:4]
        seconds = time_part[4:6]
        return int(minutes + seconds)
    except (AttributeError, IndexError, ValueError):
        log_action("No se cogió el tiempo de la foto; usando la hora actual.", archivo)
        zona_horaria = pytz.timezone("Europe/Madrid")
        now = datetime.now(zona_horaria)
        return int(now.strftime("%M%S"))


def send_monitoring_data_banda(
    filename, temp, humid, bateriaArduino, bateriaPi, archivo
):
    try:
        zona_horaria = pytz.timezone("Europe/Madrid")
        now = datetime.now(zona_horaria)
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S CEST%z")

        segundos = extract_time_from_filename(filename, archivo)

        data = {
            "name": "irivera",
            "password": API_PASSWORD,
            "device_id": DEVICE_ID_BANDA,
            "timestamp": timestamp,
            "segundos": segundos,
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
            log_action("Monitorización: datos enviados correctamente.", archivo)
        else:
            raise RuntimeError(
                f"Error al enviar datos de monitorización. Código: {response.status_code}"
            )
    except requests.RequestException as e:
        raise RuntimeError(f"Error al enviar datos de monitorización: {e}")


def send_monitoring_data_yellow(filename, bateriaArduino, bateriaPi, archivo):
    try:
        zona_horaria = pytz.timezone("Europe/Madrid")
        now = datetime.now(zona_horaria)
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S CEST%z")

        segundos = extract_time_from_filename(filename, archivo)

        data = {
            "name": "irivera",
            "password": API_PASSWORD,
            "device_id": DEVICE_ID_YELLOW,
            "timestamp": timestamp,
            "segundos": segundos,
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
            log_action("Monitorización: datos enviados correctamente.", archivo)
        else:
            raise RuntimeError(
                f"Error al enviar datos de monitorización. Código: {response.status_code}"
            )
    except requests.RequestException as e:
        raise RuntimeError(f"Error al enviar datos de monitorización: {e}")


def send_monitoring_data_green(filename, bateriaArduino, bateriaPi, archivo):
    try:
        zona_horaria = pytz.timezone("Europe/Madrid")
        now = datetime.now(zona_horaria)
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S CEST%z")

        segundos = extract_time_from_filename(filename, archivo)

        infrared_count = None
        valor_infrarrojo = infrared_count if infrared_count is not None else 0

        data = {
            "name": "irivera",
            "password": API_PASSWORD,
            "device_id": DEVICE_ID_GREEN,
            "timestamp": timestamp,
            "segundos": segundos,
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
            log_action("Monitorización: datos enviados correctamente.", archivo)
        else:
            raise RuntimeError(
                f"Error al enviar datos de monitorización. Código: {response.status_code}"
            )
    except requests.RequestException as e:
        raise RuntimeError(f"Error al enviar datos de monitorización: {e}")


def send_monitoring_data_green_2(filename, bateriaArduino, bateriaPi, archivo):
    try:
        zona_horaria = pytz.timezone("Europe/Madrid")
        now = datetime.now(zona_horaria)
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S CEST%z")

        segundos = extract_time_from_filename(filename, archivo)

        infrared_count = None
        valor_infrarrojo = infrared_count if infrared_count is not None else 0

        data = {
            "name": "irivera",
            "password": API_PASSWORD,
            "device_id": DEVICE_ID_GREEN_2,
            "timestamp": timestamp,
            "segundos": segundos,
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
            log_action("Monitorización: datos enviados correctamente.", archivo)
        else:
            raise RuntimeError(
                f"Error al enviar datos de monitorización. Código: {response.status_code}"
            )
    except requests.RequestException as e:
        raise RuntimeError(f"Error al enviar datos de monitorización: {e}")

