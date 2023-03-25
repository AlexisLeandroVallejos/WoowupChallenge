from AlertSystem.src.Observable import Observable

class Theme(Observable):
    def __init__(self, name):
        Observable.__init__(self, name)
        self.observers = []

    def addObserver(self, observer):
        self.observers.append(observer)

    def removeObserver(self, observer):
        self.observers.remove(observer)

    def notifyChange(self, alert, observer):
        if observer:
            self.notifyChangeForOne(alert, observer)
        else:
            self.notifyChangeForAll(alert)

    def notifyChangeForOne(self, alert, observer):
        if observer in self.observers:
            alert.recordSent()
            observer.notifyChange(alert)

    def notifyChangeForAll(self, alert):
        for observer in self.observers:
            alert.recordSent()
            observer.notifyChange(alert)

    def getObservers(self):
        return self.observers