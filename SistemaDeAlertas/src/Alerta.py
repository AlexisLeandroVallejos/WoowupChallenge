from datetime import datetime

class Alerta:
    FORMATO_FECHA_HORA = "%d-%m-%Y %H:%M:%S"
    def __init__(self, **kwargs):
        self.esVisible = True
        self.esLeida = False
        self.timestampSent = None
        if len(kwargs) == 3:
            self.nombre = kwargs["nombre"]
            self.descripcion = kwargs["descripcion"]
            self.tema = kwargs["tema"]
        else:
            self.fechaYhoraExpiracion = datetime.strptime(kwargs["fechaYhoraExpiracion"], self.FORMATO_FECHA_HORA)
            self.controlDeExpiracion()

    def obtenerFechaYHoraActual(self):
        return datetime.now()

    def controlDeExpiracion(self):
        if self.fechaYhoraExpiracion <= self.obtenerFechaYHoraActual():
            self.esVisible = False

    def leer(self):
        self.esLeida = True

    def fuiLeida(self):
        return self.esLeida

    def soyVisible(self):
        return self.esVisible

    def obtenerTema(self):
        return self.tema

    def registrarEnvio(self):
        self.timestampSent = self.obtenerFechaYHoraActual()

    def getTimestampSent(self):
        return self.timestampSent

    def soyInformativa(self):
        pass

    def soyUrgente(self):
        pass