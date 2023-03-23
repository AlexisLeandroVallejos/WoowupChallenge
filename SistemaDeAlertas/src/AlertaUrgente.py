from SistemaDeAlertas.src.Alerta import Alerta

class AlertaUrgente(Alerta):
    
    def soyInformativa(self):
        return False

    def soyUrgente(self):
        return True    