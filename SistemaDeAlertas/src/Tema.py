from SistemaDeAlertas.src.Observable import Observable

class Tema(Observable):
    def __init__(self, name):
        Observable.__init__(self, name)