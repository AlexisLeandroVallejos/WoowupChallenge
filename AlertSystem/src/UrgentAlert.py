#necesito mas informacion sobre que la hace urgente!
#no se justifica su existencia sino, solamente para usar booleanas por punto 11
from AlertSystem.src.Alert import Alert

class UrgentAlert(Alert):

    def __init__(self, *args):
        Alert.__init__(self, *args)

    def isInformative(self):
        return False

    def isUrgent(self):
        return True    