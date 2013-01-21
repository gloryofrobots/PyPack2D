__author__ = 'human88998999877'
from Packing2D.PackingConveyer.Unit import Unit
from Packing2D.PackingConveyer.Signal import SignalType,Signal

class PackingControl(Unit):
    def _onInit(self, packer):
        self.packer = packer
        self.result = []
        self.connect(SignalType.PUSH_INPUT, self._onPushInput)
        self.connect(SignalType.PREPARE_TO_PACK, self._onPrepareToPack)
        self.connect(SignalType.START_PACK, self._onStartPack)
        pass

    def _onPushInput(self, input):
        for bin in input:
            if self.packer.packBin(bin) is False:
                binSet = self.packer.flush()
                self.result.append(binSet)
                pass
            pass
        pass

    def _onStartPack(self, dummy):
        self.processSignal( Signal(SignalType.END_PACK, self.result) )
        pass

    def _onPrepareToPack(self, dummy):
        pass
    pass
    