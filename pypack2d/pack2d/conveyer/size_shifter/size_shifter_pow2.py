from pypack2d.pack2d.conveyer.size_shifter.size_shifter import BinSizeShifter
from pypack2d.pack2d.rectangle import Rectangle
from pypack2d.pack2d.utils import get_low_pow2


class BinSizeShifterPow2(BinSizeShifter):
    def _on_shift(self, binSet):
        self.normalise_size(binSet)
        pass

    def _normalise_size(self, binSet, newWidth, newHeight):
        # print("normaliseSize")
        # print(newWidth,newHeight)

        newRect = Rectangle.from_wh(newWidth, newHeight)

        if self.can_change_rect(binSet, newRect) is False:
            # print("CANT CHANGE",newRect)
            return False
            pass

        binSet.set_size(int(newRect.width), int(newRect.height))
        return True
        pass

    pass

    def normalise_size(self, binSet):
        newWidth = get_low_pow2(binSet.width)
        newHeight = get_low_pow2(binSet.height)

        if newWidth is None or newHeight is None:
            return False
            pass

        if self._normalise_size(binSet, newWidth, newHeight) is False:
            if self._normalise_size(binSet, binSet.width, newHeight) is False:
                if self._normalise_size(binSet, newWidth, binSet.height) is False:
                    return False
                    pass
                pass
            pass

        self.normalise_size(binSet)
        return True
        pass

    def can_change_rect(self, binSet, newRect):
        for bin in binSet:
            if newRect.isContain(bin) is False:
                return False
                pass
            pass

        return True
        pass

    pass
