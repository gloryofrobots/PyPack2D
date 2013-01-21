__author__ = 'human88998999877'
from Packing2D.PackingConveyer.Unit import Unit,checkUnitForwardLinkExist
from Packing2D.PackingConveyer.Signal import SignalType,Signal

class Accumulator(Unit):
    def _onInit(self):
        self.connect(SignalType.PREPARE_TO_PACK, self._onPrepareToPack)
        self.connect(SignalType.PUSH_INPUT, self._onPushInput)

        self.input = []
        pass

    @checkUnitForwardLinkExist
    def _onPrepareToPack(self, dummy):
        newSignal = Signal(SignalType.PUSH_INPUT, self.input)
        self._processNext(newSignal)
        pass

    @checkUnitForwardLinkExist
    def _onPushInput(self, input):
        self.input.extend(input)
        #stop diffusion of the  signal
        return False
        pass
    pass