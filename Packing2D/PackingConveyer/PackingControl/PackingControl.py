__author__ = 'human88998999877'
from Packing2D.PackingConveyer.Unit import Unit
from Packing2D.PackingConveyer.Signal import SignalType,Signal

class PackingControl(Unit):
    def _onInit(self, packer, factory, settings):
        self.packer = packer
        self.packer.initialise(factory, settings)
        self.lastPack = False
        self.result = []
        self.connect(SignalType.PUSH_INPUT, self._onPushInput)
        self.connect(SignalType.PREPARE_TO_PACK, self._onPrepareToPack)
        self.connect(SignalType.START_PACK, self._onStartPack)
        pass
    
    def _onPushInput(self, input):
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

        return True
        pass

    def _onStartPack(self, dummy):
        #TODO REFACTOR
        if self.lastPack is True:
            binSet = self.packer.flush()
            self.result.append(binSet)
            pass
        
        self.processSignal( Signal(SignalType.END_PACK, self.result) )
        return True
        pass

    def _onPrepareToPack(self, dummy):
        self.result = []
        return True
        pass
    pass
    