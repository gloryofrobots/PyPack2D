from pypack2d.pack.conveyer.size_shifter.size_shifter import BinSizeShifter


class BinSizeShifterMaximal(BinSizeShifter):
    def _on_shift(self, binSet):
        max_right = 0
        max_bottom = 0
        for bin in binSet:
            if bin.right > max_right:
                max_right = bin.right

            if bin.bottom > max_bottom:
                max_bottom = bin.bottom

        binSet.set_size(max_right, max_bottom)
