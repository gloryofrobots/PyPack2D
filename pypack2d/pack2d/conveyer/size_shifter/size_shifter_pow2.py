from pypack2d.pack2d.conveyer.size_shifter.size_shifter import BinSizeShifter
from pypack2d.pack2d.rectangle import Rectangle
from pypack2d.pack2d.utils import get_low_pow2


class BinSizeShifterPow2(BinSizeShifter):
    def _on_shift(self, bin_set):
        self.normalise_size(bin_set)

    def _normalise_size(self, bin_set, new_width, new_height):
        # print("normaliseSize")
        # print(newWidth,newHeight)

        new_rect = Rectangle.from_wh(new_width, new_height)

        if self.can_change_rect(bin_set, new_rect) is False:
            # print("CANT CHANGE",new_rect)
            return False

        bin_set.set_size(int(new_rect.width), int(new_rect.height))
        return True

    def normalise_size(self, bin_set):
        new_width = get_low_pow2(bin_set.width)
        new_height = get_low_pow2(bin_set.height)

        if new_width is None or new_height is None:
            return False

        if self._normalise_size(bin_set, new_width, new_height) is False:
            if self._normalise_size(bin_set, bin_set.width, new_height) is False:
                if self._normalise_size(bin_set, new_width, bin_set.height) is False:
                    return False

        self.normalise_size(bin_set)
        return True

    def can_change_rect(self, bin_set, new_rect):
        for bin in bin_set:
            if new_rect.is_contain(bin) is False:
                return False

        return True
