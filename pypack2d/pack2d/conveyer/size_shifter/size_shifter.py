from pypack2d.pack2d.conveyer.unit import Unit
from pypack2d.pack2d.conveyer.signal import SignalType


class BinSizeShifter(Unit):
    def _on_init(self):
        self.connect(SignalType.END_PACK, self._on_end_to_pack)
        self.connect(SignalType.CREATE_PACKER, self._on_create_packer)

    def shift(self, bin_set):
        self._on_shift(bin_set)

    def _on_create_packer(self, packer):
        self.packer = packer
        return True

    def _on_end_to_pack(self, result):
        for bin_set in result:
            self.shift(bin_set)

        return True

    def _on_shift(self, bs):
        raise NotImplementedError()
