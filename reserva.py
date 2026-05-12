# reserva.py

from excepciones import ReservaError

from logger_config import (
    registrar_log,
    registrar_error
)


class Reserva:

    def __init__(
        self,
        cliente,
        servicio,
        duracion
    ):

        # validar duracion
        if duracion <= 0:

            raise ReservaError(
                "La duración no es válida"
            )

        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "Pendiente"

    # confirmar reserva
    def confirmar(self):

        self.estado = "Confirmada"

        registrar_log(
            "reserva confirmada"
        )

        print(
            "\nreserva confirmada"
        )

    # cancelar reserva
    def cancelar(self):

        self.estado = "Cancelada"

        registrar_log(
            "reserva cancelada"
        )

        print(
            "\nreserva cancelada"
        )

    # procesar reserva
    def procesar(self):

        try:

            costo = (
                self.servicio
                .calcular_costo()
            )

        except Exception as error:

            registrar_error(error)

            raise ReservaError(
                "Error procesando reserva"
            ) from error

        else:

            print(
                f"\nCosto total: {costo}"
            )

        finally:

            print(
                "proceso finalizado"
            )
