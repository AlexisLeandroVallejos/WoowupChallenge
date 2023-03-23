from SistemaDeAlertas.src.Tema import Tema
from SistemaDeAlertas.src.Usuario import Usuario

jose = Usuario("Jose")
alberto = Usuario("Alberto")
roberto = Usuario("Roberto")
maria = Usuario("Maria")
natalia = Usuario("Natalia")

def test_registrar_cinco_usuarios():
    espectaculos = Tema("Espectaculos")
    espectaculos.addObserver(jose)
    espectaculos.addObserver(alberto)
    espectaculos.addObserver(roberto)
    espectaculos.addObserver(maria)
    espectaculos.addObserver(natalia)
    assert len(espectaculos.getObservers()) == 5

def test_registrar_un_usuario():
    musica = Tema("Musica")
    musica.addObserver(jose)
    assert len(musica.getObservers()) == 1

def test_remuevo_tres_cuando_habia_cuatro():
    automovilismo = Tema("Automovilismo")
    automovilismo.addObserver(jose)
    automovilismo.addObserver(alberto)
    automovilismo.addObserver(maria)
    automovilismo.addObserver(natalia)
    automovilismo.removeObserver(natalia)
    automovilismo.removeObserver(maria)
    automovilismo.removeObserver(alberto)
    assert len(automovilismo.getObservers()) == 1

def test_remuevo_uno_cuando_habia_cinco():
    comida = Tema("Comida")
    comida.addObserver(jose)
    comida.addObserver(alberto)
    comida.addObserver(roberto)
    comida.addObserver(maria)
    comida.addObserver(natalia)
    comida.removeObserver(jose)
    assert len(comida.getObservers()) == 4