#interfaz de Tema
class Observable:
    def __init__(self, name):
        self.name = name
        self.observers = []

    def addObserver(self, observer):
        self.observers.append(observer)

    def removeObserver(self, observer):
        self.observers.remove(observer)

    def getObservers(self):
        return self.observers
    
    def notifyChangeForOne(self, alerta, observer):
        if observer in self.observers:
            alerta.registrarEnvio()
            observer.notifyChange(alerta)

    def notifyChangeForAll(self, alerta):
        for observer in self.observers:
            alerta.registrarEnvio()
            observer.notifyChange(alerta)

    def obtenerAlertasNoExpiradas(self):
        alertasDelTema = []
        for observer in self.observers:
            alertasDelTema.append(observer.mostrarAlertasDeUnTemaOrdenadas(self))
        return self.aplanar(alertasDelTema) #el problema es el aplanar, no se si al hacer esto va a estar ordenado

    def aplanar(self, lista):
        listaAplanada = []
        for sublista in lista:
            for elemento in sublista:
                listaAplanada.append(elemento)
        return listaAplanada
