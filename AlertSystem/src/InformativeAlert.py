#necesito mas informacion sobre que la hace informativa!
#no se justifica su existencia sino, solamente para usar booleanas por punto 11
from AlertSystem.src.Alert import Alert

class InformativeAlert(Alert):

    def __init__(self, *args):
        Alert.__init__(self, *args)
    
    def isInformative(self):
        return True

    def isUrgent(self):
        return False    