from AlertSystem.src.InformativeAlert import InformativeAlert
from AlertSystem.src.UrgentAlert import UrgentAlert
from AlertSystem.src.Theme import Theme
from AlertSystem.src.User import User

jose = User("Jose")
alberto = User("Alberto")
roberto = User("Roberto")
maria = User("Maria")
natalia = User("Natalia")

def test_alerta_esta_expirada():
    cine = Theme("Cine")
    alertaExpirada = InformativeAlert("Gonzalez", "Corrio como pudo", cine, "01-01-1975 20:00:00")
    jose = User("Jose")
    jose.addTheme(cine)
    cine.notifyChange(alertaExpirada, None)
    jose.showAlerts() #leer una alerta o mostrarla las alertas de alguna forma que user conoce, actualiza el estado de las alertas
    assert alertaExpirada.getIsExpired()

def test_alerta_no_esta_expirada():
    naturaleza = Theme("Naturaleza")
    alertaNoExpirada = InformativeAlert("Rana amarilla", "salta y mata", naturaleza, "12-02-2024 22:00:00")
    natalia = User("Natalia")
    natalia.addTheme(naturaleza)
    naturaleza.notifyChange(alertaNoExpirada, None)
    natalia.showAlerts() #leer una alerta o mostrarla las alertas de alguna forma que user conoce, actualiza el estado de las alertas
    assert not alertaNoExpirada.getIsExpired()

def test_dos_alertas_expiradas_y_una_alerta_no_expirada_para_jose():
    viajes = Theme("Viajes")
    jose.addTheme(viajes)
    viajeExpirado1 = InformativeAlert(
        "Marley", "Con Florencia", viajes, "12-02-2004 16:00:00")
    viajeNoExpirado = InformativeAlert(
        "Marley", "Con invitado", viajes, "16-01-2025 20:00:00")
    viajeExpirado2 = InformativeAlert(
        "Marley", "En Qatar", viajes, "10-12-2022 23:00:00")
    viajes.notifyChange(viajeExpirado1, None)
    viajes.notifyChange(viajeNoExpirado, None)
    viajes.notifyChange(viajeExpirado2, None)
    assert len(jose.showAlerts()) == 1

def test_dos_alertas_expiradas_y_una_alerta_no_expirada_para_natalia_alberto_maria_roberto():
    deportes = Theme("Deportes")
    natalia.addTheme(deportes)
    alberto.addTheme(deportes)
    maria.addTheme(deportes)
    roberto.addTheme(deportes)
    deporteExpirado1 = UrgentAlert("Riquelme", "Se lesiono", deportes, "12-02-2005 09:26:12")
    deporteNoExpirado = InformativeAlert("Messi", "¿a arabia?", deportes, "01-12-2025 21:00:00")
    deporteExpirado2 = UrgentAlert("Riquelme", "Marco gol", deportes, "23-07-1998 16:50:03")
    deportes.notifyChange(deporteExpirado1, None)
    deportes.notifyChange(deporteExpirado2, None)
    deportes.notifyChange(deporteNoExpirado, None)
    natalia.showAlerts()
    alertasNoExpiradas = len(natalia.showAlerts()) + len(alberto.showAlerts()) + len(maria.showAlerts()) + len(roberto.showAlerts())
    assert alertasNoExpiradas == 4 # 3 alertas* 4 personas pero solo 1 alerta de esas 3 no esta expirada