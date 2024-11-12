import time
import serial
from config import port, baud_rate


def connect_serial(max_retries=5):
    ser = None
    retry_count = 0
    while ser is None and retry_count < max_retries:
        try:
            ser = serial.Serial(port, baud_rate, timeout=1)
            print("Conexión establecida con Arduino.")
            time.sleep(2)
        except serial.SerialException as e:
            retry_count += 1
            print(f"Error al conectar con Arduino: {e}. Reintentando...")
            time.sleep(2)
    if ser is None:
        raise ConnectionError("No se pudo conectar con Arduino.")
    return ser


def read_battery_data(ser):
    """Lee datos de voltaje de la batería desde Arduino."""
    bateriaArduino, bateriaPi = 0, 0
    start_time = time.time()
    timeout = 10  # Tiempo máximo de escucha en segundos

    while time.time() - start_time < timeout:
        if ser.in_waiting > 0:  # Comprobar si hay datos disponibles
            line = (
                ser.readline().decode("utf-8", errors="ignore").strip()
            )  # Leer línea desde el puerto serial

            try:
                # Separar los valores de los voltajes y convertirlos en float
                bateriaArduino, bateriaPi = map(float, line.split(","))

                # Comprobar si ambos voltajes están en el rango deseado
                if 2.0 <= bateriaArduino <= 12.0 and 2.0 <= bateriaPi <= 12.0:
                    break  # Salir del bucle si ambos valores están en el rango

            except ValueError:
                print(f"Invalid data received: {line}")

        time.sleep(0.5)

    if bateriaArduino == 0 and bateriaPi == 0:
        raise RuntimeError("No se pudo leer datos válidos de la batería desde Arduino.")

    return bateriaArduino, bateriaPi
