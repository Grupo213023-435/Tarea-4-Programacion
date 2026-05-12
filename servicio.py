# servicio.py

from abc import ABC, abstractmethod
from excepciones import ServicioError


# clase abstracta de servicios
class Servicio(ABC):

    def __init__(
        self,
        nombre,
        costo_base
    ):

        self.set_nombre(nombre)
        self.set_costo_base(costo_base)

    # validar nombre
    def set_nombre(self, nombre):

        if not nombre.strip():

            raise ServicioError(
                "El nombre del servicio está vacío"
            )

        self.nombre = nombre

    # validar costo
    def set_costo_base(self, costo_base):

        if costo_base <= 0:

            raise ServicioError(
                "El costo debe ser mayor a 0"
            )

        self.costo_base = costo_base

    # metodos abstractos
    @abstractmethod
    def calcular_costo(self):
        pass

    @abstractmethod
    def descripcion(self):
        pass


# servicio de salas
class ReservaSala(Servicio):

    def __init__(
        self,
        nombre,
        costo_base,
        horas
    ):

        super().__init__(
            nombre,
            costo_base
        )

        if horas <= 0:

            raise ServicioError(
                "Las horas son inválidas"
            )

        self.horas = horas

    # calcular costo
    def calcular_costo(
        self,
        impuesto=0
    ):

        total = self.costo_base * self.horas

        if impuesto > 0:

            total += total * impuesto

        return total

    # descripcion del servicio
    def descripcion(self):

        return (
            f"Reserva de sala "
            f"por {self.horas} horas"
        )


# servicio de alquiler
class AlquilerEquipo(Servicio):

    def __init__(
        self,
        nombre,
        costo_base,
        dias
    ):

        super().__init__(
            nombre,
            costo_base
        )

        if dias <= 0:

            raise ServicioError(
                "Los dias son inválidos"
            )

        self.dias = dias

    # calcular costo
    def calcular_costo(
        self,
        descuento=0
    ):

        total = self.costo_base * self.dias

        if descuento > total:

            raise ServicioError(
                "Descuento inválido"
            )

        return total - descuento

    # descripcion
    def descripcion(self):

        return (
            f"Alquiler de equipo "
            f"por {self.dias} dias"
        )
        # servicio de asesoria
class AsesoriaEspecializada(Servicio):

    def __init__(
        self,
        nombre,
        costo_base,
        nivel
    ):

        super().__init__(
            nombre,
            costo_base
        )

        self.nivel = nivel

    # calcular costo
    def calcular_costo(
        self,
        impuesto=0,
        descuento=0
    ):

        total = self.costo_base

        total += total * impuesto
        total -= descuento

        return total

    # descripcion
    def descripcion(self):

        return (
            f"Asesoria "
            f"{self.nivel}"
        )
