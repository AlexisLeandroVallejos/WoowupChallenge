from AlertSystem.src.AlertSystem import AlertSystem
from AlertSystem.src.Observer import Observer

class User(Observer):
    def __init__(self, name):
        Observer.__init__(self, name)
        self.alertSystem = AlertSystem()

    def addTheme(self, theme):
        theme.addObserver(self)

    def removeTheme(self, theme):
        theme.removeObserver(self)

    def notifyChange(self, alert):
        self.alertSystem.addAlert(alert)

    #devuelve solamente las alertas que no estan expiradas
    def showAlerts(self):
        return self.alertSystem.showAlerts()

    def readAlert(self, alert):
        self.alertSystem.readAlert(alert)

    def showUnreadedAlerts(self):
        return self.alertSystem.showUnreadedAlerts()

    def showThemedAlerts(self, theme):
        return self.alertSystem.showThemedAlerts(theme)
