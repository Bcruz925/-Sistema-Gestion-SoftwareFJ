
# ==========================================
# SIMULACIONES DEL SISTEMA SOFTWARE FJ
# ==========================================

import logging

from models.cliente import Cliente
from models.servicios import (
    ReservaSala,
    AlquilerEquipos,
    AsesoriaEspecializada
)
from models.reserva import Reserva

from utils.excepciones import (
    DatosInvalidosError,
    ReservaInvalidaError,
    ServicioNoDisponibleError
)

logger = logging.getLogger("SoftwareFJ")

def ejecutar_simulaciones():

    print("\n======================================")
    print(" SIMULACIONES DEL SISTEMA SOFTWARE FJ")
    print("======================================")

    exitos = 0
    errores = 0

    def registrar_resultado(numero, descripcion, operacion):

        nonlocal exitos, errores

        try:
            resultado = operacion()

        except Exception as error:
            errores += 1
            logger.exception(
                "Simulacion %s - %s",
                numero,
                descripcion
            )
            print(f"{numero}. {descripcion}: ERROR CONTROLADO - {error}")

        else:
            exitos += 1
            logger.info(
                "Simulacion %s - %s - Resultado: %s",
                numero,
                descripcion,
                resultado
            )
            print(f"{numero}. {descripcion}: CORRECTO")

        finally:
            logger.info("Finalizada simulacion %s", numero)

    # Preparacion de datos validos

    cliente = Cliente(1, "Maria Lopez", "maria@gmail.com")

    sala = ReservaSala("Sala de reuniones", 50000)
    equipos = AlquilerEquipos("Computadores", 30000)
    asesoria = AsesoriaEspecializada("Asesoria Python", 60000)

    # 1. Registrar cliente valido

    registrar_resultado(
        1,
        "Registro de cliente valido",
        lambda: cliente.mostrar_informacion()
    )

    # 2. Intentar registrar cliente sin nombre

    registrar_resultado(
        2,
        "Validacion de nombre vacio",
        lambda: Cliente(2, "", "correo@gmail.com")
    )

    # 3. Intentar registrar correo incorrecto

    registrar_resultado(
        3,
        "Validacion de correo incorrecto",
        lambda: Cliente(3, "Carlos Perez", "correoIncorrecto")
    )

    # 4. Crear servicio de salas

    registrar_resultado(
        4,
        "Creacion de servicio de salas",
        lambda: sala.describir()
    )

    # 5. Crear servicio de equipos

    registrar_resultado(
        5,
        "Creacion de servicio de equipos",
        lambda: equipos.describir()
    )

    # 6. Crear servicio de asesoria

    registrar_resultado(
        6,
        "Creacion de servicio de asesoria",
        lambda: asesoria.describir()
    )

    # 7. Intentar crear servicio con tarifa negativa

    registrar_resultado(
        7,
        "Validacion de tarifa negativa",
        lambda: ReservaSala("Sala incorrecta", -5000)
    )

    # 8. Intentar calcular un servicio no disponible

    def servicio_no_disponible():

        sala.cambiar_disponibilidad(False)
        return sala.calcular_costo(2)

    registrar_resultado(
        8,
        "Control de servicio no disponible",
        servicio_no_disponible
    )

    # Reactivar servicio

    sala.cambiar_disponibilidad(True)

    # 9. Crear reserva valida

    reserva = Reserva(101, cliente, sala, 2)

    registrar_resultado(
        9,
        "Creacion de reserva valida",
        lambda: reserva.mostrar_informacion()
    )

    # 10. Intentar crear reserva con duracion cero

    registrar_resultado(
        10,
        "Validacion de duracion incorrecta",
        lambda: Reserva(102, cliente, sala, 0)
    )

    # 11. Confirmar reserva

    registrar_resultado(
        11,
        "Confirmacion de reserva",
        lambda: reserva.confirmar()
    )

    # 12. Procesar reserva confirmada

    registrar_resultado(
        12,
        "Procesamiento de reserva",
        lambda: reserva.procesar(19, 5000)
    )

    # 13. Intentar procesar reserva nuevamente

    registrar_resultado(
        13,
        "Control de procesamiento repetido",
        lambda: reserva.procesar()
    )

    # 14. Intentar confirmar una reserva procesada

    registrar_resultado(
        14,
        "Control de confirmacion no permitida",
        lambda: reserva.confirmar()
    )

    # 15. Crear y cancelar otra reserva

    reserva_cancelada = Reserva(103, cliente, equipos, 1)

    registrar_resultado(
        15,
        "Cancelacion de reserva",
        lambda: reserva_cancelada.cancelar()
    )

    # 16. Intentar procesar reserva cancelada

    registrar_resultado(
        16,
        "Control de reserva cancelada",
        lambda: reserva_cancelada.procesar()
    )

    # 17. Validar impuesto incorrecto

    registrar_resultado(
        17,
        "Validacion de impuesto negativo",
        lambda: asesoria.calcular_costo(1, -10, 0)
    )

    # 18. Validar descuento excesivo

    registrar_resultado(
        18,
        "Validacion de descuento excesivo",
        lambda: equipos.calcular_costo(1, 0, 500000)
    )

    # 19. Validar descuento negativo

    registrar_resultado(
        19,
        "Validacion de descuento negativo",
        lambda: sala.calcular_costo(1, 0, -1000)
    )

    # 20. Calculo correcto con impuesto y descuento

    registrar_resultado(
        20,
        "Calculo de costo correcto",
        lambda: asesoria.calcular_costo(2, 19, 5000)
    )

    # Resumen final

    print("\n======================================")
    print(" RESUMEN DE LAS SIMULACIONES")
    print("======================================")

    print("Simulaciones ejecutadas:", exitos + errores)
    print("Operaciones correctas:", exitos)
    print("Errores controlados:", errores)

    logger.info(
        "Resumen: %s simulaciones, %s correctas, %s errores controlados",
        exitos + errores,
        exitos,
        errores
    )

    print("\nProceso de simulaciones finalizado.")

    return exitos, errores
    