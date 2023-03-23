from SistemaDeAlertas.src.AlertaInformativa import AlertaInformativa
from SistemaDeAlertas.src.AlertaUrgente import AlertaUrgente
from SistemaDeAlertas.src.Tema import Tema
from SistemaDeAlertas.src.Usuario import Usuario

jose = Usuario("Jose")
alberto = Usuario("Alberto")
roberto = Usuario("Roberto")
maria = Usuario("Maria")
natalia = Usuario("Natalia")

def test_la_alerta_de_roberto_fue_leida():
    cine = Tema("Cine")
    alertaRoberto = AlertaInformativa(nombre="Hombre arania 3", descripcion="Entradas agotadas", tema=cine)
    cine.addObserver(roberto)
    cine.notifyChangeForOne(alertaRoberto, roberto)
    roberto.verAlerta(alertaRoberto)
    assert alertaRoberto.fuiLeida()

def test_la_alerta_de_maria_no_fue_leida():
    cine = Tema("Cine")
    alertaMaria = AlertaUrgente(nombre="Netflix", descripcion="Nueva pelicula de ciencia ficcion", tema=cine)
    cine.addObserver(maria)
    cine.notifyChangeForOne(alertaMaria, maria)
    assert not alertaMaria.fuiLeida()