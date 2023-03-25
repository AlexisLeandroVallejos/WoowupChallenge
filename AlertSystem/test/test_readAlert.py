from AlertSystem.src.InformativeAlert import InformativeAlert
from AlertSystem.src.UrgentAlert import UrgentAlert
from AlertSystem.src.Theme import Theme
from AlertSystem.src.User import User

roberto = User("Roberto")
maria = User("Maria")
jose = User("Jose")
alberto = User("alberto")

def test_la_alerta_de_roberto_fue_leida():
    cine = Theme("Cine")
    alertaRoberto = InformativeAlert("Hombre arania 3", "Entradas agotadas", cine)
    roberto.addTheme(cine)
    cine.notifyChange(alertaRoberto, None)
    roberto.readAlert(alertaRoberto)
    assert alertaRoberto.getIsRead()

def test_la_alerta_de_maria_no_fue_leida():
    cine = Theme("Cine")
    alertaMaria = UrgentAlert("Netflix", "Nueva pelicula de ciencia ficcion", cine)
    maria.addTheme(cine)
    cine.notifyChange(alertaMaria, None)
    assert not alertaMaria.getIsRead()

def test_roberto_no_puede_leer_una_alerta_expirada_de_sus_alertas_no_leidas():
    cine = Theme("Cine")
    roberto.addTheme(cine)
    alertaCine = UrgentAlert("Las catacumbas 7", "debajo del mar", cine, "25-08-1966 15:01:03")
    cine.notifyChange(alertaCine, None)
    roberto.readAlert(alertaCine)
    assert not alertaCine.getIsRead()

def test_alberto_no_puede_leer_una_alerta_de_otra_persona():
    automovilismo = Theme("Automovilismo")
    noticia = Theme("Noticia")
    jose.addTheme(automovilismo)
    alberto.addTheme(noticia)
    alertaAutomovilismo = InformativeAlert("Sale volando rueda", "No es chiste", automovilismo)
    alertaNoticia = UrgentAlert("loco del 7", "salta de casa en casa", noticia)
    automovilismo.notifyChange(alertaAutomovilismo, None)
    noticia.notifyChange(alertaNoticia, None)
    alberto.readAlert(alertaAutomovilismo)
    assert not alertaAutomovilismo.getIsRead()