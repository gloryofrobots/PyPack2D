from pypack2d.pack2d.PackingConveyer.BinSizeShifter.BinSizeShifterPow2 import BinSizeShifterPow2,getLowPow2

class BinSizeShifterPow2MinimizeLast(BinSizeShifterPow2):
    def _onEndToPack(self, result):
        #TODO FIXME
        if len(result) is 0:
            return True
            pass

        #get last binSet and try to pack all it bins to smaller
        index = len(result) - 1
        minimized = self.findMinimalSize(result[index])
        #minimize all binSets
        super(BinSizeShifterPow2, self)._onEndToPack(result)

        #compare last minimized binSet with old last binSet
        self.normaliseSize(minimized)
        old = result[index]
        if old.getEfficiency() < minimized.getEfficiency():
            result[index] = minimized
            pass

        return True
        pass

    def findMinimalSize(self, binSet):
        width = getLowPow2(binSet.getWidth())
        height = getLowPow2(binSet.getHeight())
        if width is None or height is None:
            return binSet
            pass

        self.packer.setSize(int(width), int(height))
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
    pass