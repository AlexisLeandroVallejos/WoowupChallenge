class AlertSystem:
    def __init__(self):
        self.alerts = []

    def addAlert(self, alert):
        self.alerts.append(alert)

    #mostrar alertas no expiradas, las que esten expiradas se eliminan
    def showAlerts(self):
        updatedAlerts = []
        for alert in self.alerts:
            alert.expirationControl()
            if not alert.getIsExpired():
                updatedAlerts.append(alert)
        self.alerts = updatedAlerts
        return self.alerts

    def readAlert(self, alert):
        if alert in self.showAlerts():
            alert.read()

    def showUnreadedAlerts(self):
        unreadedAlerts = []
        for alert in self.showAlerts():
            if not alert.getIsRead():
                unreadedAlerts.append(alert)
        return self.showUnreadedAlertsOrdered(unreadedAlerts)

    def showThemedAlerts(self, theme):
        themedAlerts = []
        for alert in self.showAlerts():
            if alert.isSameTheme(theme):
                themedAlerts.append(alert)
        return self.showThemedAlertsOrdered(themedAlerts)

    def sortUrgentAlerts(self, unsortedListOfAlerts):
        urgentAlerts = []
        for alert in unsortedListOfAlerts:
            if alert.isUrgent():
                urgentAlerts.append(alert)
        return sorted(urgentAlerts, key=lambda alert: alert.getSent(), reverse=True)

    def sortInformativeAlerts(self, unsortedListOfAlerts):
        informativeAlerts = []
        for alert in unsortedListOfAlerts:
            if alert.isInformative():
                informativeAlerts.append(alert)
        return sorted(informativeAlerts, key=lambda alert: alert.getSent())

    def showUnreadedAlertsOrdered(self, unreadedAlerts):
        return self.sortUrgentAlerts(unreadedAlerts) + self.sortInformativeAlerts(unreadedAlerts)

    def showThemedAlertsOrdered(self, themedAlerts):
        return self.sortUrgentAlerts(themedAlerts) + self.sortInformativeAlerts(themedAlerts)