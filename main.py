
# ==========================================
# SISTEMA INTEGRAL SOFTWARE FJ
# Archivo principal
# Curso: Programacion - UNAD
# ==========================================

import logging

from utils.logger import configurar_logger
from utils.excepciones import ErrorSistema
from tests.simulaciones import ejecutar_simulaciones


def iniciar_sistema():

    # Configurar registro de eventos y errores
    logger = configurar_logger()

    print("\n======================================")
    print(" BIENVENIDO AL SISTEMA SOFTWARE FJ")
    print("======================================")

    logger.info("Inicio del sistema Software FJ")

    try:

        print("\nIniciando pruebas del sistema...\n")

        resultados = ejecutar_simulaciones()

    except Exception as error:

        logger.exception("Error general durante la ejecucion")

        try:
            raise ErrorSistema(
                "No fue posible completar la ejecucion del sistema."
            ) from error

        except ErrorSistema as error_encadenado:

            logger.error(
                "Excepcion encadenada: %s",
                error_encadenado
            )

            print("Se presento un error controlado:", error_encadenado)

    else:

        print("\nTodas las simulaciones finalizaron.")

        logger.info(
            "Ejecucion finalizada. Resultados: %s",
            resultados
        )

    finally:

        print("\n======================================")
        print(" FIN DEL SISTEMA SOFTWARE FJ")
        print("======================================")

        logger.info("Finalizacion del sistema Software FJ")


if __name__ == "__main__":

    iniciar_sistema()
