import time
import serial
from config import port, baud_rate
from utils.logger import log_action  # Importa el log para registrar errores


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

    try:
        while time.time() - start_time < timeout:
            if ser.in_waiting > 0:  # Comprobar si hay datos disponibles
                line = ser.readline().decode("utf-8", errors="ignore").strip()

                try:
                    # Separar y convertir los valores de voltaje
                    bateriaArduino, bateriaPi = map(float, line.split(","))

                    # Verificar que los valores estén en el rango deseado
                    if 2.0 <= bateriaArduino <= 14.0 and 2.0 <= bateriaPi <= 14.0:
                        log_action(
                            f"Valores bateria Pi:{bateriaPi}, arduino: {bateriaArduino}"
                        )
                        break  # Salir del bucle si ambos valores están en el rango

                except ValueError:
                    print(f"Invalid data received: {line}")

            time.sleep(0.5)

        if bateriaArduino == 0 and bateriaPi == 0:
            raise RuntimeError(
                "No se pudo leer datos válidos de la batería desde Arduino."
            )

    except Exception as e:
        # Registrar el error en el log y devolver valores predeterminados
        log_action(f"Error al leer datos de la batería: {e}")
        bateriaArduino, bateriaPi = -1, -1  # Valores predeterminados en caso de error

    return bateriaArduino, bateriaPi
