# logger_config.py

import logging


# configuracion del archivo de logs
logging.basicConfig(
    filename="logs.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


# guardar eventos normales
def registrar_log(mensaje):

    logging.info(mensaje)


# guardar errores
def registrar_error(error):

    logging.error(error)