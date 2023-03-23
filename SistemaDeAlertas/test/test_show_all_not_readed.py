from SistemaDeAlertas.src.AlertaInformativa import AlertaInformativa
from SistemaDeAlertas.src.AlertaUrgente import AlertaUrgente
from SistemaDeAlertas.src.Tema import Tema
from SistemaDeAlertas.src.Usuario import Usuario

jose = Usuario("Jose")
alberto = Usuario("Alberto")
roberto = Usuario("Roberto")
maria = Usuario("Maria")
natalia = Usuario("Natalia")

def test_obtener_las_alertas_del_tema_cine():
    cine = Tema("Cine")
    alertaCine1 = AlertaInformativa(nombre="Frozen", descripcion="Records de visualizacion", tema=cine)
    alertaCine2 = AlertaUrgente(nombre="Argentina, 1985", descripcion="Otro premio para la pelicula", tema=cine)
    alertaCine3 = AlertaInformativa(nombre="Doble cafe", descripcion="Intenso y violento", tema=cine)
    cine.addObserver(jose)
    cine.addObserver(alberto)
    cine.addObserver(roberto)
    cine.addObserver(maria)
    cine.addObserver(natalia)
    cine.notifyChangeForAll(alertaCine1)
    cine.notifyChangeForAll(alertaCine2)
    cine.notifyChangeForAll(alertaCine3)
    assert len(cine.obtenerAlertasNoExpiradas()) == 15

def test_obtener_las_alertas_del_tema_cocina_sin_reiniciar_lo_anterior():
    cocina = Tema("Cocina")
    alertaCocina1 = AlertaUrgente(nombre="Cremona rellena", descripcion="Falta levadura", tema=cocina)
    alertaCocina2 = AlertaInformativa(nombre="Isla Flotante", descripcion="Falta caramelo", tema=cocina)
    alertaCocina3 = AlertaUrgente(nombre="Sandwich de milanesa al caballo", descripcion="Entradas vendidas", tema=cocina)
    cocina.addObserver(jose)
    cocina.addObserver(alberto)
    cocina.addObserver(roberto)
    cocina.addObserver(maria)
    cocina.addObserver(natalia)
    cocina.notifyChangeForAll(alertaCocina1)
    cocina.notifyChangeForAll(alertaCocina2)
    cocina.notifyChangeForAll(alertaCocina3)
    assert len(cocina.obtenerAlertasNoExpiradas()) == 15

def test_obtener_las_alertas_del_tema_automovilismo_sin_reiniciar_lo_anterior_y_solamente_a_jose_con_una_alerta_expirada():
    automovilismo = Tema("Automovilismo")
    alertaAutomovilismo1 = AlertaUrgente(nombre= "Se quedo sin neumaticos", descripcion="tires are gone", tema=automovilismo)
    alertaAutomovilismo2 = AlertaInformativa(nombre= "Schumacher gano en monaco", descripcion="Ferrari saca 100 puntos a los demas", tema=automovilismo, fechaYhoraExpiracion="22-05-2003 16:05:30")
    automovilismo.addObserver(jose)
    automovilismo.notifyChangeForOne(alertaAutomovilismo1, jose)
    automovilismo.notifyChangeForOne(alertaAutomovilismo2, jose)
    assert len(automovilismo.obtenerAlertasNoExpiradas()) == 1