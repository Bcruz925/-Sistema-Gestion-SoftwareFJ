
# ==========================================
# CLASE ABSTRACTA ENTIDAD
# Sistema de Gestion Software FJ
# ==========================================

from abc import ABC, abstractmethod


class Entidad(ABC):
    """
    Clase abstracta que representa las entidades
    generales del sistema Software FJ.
    """

    def __init__(self, identificador):

        if identificador is None:
            raise ValueError("El identificador es obligatorio.")

        self._identificador = identificador

    @property
    def identificador(self):
        """Permite consultar el identificador."""
        return self._identificador

    @abstractmethod
    def mostrar_informacion(self):
        """Metodo que deben implementar las clases hijas."""
        pass
