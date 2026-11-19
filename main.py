
from abc import ABC, abstractmethod
import logging

# ==========================================
# CONFIGURACION DEL SISTEMA DE REGISTROS
# ==========================================

logging.basicConfig(
    filename="sistema.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)


# ==========================================
# EXCEPCIONES PERSONALIZADAS
# ==========================================

class ErrorSistema(Exception):
    """Excepcion general del sistema."""
    pass


class DatosInvalidosError(ErrorSistema):
    """Se presenta cuando los datos no son validos."""
    pass


class ReservaInvalidaError(ErrorSistema):
    """Se presenta cuando una reserva es incorrecta."""
    pass


class ServicioNoDisponibleError(ErrorSistema):
    """Se presenta cuando un servicio no esta disponible."""
    pass


# ==========================================
# ENTIDAD ABSTRACTA
# ==========================================

class Entidad(ABC):

    def __init__(self, identificador):
        self._identificador = identificador

    @property
    def identificador(self):
        return self._identificador

    @abstractmethod
    def mostrar_informacion(self):
        pass


# ==========================================
# CLASE CLIENTE
# ==========================================

class Cliente(Entidad):

    def __init__(self, identificador, nombre, correo):
        super().__init__(identificador)

        if not nombre or not nombre.strip():
            raise DatosInvalidosError("El nombre es obligatorio.")

        if not correo or "@" not in correo:
            raise DatosInvalidosError("El correo no es valido.")

        self.__nombre = nombre
        self.__correo = correo

    @property
    def nombre(self):
        return self.__nombre

    @property
    def correo(self):
        return self.__correo

    def mostrar_informacion(self):
        return f"Cliente: {self.__nombre} - {self.__correo}"


# ==========================================
# SERVICIO ABSTRACTO
# ==========================================

class Servicio(ABC):

    def __init__(self, nombre, tarifa):
        if tarifa <= 0:
            raise DatosInvalidosError("La tarifa debe ser mayor que cero.")

        self.nombre = nombre
        self.tarifa = tarifa

    @abstractmethod
    def calcular_costo(self, duracion, impuesto=0, descuento=0):
        pass

    @abstractmethod
    def describir(self):
        pass


# ==========================================
# SERVICIOS ESPECIALIZADOS
# ==========================================

class ReservaSala(Servicio):

    def calcular_costo(self, duracion, impuesto=0, descuento=0):
        subtotal = self.tarifa * duracion
        return subtotal + (subtotal * impuesto / 100) - descuento

    def describir(self):
        return "Reserva de sala por horas."


class AlquilerEquipos(Servicio):

    def calcular_costo(self, duracion, impuesto=0, descuento=0):
        subtotal = self.tarifa * duracion
        return subtotal + (subtotal * impuesto / 100) - descuento

    def describir(self):
        return "Alquiler de equipos tecnologicos."


class AsesoriaEspecializada(Servicio):

    def calcular_costo(self, duracion, impuesto=0, descuento=0):
        subtotal = self.tarifa * duracion
        return subtotal + (subtotal * impuesto / 100) - descuento

    def describir(self):
        return "Asesoria especializada por horas."


# ==========================================
# CLASE RESERVA
# ==========================================

class Reserva(Entidad):

    def __init__(self, identificador, cliente, servicio, duracion):
        super().__init__(identificador)

        if not isinstance(cliente, Cliente):
            raise DatosInvalidosError("El cliente no es valido.")

        if not isinstance(servicio, Servicio):
            raise DatosInvalidosError("El servicio no es valido.")

        if duracion <= 0:
            raise ReservaInvalidaError("La duracion debe ser positiva.")

        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "Pendiente"

    def confirmar(self):
        if self.estado != "Pendiente":
            raise ReservaInvalidaError(
                "La reserva no puede confirmarse."
            )

        self.estado = "Confirmada"
        logging.info("Reserva %s confirmada", self.identificador)

    def cancelar(self):
        if self.estado == "Cancelada":
            raise ReservaInvalidaError(
                "La reserva ya esta cancelada."
            )

        self.estado = "Cancelada"
        logging.info("Reserva %s cancelada", self.identificador)

    def procesar(self):
        if self.estado != "Confirmada":
            raise ReservaInvalidaError(
                "Solo se procesan reservas confirmadas."
            )

        costo = self.servicio.calcular_costo(self.duracion)
        logging.info("Reserva %s procesada", self.identificador)
        return costo

    def mostrar_informacion(self):
        return (
            f"Reserva {self.identificador} | "
            f"Cliente: {self.cliente.nombre} | "
            f"Servicio: {self.servicio.nombre} | "
            f"Estado: {self.estado}"
        )


# ==========================================
# SISTEMA PRINCIPAL
# ==========================================

class SistemaSoftwareFJ:

    def __init__(self):
        self.clientes = []
        self.servicios = []
        self.reservas = []

    def registrar_cliente(self, cliente):
        self.clientes.append(cliente)
        logging.info("Cliente registrado: %s", cliente.nombre)

    def registrar_servicio(self, servicio):
        self.servicios.append(servicio)
        logging.info("Servicio registrado: %s", servicio.nombre)

    def registrar_reserva(self, reserva):
        self.reservas.append(reserva)
        logging.info("Reserva registrada: %s", reserva.identificador)


# ==========================================
# SIMULACIONES DEL SISTEMA
# ==========================================

def ejecutar_simulaciones():

    sistema = SistemaSoftwareFJ()

    print("\n===================================")
    print(" SISTEMA DE GESTION SOFTWARE FJ")
    print("===================================\n")

    # 1. Registrar cliente valido
    try:
        cliente1 = Cliente(1, "Maria Lopez", "maria@gmail.com")
        sistema.registrar_cliente(cliente1)
        print("1. Cliente registrado correctamente.")

    except DatosInvalidosError as error:
        logging.error("Error al registrar cliente: %s", error)
        print("1. Error:", error)

    # 2. Registrar cliente con correo invalido
    try:
        Cliente(2, "Carlos Perez", "correoIncorrecto")
    except DatosInvalidosError as error:
        logging.error("Error de datos de cliente: %s", error)
        print("2. Cliente rechazado:", error)

    # 3. Crear servicio de salas
    try:
        sala = ReservaSala("Sala de reuniones", 50000)
        sistema.registrar_servicio(sala)
        print("3. Servicio de salas creado.")

    except DatosInvalidosError as error:
        logging.error("Error de servicio: %s", error)

    # 4. Crear servicio de alquiler de equipos
    equipos = AlquilerEquipos("Alquiler de computadores", 30000)
    sistema.registrar_servicio(equipos)
    print("4. Servicio de equipos creado.")

    # 5. Crear servicio de asesoria
    asesoria = AsesoriaEspecializada("Asesoria Python", 60000)
    sistema.registrar_servicio(asesoria)
    print("5. Servicio de asesoria creado.")

    # 6. Intentar crear servicio con tarifa incorrecta
    try:
        ReservaSala("Sala incorrecta", -1000)
    except DatosInvalidosError as error:
        logging.error("Error de tarifa: %s", error)
        print("6. Servicio rechazado:", error)

    # 7. Crear una reserva valida
    try:
        reserva1 = Reserva(101, cliente1, sala, 2)
        sistema.registrar_reserva(reserva1)
        print("7. Reserva creada correctamente.")

    except ErrorSistema as error:
        logging.error("Error de reserva: %s", error)

    # 8. Intentar crear una reserva con duracion incorrecta
    try:
        Reserva(102, cliente1, sala, 0)
    except ReservaInvalidaError as error:
        logging.error("Reserva invalida: %s", error)
        print("8. Reserva rechazada:", error)

    # 9. Confirmar y procesar una reserva
    try:
        reserva1.confirmar()
        costo = reserva1.procesar()
        print("9. Reserva procesada. Total:", costo)

    except ReservaInvalidaError as error:
        logging.error("Error de procesamiento: %s", error)

    # 10. Intentar procesar una reserva cancelada
    try:
        reserva2 = Reserva(103, cliente1, sala, 1)
        reserva2.cancelar()
        reserva2.procesar()

    except ReservaInvalidaError as error:
        logging.error("Operacion no permitida: %s", error)
        print("10. Operacion rechazada:", error)

    # 11. Simular una operacion con encadenamiento
    try:
        try:
            raise ValueError("Error interno de calculo.")
        except ValueError as error:
            raise ErrorSistema("No fue posible realizar el calculo.") from error

    except ErrorSistema as error:
        logging.exception("Error encadenado: %s", error)
        print("11. Error controlado:", error)

    # 12. Demostrar try/except/else/finally
    try:
        resultado = sala.calcular_costo(2, 19, 5000)

    except Exception as error:
        logging.error("Error en calculo: %s", error)

    else:
        print("12. Calculo con impuesto y descuento:", resultado)

    finally:
        print("\nProceso de simulaciones finalizado.")
        logging.info("Finalizaron las simulaciones.")


if __name__ == "__main__":
    ejecutar_simulaciones()
