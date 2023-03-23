from SistemaDeAlertas.src.AlertaInformativa import AlertaInformativa
from SistemaDeAlertas.src.AlertaUrgente import AlertaUrgente
from SistemaDeAlertas.src.Tema import Tema
from SistemaDeAlertas.src.Usuario import Usuario

jose = Usuario("Jose")
alberto = Usuario("Alberto")
roberto = Usuario("Roberto")
maria = Usuario("Maria")
natalia = Usuario("Natalia")

def test_alerta_esta_expirada():
    alerta = AlertaInformativa(nombre="Gonzalez", descripcion="Corrio como pudo", tema=Tema("algo"), fechaYhoraExpiracion="01-01-1975 20:00:00")
    assert not alerta.soyVisible()

def test_alerta_no_esta_expirada():
    alerta = AlertaInformativa(nombre="Chistoso", descripcion="Salio en CronicaTV", tema=Tema("algo"), fechaYhoraExpiracion="25-12-2024 00:00:00")
    assert alerta.soyVisible()

def test_dos_alertas_expiradas_y_una_alerta_no_expirada_para_jose():
    viajes = Tema("Viajes")
    viajes.addObserver(jose)
    viajeExpirados1 = AlertaInformativa(
        nombre="Marley", descripcion="Con Florencia", tema=viajes, fechaYhoraExpiracion="12-02-2004 16:00:00")
    viajeNoExpirado = AlertaInformativa(
        nombre="Marley", descripcion="Con invitado", tema=viajes, fechaYhoraExpiracion="16-01-2025 20:00:00")
    viajeExpirados2 = AlertaInformativa(
        nombre="Marley", descripcion="En Qatar", tema=viajes, fechaYhoraExpiracion="10-12-2022 23:00:00")
    viajes.notifyChangeForOne(viajeExpirados1, jose)
    viajes.notifyChangeForOne(viajeExpirados2, jose)
    viajes.notifyChangeForOne(viajeNoExpirado, jose)
    assert len(jose.mostrarAlertas()) == 1

def test_dos_alertas_expiradas_y_una_alerta_no_expirada_para_natalia_alberto_maria_roberto():
    deportes = Tema("Deportes")
    deportes.addObserver(natalia)
    deportes.addObserver(alberto)
    deportes.addObserver(maria)
    deportes.addObserver(roberto)
    deporteExpirados1 = AlertaUrgente(
        nombre="Riquelme", descripcion="Se lesiono", tema=deportes, fechaYhoraExpiracion="12-02-2005 09:26:12")
    deporteNoExpirado = AlertaInformativa(
        nombre="Messi", descripcion="¿a arabia?", tema=deportes, fechaYhoraExpiracion="01-12-2025 21:00:00")
    deporteExpirados2 = AlertaUrgente(
        nombre="Riquelme", descripcion="Marco gol", tema=deportes, fechaYhoraExpiracion="23-07-1998 16:50:03")
    deportes.notifyChangeForAll(deporteExpirados1)
    deportes.notifyChangeForAll(deporteExpirados2)
    deportes.notifyChangeForAll(deporteNoExpirado)
    alertasNoExpiradas = len(natalia.mostrarAlertas()) + len(alberto.mostrarAlertas())+ len(maria.mostrarAlertas()) + len(roberto.mostrarAlertas())
    assert alertasNoExpiradas == 4 # 3 alertas* 4 personas pero solo 1 alerta de esas 3 no esta expirada