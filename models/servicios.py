
# ==========================================
# CLASES DE SERVICIOS
# Sistema de Gestion Software FJ
# ==========================================

from abc import ABC, abstractmethod

from utils.excepciones import (
    DatosInvalidosError,
    ServicioNoDisponibleError
)


class Servicio(ABC):
    """
    Clase abstracta que representa los servicios
    ofrecidos por Software FJ.
    """

    def __init__(self, nombre, tarifa, disponible=True):

        if not isinstance(nombre, str) or not nombre.strip():
            raise DatosInvalidosError(
                "El nombre del servicio es obligatorio."
            )

        if isinstance(tarifa, bool) or not isinstance(tarifa, (int, float)):
            raise DatosInvalidosError(
                "La tarifa debe ser numerica."
            )

        if tarifa <= 0:
            raise DatosInvalidosError(
                "La tarifa debe ser mayor que cero."
            )

        if not isinstance(disponible, bool):
            raise DatosInvalidosError(
                "La disponibilidad debe ser verdadera o falsa."
            )

        self.nombre = nombre.strip()
        self.tarifa = tarifa
        self.disponible = disponible

    def verificar_disponibilidad(self):

        if not self.disponible:
            raise ServicioNoDisponibleError(
                f"El servicio {self.nombre} no esta disponible."
            )

    def cambiar_disponibilidad(self, estado):

        if not isinstance(estado, bool):
            raise DatosInvalidosError(
                "El estado debe ser verdadero o falso."
            )

        self.disponible = estado

    def _calcular_total(self, duracion, impuesto, descuento):

        self.verificar_disponibilidad()

        if isinstance(duracion, bool) or not isinstance(duracion, (int, float)):
            raise DatosInvalidosError(
                "La duracion debe ser numerica."
            )

        if duracion <= 0:
            raise DatosInvalidosError(
                "La duracion debe ser mayor que cero."
            )

        if isinstance(impuesto, bool) or not isinstance(impuesto, (int, float)):
            raise DatosInvalidosError(
                "El impuesto debe ser numerico."
            )

        if impuesto < 0 or impuesto > 100:
            raise DatosInvalidosError(
                "El impuesto debe estar entre 0 y 100."
            )

        if isinstance(descuento, bool) or not isinstance(descuento, (int, float)):
            raise DatosInvalidosError(
                "El descuento debe ser numerico."
            )

        if descuento < 0:
            raise DatosInvalidosError(
                "El descuento no puede ser negativo."
            )

        subtotal = self.tarifa * duracion
        total = subtotal + (subtotal * impuesto / 100) - descuento

        if total < 0:
            raise DatosInvalidosError(
                "El descuento no puede superar el valor total."
            )

        return round(total, 2)

    @abstractmethod
    def calcular_costo(self, duracion, impuesto=0, descuento=0):
        pass

    @abstractmethod
    def describir(self):
        pass


# ==========================================
# SERVICIO DE RESERVA DE SALAS
# ==========================================

class ReservaSala(Servicio):

    def calcular_costo(self, duracion, impuesto=0, descuento=0):

        return self._calcular_total(
            duracion, impuesto, descuento
        )

    def describir(self):

        return "Reserva de sala por horas."


# ==========================================
# SERVICIO DE ALQUILER DE EQUIPOS
# ==========================================

class AlquilerEquipos(Servicio):

    def calcular_costo(self, duracion, impuesto=0, descuento=0):

        return self._calcular_total(
            duracion, impuesto, descuento
        )

    def describir(self):

        return "Alquiler de equipos tecnologicos."


# ==========================================
# SERVICIO DE ASESORIA ESPECIALIZADA
# ==========================================

class AsesoriaEspecializada(Servicio):

    def calcular_costo(self, duracion, impuesto=0, descuento=0):

        return self._calcular_total(
            duracion, impuesto, descuento
        )

    def describir(self):

        return "Asesoria especializada por horas."
