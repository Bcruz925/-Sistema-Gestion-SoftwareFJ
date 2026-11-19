
# ==========================================
# CLASE RESERVA
# Sistema de Gestion Software FJ
# ==========================================

import logging

from models.entidades import Entidad
from models.cliente import Cliente
from models.servicios import Servicio

from utils.excepciones import (
    DatosInvalidosError,
    ReservaInvalidaError
)


class Reserva(Entidad):
    """
    Representa una reserva realizada por un cliente
    para utilizar uno de los servicios de Software FJ.
    """

    def __init__(self, identificador, cliente, servicio, duracion):

        super().__init__(identificador)

        if not isinstance(cliente, Cliente):
            raise DatosInvalidosError(
                "El cliente registrado no es valido."
            )

        if not isinstance(servicio, Servicio):
            raise DatosInvalidosError(
                "El servicio seleccionado no es valido."
            )

        if isinstance(duracion, bool) or not isinstance(duracion, (int, float)):
            raise ReservaInvalidaError(
                "La duracion debe ser numerica."
            )

        if duracion <= 0:
            raise ReservaInvalidaError(
                "La duracion debe ser mayor que cero."
            )

        servicio.verificar_disponibilidad()

        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "Pendiente"

        logging.info(
            "Reserva %s creada para el cliente %s",
            self.identificador,
            self.cliente.nombre
        )

    def confirmar(self):
        """Confirma una reserva pendiente."""

        if self.estado != "Pendiente":
            raise ReservaInvalidaError(
                "Solo se pueden confirmar reservas pendientes."
            )

        self.servicio.verificar_disponibilidad()

        self.estado = "Confirmada"

        logging.info(
            "Reserva %s confirmada",
            self.identificador
        )

    def cancelar(self):
        """Cancela una reserva pendiente o confirmada."""

        if self.estado == "Cancelada":
            raise ReservaInvalidaError(
                "La reserva ya se encuentra cancelada."
            )

        if self.estado == "Procesada":
            raise ReservaInvalidaError(
                "No se puede cancelar una reserva procesada."
            )

        self.estado = "Cancelada"

        logging.info(
            "Reserva %s cancelada",
            self.identificador
        )

    def procesar(self, impuesto=0, descuento=0):
        """Calcula el costo de una reserva confirmada."""

        if self.estado != "Confirmada":
            raise ReservaInvalidaError(
                "Solo se pueden procesar reservas confirmadas."
            )

        costo = self.servicio.calcular_costo(
            self.duracion,
            impuesto,
            descuento
        )

        self.estado = "Procesada"

        logging.info(
            "Reserva %s procesada. Total: %s",
            self.identificador,
            costo
        )

        return costo

    def mostrar_informacion(self):
        """Devuelve la informacion de la reserva."""

        return (
            f"Reserva: {self.identificador} | "
            f"Cliente: {self.cliente.nombre} | "
            f"Servicio: {self.servicio.nombre} | "
            f"Duracion: {self.duracion} | "
            f"Estado: {self.estado}"
        )
