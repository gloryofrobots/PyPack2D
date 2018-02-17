from pypack2d.pack.conveyer.unit import Unit, check_unit_forward_link_exist
from pypack2d.pack.conveyer.signal import SignalType, Signal


class Accumulator(Unit):
    def _on_init(self):
        self.connect(SignalType.START_PACK, self._on_start_pack)
        self.connect(SignalType.PUSH_INPUT, self._on_push_input)

        self.input = []

    @check_unit_forward_link_exist
    def _on_start_pack(self, dummy):
        new_signal = Signal(SignalType.PUSH_INPUT, self.input)
        self._process_next(new_signal)
        return True

    @check_unit_forward_link_exist
    def _on_push_input(self, input):
        self.input.extend(input)
        # stop diffusion of the  signal
        return False
