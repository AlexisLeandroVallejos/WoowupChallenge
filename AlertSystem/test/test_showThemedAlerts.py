from AlertSystem.src.InformativeAlert import InformativeAlert
from AlertSystem.src.UrgentAlert import UrgentAlert
from AlertSystem.src.Theme import Theme
from AlertSystem.src.User import User

jose = User("Jose")
alberto = User("Alberto")
roberto = User("Roberto")
maria = User("Maria")
natalia = User("Natalia")

cine = Theme("Cine")
cocina = Theme("Cocina")
automovilismo = Theme("Automovilismo")

alertaCine1 = InformativeAlert("Frozen", "Records de visualizacion", cine)
alertaCine2 = UrgentAlert("Argentina, 1985", "Otro premio para la pelicula", cine)
alertaCine3 = InformativeAlert("Doble cafe", "Intenso y violento", cine)
alertaCine4 = UrgentAlert("Indiana", "Jones", cine)
alertaCine5 = UrgentAlert("Desde lo alto", "temblaban", cine)
alertaCine6 = InformativeAlert("Carrera de pichones", "¿...que?", cine)

alertaCocina1 = UrgentAlert("Cremona rellena", "Falta levadura", cocina)
alertaCocina2 = InformativeAlert("Isla Flotante", "Falta caramelo", cocina)

alertaAutomovilismo1 = UrgentAlert("Se quedo sin neumaticos", "tires are gone", automovilismo)
alertaAutomovilismo2 = InformativeAlert("Schumacher gano en monaco", "Ferrari saca 100 puntos a los demas", automovilismo, "22-05-2003 16:05:30")

jose.addTheme(cine)
natalia.addTheme(cine)
alberto.addTheme(cine)
maria.addTheme(cine)
roberto.addTheme(cine)

jose.addTheme(cocina)
alberto.addTheme(cocina)
roberto.addTheme(cocina)
maria.addTheme(cocina)
natalia.addTheme(cocina)

jose.addTheme(automovilismo)

cine.notifyChange(alertaCine1, None) #I1
cine.notifyChange(alertaCine2, None) #U2
cine.notifyChange(alertaCine3, None) #I3
cine.notifyChange(alertaCine4, None) #U4
cine.notifyChange(alertaCine5, None) #U5
cine.notifyChange(alertaCine6, None) #I6

cocina.notifyChange(alertaCocina1, None)
cocina.notifyChange(alertaCocina2, None)

automovilismo.notifyChange(alertaAutomovilismo1, jose) #no expiro
automovilismo.notifyChange(alertaAutomovilismo2, jose) #expirada

def test_obtener_las_alertas_del_tema_cine():
    totalDeAlertasDeCine = len(jose.showThemedAlerts(cine)) + len(natalia.showThemedAlerts(cine)) + len(alberto.showThemedAlerts(cine)) + len(maria.showThemedAlerts(cine)) + len(roberto.showThemedAlerts(cine))
    assert totalDeAlertasDeCine  == 30

def test_obtener_las_alertas_del_tema_cocina_sin_reiniciar_lo_anterior():
    totalDeAlertasDeCocina = len(jose.showThemedAlerts(cocina)) + len(natalia.showThemedAlerts(cocina)) + len(
        alberto.showThemedAlerts(cocina)) + len(maria.showThemedAlerts(cocina)) + len(roberto.showThemedAlerts(cocina))
    assert totalDeAlertasDeCocina == 10

def test_obtener_las_alertas_del_tema_automovilismo_sin_reiniciar_lo_anterior_y_solamente_a_jose_con_una_alerta_expirada():
    assert len(jose.showThemedAlerts(automovilismo)) == 1

def test_las_alertas_de_cine_de_alberto_estan_ordenadas():
    # segun enunciado las de cine deberian estar asi: [U5,U4,U2,I1,I3,I6]
    primerElemento = alberto.showThemedAlerts(cine)[0] == alertaCine5
    segundoElemento = alberto.showThemedAlerts(cine)[1] == alertaCine4
    tercerElemento = alberto.showThemedAlerts(cine)[2] == alertaCine2
    cuartoElemento = alberto.showThemedAlerts(cine)[3] == alertaCine1
    quintoElemento = alberto.showThemedAlerts(cine)[4] == alertaCine3
    sextoElemento = alberto.showThemedAlerts(cine)[5] == alertaCine6
    estanOrdenados = primerElemento and segundoElemento and tercerElemento and cuartoElemento and quintoElemento and sextoElemento
    assert estanOrdenados