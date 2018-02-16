from pypack2d.pack2d.conveyer.size_shifter.size_shifter_pow2 import BinSizeShifterPow2, get_low_pow2


class BinSizeShifterPow2MinimizeLast(BinSizeShifterPow2):
    def _on_end_to_pack(self, result):
        # TODO FIXME
        if len(result) is 0:
            return True


        # get last binSet and try to pack all it bins to smaller
        index = len(result) - 1
        minimized = self.find_minimal_size(result[index])
        # minimize all binSets
        super(BinSizeShifterPow2, self)._on_end_to_pack(result)

        # compare last minimized binSet with old last binSet
        self.normalise_size(minimized)
        old = result[index]
        if old.get_efficiency() < minimized.getEfficiency():
            result[index] = minimized

        return True

    def find_minimal_size(self, bin_set):
        width = get_low_pow2(bin_set.width)
        height = get_low_pow2(bin_set.height)
        if width is None or height is None:
            return bin_set

        self.packer.set_size(int(width), int(height))
        bins = bin_set.getBins()
        for bin in bins:
            clone = bin.clone()
            if self.packer.pack_bin(clone) is False:
                return bin_set

        result = self.packer.flush()
        return self.find_minimal_size(result)
