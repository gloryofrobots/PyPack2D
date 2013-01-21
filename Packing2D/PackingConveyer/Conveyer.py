__author__ = 'human88998999877'
from Packing2D.PackingConveyer.Unit import Unit,checkUnitForwardLinkExist
from Packing2D.PackingConveyer.Signal import SignalType
from Packing2D.PackingConveyer.Collector import Collector


class Conveyer(Unit):
    def _onInit(self):
        self.connect(SignalType.PREPARE_TO_PACK, self._onPrepareToPack)
        self.connect(SignalType.WASTE_INPUT, self._onWasteInput)
        self.collector = Collector()
        self.waste = []
        pass

    @checkUnitForwardLinkExist
    def _onPrepareToPack(self, dummy):
        self.pushUnit(self.collector)
        return True
        pass

    def _onWasteInput(self, waste):
        self.waste.extend(waste)
        pass

    def getResult(self):
        return self.collector.getResult()
        pass

    def getWaste(self):
        return self.waste
        pass
    pass