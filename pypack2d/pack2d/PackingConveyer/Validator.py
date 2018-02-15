from pypack2d.pack2d.PackingConveyer.Unit import Unit,checkUnitForwardLinkDoesNotExist
from pypack2d.pack2d.PackingConveyer.Signal import SignalType, Signal

class Validator(Unit):
    def _onInit(self, maxWidth, maxHeight):
        self.maxWidth = maxWidth
        self.maxHeight = maxHeight
        self.connect(SignalType.PUSH_INPUT, self._onPushInput)
        pass


    def _onPushInput(self, input):
        waste = []
        for bin in input:
            if bin.width > self.maxWidth or bin.height > self.maxHeight:
                waste.append(bin)
                input.remove(bin)
                pass
            pass
        self.processSignal( Signal(SignalType.WASTE_INPUT, waste) )
        return True
        pass
    pass
