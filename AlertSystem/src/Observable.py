#interfaz de Tema
class Observable:
    def __init__(self, name):
        self.name = name

    def addObserver(self, observer):
        pass

    def removeObserver(self, observer):
        pass

    def notifyChange(self, alert, observer):
        pass