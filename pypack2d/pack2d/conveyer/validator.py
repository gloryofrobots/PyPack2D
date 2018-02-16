from pypack2d.pack2d.conveyer.unit import Unit, check_unit_forward_link_does_not_exist
from pypack2d.pack2d.conveyer.signal import SignalType, Signal


class Validator(Unit):
    def _on_init(self, max_width, max_height):
        self.max_width = max_width
        self.max_height = max_height
        self.connect(SignalType.PUSH_INPUT, self._on_push_input)

    def _on_push_input(self, input):
        waste = []
        for bin in input:
            if bin.width > self.max_width or bin.height > self.max_height:
                waste.append(bin)
                input.remove(bin)

        self.process_signal(Signal(SignalType.WASTE_INPUT, waste))
        return True
