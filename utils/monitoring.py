import requests
from datetime import datetime
import pytz
from config import MONITORING_URL, DEVICE_ID, API_PASSWORD
from utils.logger import log_action


def send_monitoring_data(filename, temp, humid, bateriaArduino, bateriaPi):
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
            "device_id": DEVICE_ID,
            "timestamp": timestamp,
            "segundos": int(minutes + seconds),
            "temperatura": temp,
            "humedad": humid,
            "bateriaArduino": bateriaArduino,
            "bateriaPi": bateriaPi,
        }

        response = requests.post(
            MONITORING_URL, json=data, headers={"Content-Type": "application/json"}
        )

        if response.status_code == 200:
            print("Datos de monitorización enviados correctamente.")
            log_action("Monitorización: datos enviados correctamente.")
        else:
            raise RuntimeError(
                f"Error al enviar datos de monitorización. Código: {response.status_code}"
            )
    except requests.RequestException as e:
        raise RuntimeError(f"Error al enviar datos de monitorización: {e}")
