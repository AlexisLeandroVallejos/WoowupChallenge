import time
from datetime import datetime

class Alert:
    DATE_TIME_FORMAT = "%d-%m-%Y %H:%M:%S"
    DELAY_BETWEEN_SENT = 1e-9
    def __init__(self, *args):
        self.isExpired = False
        self.isRead = False
        self.sent = None
        if len(args) == 3:
            self.name = args[0]
            self.description = args[1]
            self.theme = args[2]
            self.expirationDateAndTime = None
        else:
            self.name = args[0]
            self.description = args[1]
            self.theme = args[2]
            self.expirationDateAndTime = datetime.strptime(args[3], self.DATE_TIME_FORMAT)

    def isInformative(self):
        pass

    def isUrgent(self):
        pass

    def getCurrentDatetime(self):
        return datetime.now()

    def expirationControl(self):
        if self.expirationDateAndTime and self.expirationDateAndTime <= self.getCurrentDatetime():
            self.isExpired = True

    def getIsExpired(self):
        return self.isExpired

    def getIsRead(self):
        return self.isRead

    def read(self):
        self.isRead = True

    def getTheme(self):
        return self.theme

    def isSameTheme(self, theme):
        return self.getTheme() == theme

    def recordSent(self):
        # es posible que se envien en el mismo tiempo que otra alerta
        # sobretodo cuando el envio esta uno debajo del otro
        time.sleep(self.DELAY_BETWEEN_SENT) #para evitarlo
        self.sent = self.getCurrentDatetime()

    def getSent(self):
        return self.sent



