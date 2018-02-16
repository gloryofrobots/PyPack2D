from pypack2d.pack2d.conveyer.size_shifter.size_shifter import BinSizeShifter


class BinSizeShifterMaximal(BinSizeShifter):
    def _on_shift(self, binSet):
        maxRight = 0
        maxBottom = 0
        for bin in binSet:
            if bin.right > maxRight:
                maxRight = bin.right

            if bin.bottom > maxBottom:
                maxBottom = bin.bottom

        binSet.set_size(maxRight, maxBottom)
