from pypack2d.pack2d.conveyer.unit import Unit,check_unit_forward_link_exist
from pypack2d.pack2d.conveyer.signal import SignalType,Signal

class Accumulator(Unit):
    def _on_init(self):
        self.connect(SignalType.START_PACK, self._on_start_pack)
        self.connect(SignalType.PUSH_INPUT, self._on_push_input)

        self.input = []
        pass

    @check_unit_forward_link_exist
    def _on_start_pack(self, dummy):
        newSignal = Signal(SignalType.PUSH_INPUT, self.input)
        self._process_next(newSignal)
        return True
        pass

    @check_unit_forward_link_exist
    def _on_push_input(self, input):
        self.input.extend(input)
        #stop diffusion of the  signal
        return False
        pass
    pass