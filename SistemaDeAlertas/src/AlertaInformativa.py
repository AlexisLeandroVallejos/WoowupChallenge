from SistemaDeAlertas.src.Alerta import Alerta

class AlertaInformativa(Alerta):
    
    def soyInformativa(self):
        return True

    def soyUrgente(self):
        return False    