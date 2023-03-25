from AlertSystem.src.InformativeAlert import InformativeAlert
from AlertSystem.src.UrgentAlert import UrgentAlert
from AlertSystem.src.Theme import Theme

#necesito mas informacion sobre que la hace informativa/urgente!
#no se justifica su existencia sino; solamente para usar booleanas por punto 11
def test_es_alerta_informativa():
    viajes = Theme("Viajes")
    alertaViajesInformativa = InformativeAlert("Relajo", "Vacaciones en el caribe", viajes, "25-12-2029 16:16:16")
    assert alertaViajesInformativa.isInformative()

def test_no_es_alerta_urgente():
    autos = Theme("Autos")
    alertaAutosInformativa = InformativeAlert("Lamborghini", "Sesto elemento", autos, "21-02-2045 10:06:16")
    assert not alertaAutosInformativa.isUrgent()

def test_es_alerta_urgente():
    moda = Theme("Moda")
    alertaModaUrgente = UrgentAlert("5 cosas", "utiles en costura", moda, "01-02-2032 18:16:18")
    assert alertaModaUrgente.isUrgent()

def test_no_es_alerta_informativa():
    disenio = Theme("Disenio")
    alertaDiseñoUrgente = UrgentAlert("5 cosas", "utiles en aislamiento", disenio, "01-02-2032 18:16:18")
    assert not alertaDiseñoUrgente.isInformative()