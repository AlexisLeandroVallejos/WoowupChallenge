from AlertSystem.src.InformativeAlert import InformativeAlert
from AlertSystem.src.UrgentAlert import UrgentAlert
from AlertSystem.src.Theme import Theme
from AlertSystem.src.User import User

jose = User("Jose")
alberto = User("Alberto")
roberto = User("Roberto")
maria = User("Maria")
natalia = User("Natalia")

def test_notificar_alerta_a_cinco_usuarios():
    espectaculos = Theme("Espectaculos")
    alerta = InformativeAlert("Accion", "Se escucho el sonido", espectaculos)
    jose.addTheme(espectaculos)
    alberto.addTheme(espectaculos)
    roberto.addTheme(espectaculos)
    maria.addTheme(espectaculos)
    natalia.addTheme(espectaculos)
    espectaculos.notifyChange(alerta, None) #sino se pasa un user se hara notifyChangeForAll
    alertaMandadaALosCincoUsuarios = len(jose.showAlerts()) + len(alberto.showAlerts()) + len(roberto.showAlerts()) + len(
        maria.showAlerts()) + len(natalia.showAlerts())
    assert alertaMandadaALosCincoUsuarios == 5

def test_notificar_alerta_solamente_a_natalia_habiendo_mandado_alerta_a_todos_antes():
    comida = Theme("Comida")
    alerta = UrgentAlert("Tuco", "Salio riquisimo", comida)
    natalia.addTheme(comida)
    comida.notifyChange(alerta, natalia) #se ejecuta notifyChangeForOne implicitamente
    totalDeAlertasMandadas = len(jose.showAlerts()) + len(alberto.showAlerts()) + len(roberto.showAlerts()) + len(
        maria.showAlerts()) + len(natalia.showAlerts())
    assert totalDeAlertasMandadas == 6

def test_notificar_alerta_solamente_a_jose_con_usuarios_locales():
    # reiniciar usuarios para hacer este test sino daria 7
    jose = User("Jose")
    alberto = User("Alberto")
    roberto = User("Roberto")
    maria = User("Maria")
    natalia = User("Natalia")
    automovilismo = Theme("Automovilismo")
    alerta = UrgentAlert("Despisto ayer", "Salio ileso", automovilismo)
    jose.addTheme(automovilismo)
    automovilismo.notifyChange(alerta, jose) #se ejecuta notifyChangeForOne implicitamente
    alertaMandadaAUnUsuario = len(jose.showAlerts()) + len(alberto.showAlerts()) + len(roberto.showAlerts()) + len(
        maria.showAlerts()) + len(natalia.showAlerts())
    assert alertaMandadaAUnUsuario == 1

def test_cocina_trata_de_mandar_alerta_a_natalia_pero_no_esta_suscripta_a_ese_tema():
    # reiniciar usuarios para hacer este test sino daria 7
    jose = User("Jose")
    alberto = User("Alberto")
    roberto = User("Roberto")
    maria = User("Maria")
    natalia = User("Natalia")
    cocina = Theme("Cocina")
    alerta = UrgentAlert("Pollo al spiedo", "Delicioso", cocina)
    cocina.notifyChange(alerta, natalia)
    alertaMandadaAUnUsuario = len(jose.showAlerts()) + len(alberto.showAlerts()) + len(roberto.showAlerts()) + len(
        maria.showAlerts()) + len(natalia.showAlerts())
    assert alertaMandadaAUnUsuario == 0 #natalia no recibe la alerta de cocina porque no estaba suscripta

#afuera para probar ultimo test
noticia = Theme("Noticia")

def test_notificar_tres_alertas_de_tres_temas_diferentes_a_todos():
    musica = Theme("Musica")
    ciencia = Theme("Ciencia")
    alertaMusica1 = UrgentAlert("Canto la sole", "Cosquin", musica, "15-02-2023 22:30:15")
    alertaMusica2 = UrgentAlert("L-gante llego", "5 canciones", musica)
    alertaMusica3 = InformativeAlert("Mariano", "Esta recuperando la voz", musica, "15-07-2018 15:12:02")
    alertaCiencia1 = InformativeAlert("El sol se acerca", "¿para asustarse?", ciencia)
    alertaCiencia2 = InformativeAlert("El efecto invernadero", "Las vacas no hicieron nada", ciencia, "31-12-2100 00:00:00")
    alertaCiencia3 = UrgentAlert("Industrias", "El CO2 no es nuestro problema", ciencia, "01-01-1900 00:00:00")
    alertaNews1 = UrgentAlert("Cayo 'coco'", "No teman", noticia)
    alertaNews2 = InformativeAlert("Seleccion Argentina", "Horas para el encuentro", noticia, "18-12-2022 15:00:00")
    alertaNews3 = UrgentAlert("Tinelli", "Showmatch Nº42069", noticia)
    natalia.addTheme(musica)
    natalia.addTheme(ciencia)
    natalia.addTheme(noticia)
    jose.addTheme(musica)
    jose.addTheme(ciencia)
    jose.addTheme(noticia)
    roberto.addTheme(musica)
    roberto.addTheme(ciencia)
    roberto.addTheme(noticia)
    maria.addTheme(musica)
    maria.addTheme(ciencia)
    maria.addTheme(noticia)
    alberto.addTheme(musica)
    alberto.addTheme(ciencia)
    alberto.addTheme(noticia)
    musica.notifyChange(alertaMusica1, None)
    musica.notifyChange(alertaMusica2, None)
    musica.notifyChange(alertaMusica3, None)
    ciencia.notifyChange(alertaCiencia1, None)
    ciencia.notifyChange(alertaCiencia2, None)
    ciencia.notifyChange(alertaCiencia3, None)
    noticia.notifyChange(alertaNews1, None)
    noticia.notifyChange(alertaNews2, None)
    noticia.notifyChange(alertaNews3, None)
    totalDeAlertasMandadas = len(jose.showAlerts()) + len(alberto.showAlerts()) + len(roberto.showAlerts()) + len(
        maria.showAlerts()) + len(natalia.showAlerts())
    assert totalDeAlertasMandadas == 31 #las primeras 5 + la alerta de nati + 5 alertas sin expirar * 5 personas

def test_remover_a_todos_de_un_tema_anterior_y_enviar_alerta():
    jose.removeTheme(noticia)
    alberto.removeTheme(noticia)
    natalia.removeTheme(noticia)
    maria.removeTheme(noticia)
    roberto.removeTheme(noticia)
    alertaNews = UrgentAlert("Nadie lo vio", "Ahora escapo", noticia)
    noticia.notifyChange(alertaNews, None)
    totalDeAlertasMandadas = len(jose.showAlerts()) + len(alberto.showAlerts()) + len(roberto.showAlerts()) + len(
        maria.showAlerts()) + len(natalia.showAlerts())
    assert totalDeAlertasMandadas == 31 #no cambia
