from sht20 import SHT20

# Registra el error y devuelve valores predeterminados
from utils.logger import log_action


def read_sensor_data(archivo):
    try:
        sht = SHT20(1, resolution=SHT20.TEMP_RES_14bit)
        data = sht.read_all()
        temp = round(data[0], 2)
        humid = round(data[1], 2)
        log_action(f"Datos sensor temp: {temp}, hum: {humid}", archivo)
        return temp, humid

    except Exception as e:
        log_action(f"Error al leer los datos del sensor: {e}", archivo)
        return -1, -1  # Devuelve valores nulos o predeterminados
