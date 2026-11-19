
# ==========================================
# EXCEPCIONES PERSONALIZADAS
# Sistema de Gestion Software FJ
# ==========================================

class ErrorSistema(Exception):
    """Excepcion general del sistema Software FJ."""
    pass


class DatosInvalidosError(ErrorSistema):
    """Se presenta cuando los datos ingresados no son validos."""
    pass


class ReservaInvalidaError(ErrorSistema):
    """Se presenta cuando una reserva no cumple las condiciones."""
    pass


class ServicioNoDisponibleError(ErrorSistema):
    """Se presenta cuando un servicio no esta disponible."""
    pass


class ClienteNoEncontradoError(ErrorSistema):
    """Se presenta cuando un cliente no existe en el sistema."""
    pass
