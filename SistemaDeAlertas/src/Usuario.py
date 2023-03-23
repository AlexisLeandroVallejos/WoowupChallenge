from SistemaDeAlertas.src.Observer import Observer

class Usuario(Observer):

    def __init__(self, name):
        Observer.__init__(self, name)
        self.alertas = []
        
    def notifyChange(self, alerta):
        self.alertas.append(alerta)

    #devuelve todas las alertas
    def getAlerts(self):
        return self.alertas

    #devuelve solamente las alertas que no estan expiradas
    #llamarla asi es mas directo segun lo pedido
    def mostrarAlertas(self):
        alertasVisibles = []
        for alerta in self.alertas:
            if alerta.soyVisible():
                alertasVisibles.append(alerta)
        return alertasVisibles

    def mostrarAlertasNoLeidasSinOrdenar(self):
        alertasNoLeidasSinOrdenar = []
        for alerta in self.mostrarAlertas():
            if not alerta.fuiLeida():
                alertasNoLeidasSinOrdenar.append(alerta)
        return alertasNoLeidasSinOrdenar

    def ordenarUrgentes(self, listaDeAlertasAOrdenar):
        alertasUrgentes = []
        for alerta in listaDeAlertasAOrdenar:
            if alerta.soyUrgente():
                alertasUrgentes.append(alerta)
        return sorted(alertasUrgentes, key=lambda alerta: alerta.getTimestampSent())

    def ordenarInformativas(self, listaDeAlertasAOrdenar):
        alertasInformativas = []
        for alerta in listaDeAlertasAOrdenar:
            if alerta.soyInformativa():
                alertasInformativas.append(alerta)
        return sorted(alertasInformativas, key=lambda alerta: alerta.getTimestampSent(), reverse=True)

    def mostrarAlertasNoLeidasOrdenadas(self):
        return self.ordenarUrgentes(self.mostrarAlertasNoLeidasSinOrdenar()) + self.ordenarInformativas(self.mostrarAlertasNoLeidasSinOrdenar())

    def mostrarAlertasDeUnTema(self, tema):
        alertasDelTema = []
        for alerta in self.mostrarAlertas():
            if alerta.obtenerTema() == tema:
                alertasDelTema.append(alerta)
        return alertasDelTema

    def mostrarAlertasDeUnTemaOrdenadas(self, tema):
        return self.ordenarUrgentes(self.mostrarAlertasDeUnTema(tema)) + self.ordenarInformativas(self.mostrarAlertasDeUnTema(tema))

    def verAlerta(self, alerta):
        if alerta in self.alertas:
            alerta.leer()

