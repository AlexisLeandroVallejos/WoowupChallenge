from SistemaDeAlertas.src.AlertaInformativa import AlertaInformativa
from SistemaDeAlertas.src.AlertaUrgente import AlertaUrgente
from SistemaDeAlertas.src.Tema import Tema
from SistemaDeAlertas.src.Usuario import Usuario

jose = Usuario("Jose")
alberto = Usuario("Alberto")
roberto = Usuario("Roberto")
maria = Usuario("Maria")
natalia = Usuario("Natalia")

def test_jose_lee_solamente_los_tres_temas_de_automovilismo_seis_quedan_sin_leer():
    automovilismo = Tema("Automovilismo")
    cine = Tema("Cine")
    cocina = Tema("Cocina")
    alertaAutomovilismo1 = AlertaInformativa(nombre="¿Pero lo dejarias pasar?", descripcion="Alonso is faster than you", tema=automovilismo)
    alertaAutomovilismo2 = AlertaInformativa(nombre="YOUR DAYS ARE GONE!", descripcion="G. CEARA", tema=automovilismo)
    alertaAutomovilismo3 = AlertaInformativa(nombre="Indianapolis 2005", descripcion="No lo entenderias...", tema=automovilismo)
    alertaCine1 = AlertaUrgente(nombre="Frozen", descripcion="Records de visualizacion", tema=cine)
    alertaCine2 = AlertaUrgente(nombre="Argentina, 1985", descripcion="Otro premio para la pelicula", tema=cine)
    alertaCine3 = AlertaUrgente(nombre="Doble cafe", descripcion="Intenso y violento", tema=cine)
    alertaCocina1 = AlertaUrgente(nombre="Cremona rellena", descripcion="Falta levadura", tema=cocina)
    alertaCocina2 = AlertaUrgente(nombre="Isla Flotante", descripcion="Falta caramelo", tema=cocina)
    alertaCocina3 = AlertaUrgente(nombre="Sandwich de milanesa al caballo", descripcion="Entradas vendidas", tema=cocina)
    automovilismo.addObserver(jose)
    cine.addObserver(jose)
    cocina.addObserver(jose)
    automovilismo.notifyChangeForAll(alertaAutomovilismo1)
    automovilismo.notifyChangeForAll(alertaAutomovilismo2)
    automovilismo.notifyChangeForAll(alertaAutomovilismo3)
    cine.notifyChangeForAll(alertaCine1)
    cine.notifyChangeForAll(alertaCine2)
    cine.notifyChangeForAll(alertaCine3)
    cocina.notifyChangeForAll(alertaCocina1)
    cocina.notifyChangeForAll(alertaCocina2)
    cocina.notifyChangeForAll(alertaCocina3)
    jose.verAlerta(alertaAutomovilismo1)
    jose.verAlerta(alertaAutomovilismo2)
    jose.verAlerta(alertaAutomovilismo3)
    assert len(jose.mostrarAlertasNoLeidasOrdenadas()) == 6