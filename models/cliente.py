
# ==========================================
# CLASE CLIENTE
# Sistema de Gestion Software FJ
# ==========================================

from models.entidades import Entidad
from utils.excepciones import DatosInvalidosError


class Cliente(Entidad):
    """
    Representa a los clientes registrados
    en el sistema Software FJ.
    """

    def __init__(self, identificador, nombre, correo):

        super().__init__(identificador)

        if not isinstance(nombre, str) or not nombre.strip():
            raise DatosInvalidosError(
                "El nombre del cliente es obligatorio."
            )

        if not isinstance(correo, str) or "@" not in correo:
            raise DatosInvalidosError(
                "El correo electronico no es valido."
            )

        self.__nombre = nombre.strip()
        self.__correo = correo.strip()

    @property
    def nombre(self):
        return self.__nombre

    @property
    def correo(self):
        return self.__correo

    def mostrar_informacion(self):

        return (
            f"Cliente: {self.__nombre} | "
            f"Correo: {self.__correo}"
        )
