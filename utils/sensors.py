from sht20 import SHT20


def read_sensor_data():
    try:
        sht = SHT20(1, resolution=SHT20.TEMP_RES_14bit)
        data = sht.read_all()
        temp = round(data[0], 2)
        humid = round(data[1], 2)
        return temp, humid

    except Exception as e:
        raise RuntimeError(f"Error al leer los datos del sensor: {e}")
