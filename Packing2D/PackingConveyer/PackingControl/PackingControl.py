__author__ = 'human88998999877'
from PyPack2D.Packing2D.PackingConveyer.Unit import Unit
from PyPack2D.Packing2D.PackingConveyer.Signal import SignalType,Signal

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
        self.result = []
        self.lastPack  = False
        self.settings = settings
        self.factory = factory
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

        if self.settings.findMinimalBinSetSize is True and len(self.result) is not 0:
            index = len(self.result) - 1
            last =  self.result[index]
            self.result[index] = self.findMinimalSize(self.result[index])
            last2 = self.result[index]
            x = 1
            pass
        
        self.processSignal( Signal(SignalType.END_PACK, self.result) )
        return True
        pass

    def findMinimalSize(self, binSet):
        width = int(getLowPow2(binSet.getWidth()))
        height = int(getLowPow2(binSet.getHeight()))
        if width is None or height is None:
            return binSet
            pass

        self.packer.initialise(self.factory, self.settings, size = (width, height))
        bins = binSet.getBins()
        for bin in bins:
            clone = bin.clone()
            if self.packer.packBin(clone) is False:
                return binSet
                pass
            pass

        result = self.packer.flush()
        return self.findMinimalSize(result)
        pass

    def _onPrepareToPack(self, dummy):
        self.result = []
        return True
        pass
    pass
    