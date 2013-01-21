__author__ = 'human88998999877'
from Packing2D.PackingConveyer.Unit import Unit,checkUnitForwardLinkDoesNotExist
from Packing2D.PackingConveyer.Signal import SignalType

class Collector(Unit):
    def _onInit(self):
        self.connect(SignalType.END_PACK, self._onEndToPack)
        self.result = None
        pass

    @checkUnitForwardLinkDoesNotExist
    def _onEndToPack(self, result):
        self.result = result
        pass

    def getResult(self):
        return self.result
        pass
    pass