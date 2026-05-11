# main.py

from cliente import Cliente

from servicio import (
    ReservaSala,
    AlquilerEquipo
)

from logger_config import (
    registrar_log,
    registrar_error
)


print("\nsoftware fj\n")


clientes = []
servicios = []


# operacion 1
try:

    cliente1 = Cliente(
        "Andres Felipe",
        "andres@gmail.com",
        "312345678"
    )

    clientes.append(cliente1)

    registrar_log(
        "cliente registrado"
    )

    cliente1.mostrar_info()

except Exception as e:

    registrar_error(e)
    print(e)


# operacion 2
try:

    cliente2 = Cliente(
        "Maria",
        "maria@gmail.com",
        "300456789"
    )

    clientes.append(cliente2)

    registrar_log(
        "cliente registrado"
    )

except Exception as e:

    registrar_error(e)
    print(e)


# operacion 3
try:

    cliente_error = Cliente(
        "",
        "correo_malo",
        "12"
    )

except Exception as e:

    registrar_error(e)

    print(
        f"\nerror: {e}"
    )


# operacion 4
try:

    servicio1 = ReservaSala(
        "Sala VIP",
        120000,
        4
    )

    servicios.append(servicio1)

    registrar_log(
        "servicio creado"
    )

except Exception as e:

    registrar_error(e)


# operacion 5
try:

    servicio2 = AlquilerEquipo(
        "Portatil Gamer",
        80000,
        3
    )

    servicios.append(servicio2)

    registrar_log(
        "servicio creado"
    )

except Exception as e:

    registrar_error(e)