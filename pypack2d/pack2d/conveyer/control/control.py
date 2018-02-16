from pypack2d.pack2d.conveyer.unit import Unit
from pypack2d.pack2d.conveyer.signal import SignalType, Signal


class PackingControl(Unit):
    def _on_init(self, packer, factory, settings):
        self.packer = packer
        self.packer.initialise(factory, settings)
        self.packer.set_size(settings.max_width, settings.max_height)

        self.result = []
        self.lastPack = False

        self.connect(SignalType.PUSH_INPUT, self._on_push_input)
        self.connect(SignalType.PREPARE_TO_PACK, self._on_prepare_to_pack)
        self.connect(SignalType.START_PACK, self._on_start_pack)

    def pack_bins(self, input):
        self.lastPack = False
        index = 0
        while True:
            if index == len(input):
                break

            bin = input[index]

            self.lastPack = self.packer.pack_bin(bin)

            if self.lastPack is True:
                index += 1
                continue

            binSet = self.packer.flush()
            self.result.append(binSet)

    def _on_push_input(self, input):
        self.pack_bins(input)
        return True

    def check_last_pack(self):
        if self.lastPack is False:
            return

        binSet = self.packer.flush()
        self.result.append(binSet)

    def _on_start_pack(self, dummy):
        # TODO REFACTOR
        self.check_last_pack()
        self.process_signal(Signal(SignalType.END_PACK, self.result))
        return True

    def _on_prepare_to_pack(self, dummy):
        self.process_signal(Signal(SignalType.CREATE_PACKER, self.packer))
        self.result = []
        return True
