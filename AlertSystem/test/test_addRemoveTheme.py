from AlertSystem.src.Theme import Theme
from AlertSystem.src.User import User

jose = User("Jose")
alberto = User("Alberto")
roberto = User("Roberto")
maria = User("Maria")
natalia = User("Natalia")

def test_registrar_cinco_usuarios():
    espectaculos = Theme("Espectaculos")
    jose.addTheme(espectaculos)
    alberto.addTheme(espectaculos)
    roberto.addTheme(espectaculos)
    maria.addTheme(espectaculos)
    natalia.addTheme(espectaculos)
    assert len(espectaculos.getObservers()) == 5

def test_registrar_un_usuario():
    musica = Theme("Musica")
    jose.addTheme(musica)
    assert len(musica.getObservers()) == 1

def test_remuevo_tres_cuando_habia_cuatro():
    automovilismo = Theme("Automovilismo")
    jose.addTheme(automovilismo)
    alberto.addTheme(automovilismo)
    maria.addTheme(automovilismo)
    natalia.addTheme(automovilismo)
    natalia.removeTheme(automovilismo)
    maria.removeTheme(automovilismo)
    alberto.removeTheme(automovilismo)
    assert len(automovilismo.getObservers()) == 1

def test_remuevo_uno_cuando_habia_cinco():
    comida = Theme("Comida")
    jose.addTheme(comida)
    alberto.addTheme(comida)
    roberto.addTheme(comida)
    maria.addTheme(comida)
    natalia.addTheme(comida)
    jose.removeTheme(comida)
    assert len(comida.getObservers()) == 4