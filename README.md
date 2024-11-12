# Proyecto de Monitorización con Raspberry Pi y Arduino

Este proyecto permite monitorizar datos ambientales y de sistema usando sensores conectados a una Raspberry Pi y un Arduino, con funcionalidades de captura de fotos, envío de datos a un servidor, y almacenamiento de logs.

## Estructura del Proyecto

```plaintext
proyecto/
│
├── main.py                # Script principal que ejecuta el proceso general.
│
├── config.py              # Configuración general y carga de variables de entorno.
│
├── utils/                 # Carpeta de módulos utilitarios.
│   ├── serial_connection.py # Conexión serial y lectura de datos de batería.
│   ├── sensors.py           # Lectura de datos de sensores SHT20.
│   ├── camera.py            # Toma de fotos mediante la cámara conectada.
│   ├── server_upload.py     # Subida de fotos y datos al servidor.
│   ├── logger.py            # Registro de logs del sistema y eventos.
│   ├── monitoring.py        # Envío de datos de monitorización al servidor.
│   └── shutdown.py          # Apagado seguro del sistema.
│
└── .env                     # Variables de entorno para configuraciones sensibles.
