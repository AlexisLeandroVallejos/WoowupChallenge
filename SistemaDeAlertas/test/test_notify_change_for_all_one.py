from SistemaDeAlertas.src.AlertaInformativa import AlertaInformativa
from SistemaDeAlertas.src.AlertaUrgente import AlertaUrgente
from SistemaDeAlertas.src.Tema import Tema
from SistemaDeAlertas.src.Usuario import Usuario

jose = Usuario("Jose")
alberto = Usuario("Alberto")
roberto = Usuario("Roberto")
maria = Usuario("Maria")
natalia = Usuario("Natalia")

def test_notificar_alerta_a_cinco_usuarios():
    espectaculos = Tema("Espectaculos")
    alerta = AlertaInformativa(nombre="Accion", descripcion="Se escucho el sonido", tema=espectaculos)
    espectaculos.addObserver(jose)
    espectaculos.addObserver(alberto)
    espectaculos.addObserver(roberto)
    espectaculos.addObserver(maria)
    espectaculos.addObserver(natalia)
    espectaculos.notifyChangeForAll(alerta)
    alertaMandadaALosCincoUsuarios = len(jose.getAlerts())+len(alberto.getAlerts())+len(roberto.getAlerts())+len(maria.getAlerts())+len(natalia.getAlerts())
    assert alertaMandadaALosCincoUsuarios == 5

def test_notificar_alerta_solamente_a_natalia_habiendo_mandado_alerta_a_todos_antes():
    comida = Tema("Comida")
    alerta = AlertaUrgente(nombre="Tuco", descripcion="Salio riquisimo", tema=comida)
    comida.addObserver(natalia)
    comida.notifyChangeForOne(alerta, natalia)
    totalDeAlertasMandadas = len(jose.getAlerts()) + len(alberto.getAlerts()) + len(roberto.getAlerts()) + len(
        maria.getAlerts()) + len(natalia.getAlerts())
    assert totalDeAlertasMandadas == 6

def test_notificar_alerta_solamente_a_jose_con_usuarios_locales():
    # reiniciar usuarios para hacer el test sino daria 7
    jose = Usuario("Jose")
    alberto = Usuario("Alberto")
    roberto = Usuario("Roberto")
    maria = Usuario("Maria")
    natalia = Usuario("Natalia")
    automovilismo = Tema("Automovilismo")
    alerta = AlertaUrgente(nombre="Despisto ayer", descripcion="Salio ileso", tema=automovilismo)
    automovilismo.addObserver(jose)
    automovilismo.notifyChangeForOne(alerta, jose)
    alertaMandadaAUnUsuario = len(jose.getAlerts()) + len(alberto.getAlerts()) + len(roberto.getAlerts()) + len(
        maria.getAlerts()) + len(natalia.getAlerts())
    assert alertaMandadaAUnUsuario == 1

def test_cocina_trata_de_mandar_alerta_a_natalia_pero_no_esta_suscripta_a_ese_tema():
    # reiniciar usuarios para hacer el test sino daria 7
    jose = Usuario("Jose")
    alberto = Usuario("Alberto")
    roberto = Usuario("Roberto")
    maria = Usuario("Maria")
    natalia = Usuario("Natalia")
    cocina = Tema("Cocina")
    alerta = AlertaUrgente(nombre="Pollo al spiedo", descripcion="Delicioso", tema=cocina)
    cocina.notifyChangeForOne(alerta, natalia)
    alertaMandadaAUnUsuario = len(jose.getAlerts()) + len(alberto.getAlerts()) + len(roberto.getAlerts()) + len(
        maria.getAlerts()) + len(natalia.getAlerts())
    assert alertaMandadaAUnUsuario == 0 #natalia no recibe la alerta de cocina porque no estaba suscripta

#afuera para probar ultimo test
noticia = Tema("Noticia")

def test_notificar_tres_alertas_de_tres_temas_diferentes_a_todos():
    musica = Tema("Musica")
    ciencia = Tema("Ciencia")
    alertaMusica1 = AlertaUrgente(nombre="Canto la sole", descripcion="Cosquin", tema=musica, fechaYhoraExpiracion="15-02-2023 22:30:15")
    alertaMusica2 = AlertaUrgente(nombre="L-gante llego", descripcion="5 canciones", tema=musica)
    alertaMusica3 = AlertaInformativa(nombre="Mariano", descripcion="Esta recuperando la voz", tema=musica, fechaYhoraExpiracion="15-07-2018 15:12:02")
    alertaCiencia1 = AlertaInformativa(nombre="El sol se acerca", descripcion="¿para asustarse?", tema=ciencia)
    alertaCiencia2 = AlertaInformativa(nombre="El efecto invernadero", descripcion="Las vacas no hicieron nada", tema=ciencia, fechaYhoraExpiracion="31-12-2100 00:00:00")
    alertaCiencia3 = AlertaUrgente(nombre="Industrias", descripcion="El CO2 no es nuestro problema", tema=ciencia, fechaYhoraExpiracion="01-01-1900 00:00:00")
    alertaNews1 = AlertaUrgente(nombre="Cayo 'coco'", descripcion="No teman", tema=noticia)
    alertaNews2 = AlertaInformativa(nombre="Seleccion Argentina", descripcion="Horas para el encuentro", tema=noticia, fechaYhoraExpiracion="18-12-2022 15:00:00")
    alertaNews3 = AlertaUrgente(nombre="Tinelli", descripcion="Showmatch Nº42069", tema=noticia)
    musica.addObserver(natalia)
    musica.addObserver(jose)
    musica.addObserver(maria)
    musica.addObserver(alberto)
    musica.addObserver(roberto)
    ciencia.addObserver(natalia)
    ciencia.addObserver(jose)
    ciencia.addObserver(maria)
    ciencia.addObserver(alberto)
    ciencia.addObserver(roberto)
    noticia.addObserver(natalia)
    noticia.addObserver(jose)
    noticia.addObserver(maria)
    noticia.addObserver(alberto)
    noticia.addObserver(roberto)
    musica.notifyChangeForAll(alertaMusica1)
    musica.notifyChangeForAll(alertaMusica2)
    musica.notifyChangeForAll(alertaMusica3)
    ciencia.notifyChangeForAll(alertaCiencia1)
    ciencia.notifyChangeForAll(alertaCiencia2)
    ciencia.notifyChangeForAll(alertaCiencia3)
    noticia.notifyChangeForAll(alertaNews1)
    noticia.notifyChangeForAll(alertaNews2)
    noticia.notifyChangeForAll(alertaNews3)
    totalDeAlertasMandadas = len(jose.getAlerts()) + len(alberto.getAlerts()) + len(roberto.getAlerts()) + len(
        maria.getAlerts()) + len(natalia.getAlerts())
    assert totalDeAlertasMandadas == 51 #9 alertas * 5 personas + la alerta de nati + las primeras 5

def test_remover_a_todos_de_un_tema_anterior_y_enviar_alerta():
    noticia.removeObserver(jose)
    noticia.removeObserver(alberto)
    noticia.removeObserver(natalia)
    noticia.removeObserver(maria)
    noticia.removeObserver(roberto)
    alertaNews = AlertaUrgente(nombre="Nadie lo vio", descripcion="Ahora escapo", tema=noticia)
    noticia.notifyChangeForAll(alertaNews)
    totalDeAlertasMandadas = len(jose.getAlerts()) + len(alberto.getAlerts()) + len(roberto.getAlerts()) + len(
        maria.getAlerts()) + len(natalia.getAlerts())
    assert totalDeAlertasMandadas == 51 #no cambia
