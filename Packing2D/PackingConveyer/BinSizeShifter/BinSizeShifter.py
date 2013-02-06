from PyPack2D.Packing2D.PackingConveyer.Unit import Unit
from PyPack2D.Packing2D.PackingConveyer.Signal import SignalType

class BinSizeShifter(Unit):
    def _onInit(self):
        self.connect(SignalType.END_PACK, self._onEndToPack)
        pass

    def shift(self, binSet):
        self._onShift(binSet)
        pass

    def _onEndToPack(self, result):
        for binSet in result:
            self.shift(binSet)
            pass

        return True
        pass

    def _onShift(self, binSet):
        raise NotImplementedError()
        pass
    pass
  