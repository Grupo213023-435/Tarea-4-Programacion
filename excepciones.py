# excepciones.py


# error base del sistema
class ErrorBaseSistema(Exception):

    def __init__(self, mensaje):

        self.mensaje = mensaje

        super().__init__(self.mensaje)

    def __str__(self):

        return f"{self.mensaje}"


# errores relacionados con clientes
class ClienteError(ErrorBaseSistema):

    pass


# errores relacionados con servicios
class ServicioError(ErrorBaseSistema):

    pass


# errores relacionados con reservas
class ReservaError(ErrorBaseSistema):

    pass