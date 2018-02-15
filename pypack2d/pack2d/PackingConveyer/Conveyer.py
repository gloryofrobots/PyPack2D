from pypack2d.pack2d.PackingConveyer.Unit import Unit,checkUnitForwardLinkExist
from pypack2d.pack2d.PackingConveyer.Signal import SignalType
from pypack2d.pack2d.PackingConveyer.Collector import Collector


class Conveyer(Unit):
    def _onInit(self):
        self.connect(SignalType.PREPARE_TO_PACK, self._onPrepareToPack)
        self.collector = Collector()
        self.waste = []
        pass

    @checkUnitForwardLinkExist
    def _onPrepareToPack(self, dummy):
        self.pushUnit(self.collector)
        return True
        pass

    def getResult(self):
        return self.collector.getResult()
        pass

    def getWaste(self):
        return self.collector.getWaste()
        pass
    pass