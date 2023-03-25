from AlertSystem.src.InformativeAlert import InformativeAlert
from AlertSystem.src.UrgentAlert import UrgentAlert
from AlertSystem.src.Theme import Theme
from AlertSystem.src.User import User

jose = User("Jose")
maria = User("Maria")
roberto = User("Roberto")

automovilismo = Theme("Automovilismo")
cine = Theme("Cine")
cocina = Theme("Cocina")

alertaAutomovilismo1 = InformativeAlert("¿Pero lo dejarias pasar?", "Alonso is faster than you", automovilismo)
alertaAutomovilismo2 = InformativeAlert("YOUR DAYS ARE GONE!", "G. CEARA", automovilismo)
alertaAutomovilismo3 = InformativeAlert("Indianapolis 2005", "No lo entenderias...", automovilismo)

alertaCine1 = UrgentAlert("Frozen", "Records de visualizacion", cine)
alertaCine2 = InformativeAlert("Argentina, 1985", "Otro premio para la pelicula", cine)
alertaCine3 = UrgentAlert("Doble cafe", "Intenso y violento", cine)

alertaCocina1 = InformativeAlert("Cremona rellena", "Falta levadura", cocina)
alertaCocina2 = InformativeAlert("Isla Flotante", "Falta caramelo", cocina)
alertaCocina3 = UrgentAlert("Sandwich de milanesa al caballo", "Entradas vendidas", cocina)

jose.addTheme(automovilismo)
jose.addTheme(cine)
jose.addTheme(cocina)

automovilismo.notifyChange(alertaAutomovilismo1, None)
automovilismo.notifyChange(alertaAutomovilismo2, None)
automovilismo.notifyChange(alertaAutomovilismo3, None)

cine.notifyChange(alertaCine1, None)        #U1
cine.notifyChange(alertaCine2, None)        #I2
cine.notifyChange(alertaCine3, None)        #U3
cocina.notifyChange(alertaCocina1, None)    #I4
cocina.notifyChange(alertaCocina2, None)    #I5
cocina.notifyChange(alertaCocina3, None)    #U6

def test_maria_no_lee_ninguna_alerta():
    costura = Theme("Costura")
    alertaCostura1 = UrgentAlert("Goma eva", "¿util?", costura)
    alertaCostura2 = UrgentAlert("retazos", "¿que se puede hacer?", costura)
    maria.addTheme(costura)
    costura.notifyChange(alertaCostura1, None)
    costura.notifyChange(alertaCostura2, None)
    assert len(maria.showUnreadedAlerts()) == 2

def test_jose_lee_solamente_los_tres_temas_de_automovilismo_seis_quedan_sin_leer():
    jose.readAlert(alertaAutomovilismo1)
    jose.readAlert(alertaAutomovilismo2)
    jose.readAlert(alertaAutomovilismo3)
    assert len(jose.showUnreadedAlerts()) == 6

def test_roberto_recibe_dos_alertas_y_lee_una_automovilistica_la_otra_estaba_expirada():
    noticia = Theme("Noticia")
    alertaNoticiosaExpirada = UrgentAlert("Detienen al mas buscado", "estaba en un estado de USA", noticia, "22-06-2005 15:01:01")
    roberto.addTheme(automovilismo)
    roberto.addTheme(noticia)
    automovilismo.notifyChange(alertaAutomovilismo2, roberto)
    noticia.notifyChange(alertaNoticiosaExpirada, roberto)
    roberto.readAlert(alertaAutomovilismo2)
    assert len(roberto.showUnreadedAlerts()) == 0

def test_las_alertas_no_leidas_de_jose_estan_ordenadas():
    # segun enunciado las no leidas de jose deberian estar asi: [U6,U3,U1,I2,I4,I5]
    primerElemento = jose.showUnreadedAlerts()[0] == alertaCocina3
    segundoElemento =jose.showUnreadedAlerts()[1] == alertaCine3
    tercerElemento = jose.showUnreadedAlerts()[2] == alertaCine1
    cuartoElemento = jose.showUnreadedAlerts()[3] == alertaCine2
    quintoElemento = jose.showUnreadedAlerts()[4] == alertaCocina1
    sextoElemento =  jose.showUnreadedAlerts()[5] == alertaCocina2
    estanOrdenados = primerElemento and segundoElemento and tercerElemento and cuartoElemento and quintoElemento and sextoElemento
    assert estanOrdenados