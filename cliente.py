# cliente.py

from abc import ABC, abstractmethod
from excepciones import ClienteError


# clase abstracta
class Entidad(ABC):

    @abstractmethod
    def mostrar_info(self):
        pass


class Cliente(Entidad):

    def __init__(self, nombre, correo, telefono):

        # validar datos al crear cliente
        self.set_nombre(nombre)
        self.set_correo(correo)
        self.set_telefono(telefono)

    # validar nombre
    def set_nombre(self, nombre):

        if not nombre.strip():

            raise ClienteError(
                "El nombre no puede estar vacío"
            )

        if len(nombre) < 3:

            raise ClienteError(
                "El nombre es demasiado corto"
            )

        self.__nombre = nombre

    # validar correo
    def set_correo(self, correo):

        if not correo.strip():

            raise ClienteError(
                "El correo está vacío"
            )

        if "@" not in correo or "." not in correo:

            raise ClienteError(
                "Correo inválido"
            )

        self.__correo = correo

    # validar telefono
    def set_telefono(self, telefono):

        if not telefono.isdigit():

            raise ClienteError(
                "El teléfono debe tener números"
            )

        if len(telefono) < 7:

            raise ClienteError(
                "Número inválido"
            )

        self.__telefono = telefono

    # getters
    def get_nombre(self):

        return self.__nombre

    def get_correo(self):

        return self.__correo

    def get_telefono(self):

        return self.__telefono

    # actualizar informacion
    def actualizar_datos(
        self,
        nuevo_nombre,
        nuevo_correo,
        nuevo_telefono
    ):

        self.set_nombre(nuevo_nombre)
        self.set_correo(nuevo_correo)
        self.set_telefono(nuevo_telefono)

    # mostrar datos
    def mostrar_info(self):

        print("\ninformacion del cliente")
        print(f"Nombre: {self.__nombre}")
        print(f"Correo: {self.__correo}")
        print(f"Telefono: {self.__telefono}")

    # mostrar objeto como texto
    def __str__(self):

        return (
            f"{self.__nombre} - "
            f"{self.__correo}"
        )