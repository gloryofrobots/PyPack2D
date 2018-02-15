__author__ = 'human88998999877'
from pypack2d.Packing2D.PackingConveyer.Unit import Unit
from pypack2d.Packing2D.PackingConveyer.Signal import SignalType,Signal

def getLowPow2( x ):
    y = 2
    if y >= x:
        return None
    while True:
        if y >= x:
            return y / 2
            pass
        y *= 2
        pass
    pass

class PackingControl(Unit):
    def _onInit(self, packer, factory, settings):
        self.packer = packer
        self.packer.initialise(factory, settings)
        self.packer.setSize(settings.maxWidth, settings.maxHeight)

        self.result = []
        self.lastPack  = False

        self.connect(SignalType.PUSH_INPUT, self._onPushInput)
        self.connect(SignalType.PREPARE_TO_PACK, self._onPrepareToPack)
        self.connect(SignalType.START_PACK, self._onStartPack)
        pass

    def packBins(self, input):
        self.lastPack  = False
        index = 0
        while True:
            if index == len(input):
                break
                pass

            bin = input[index]

            self.lastPack = self.packer.packBin(bin)

            if self.lastPack is True:
                index += 1
                continue
                pass

            binSet = self.packer.flush()
            self.result.append(binSet)
            pass
        pass

    def _onPushInput(self, input):
        self.packBins(input)
        return True
        pass

    def checkLastPack(self):
        if self.lastPack is False:
            return
            pass

        binSet = self.packer.flush()
        self.result.append(binSet)
        pass

    def _onStartPack(self, dummy):
        #TODO REFACTOR
        self.checkLastPack()
        self.processSignal( Signal(SignalType.END_PACK, self.result) )
        return True
        pass

    def _onPrepareToPack(self, dummy):
        self.processSignal( Signal(SignalType.CREATE_PACKER, self.packer) )
        self.result = []
        return True
        pass
    pass
