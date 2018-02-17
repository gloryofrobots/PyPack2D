from pypack2d.pack.conveyer.unit import Unit
from pypack2d.pack.conveyer.signal import Signal, SignalType


# split input sequence S on groups of sub sequences S1..Sn where  length each of them == count
class Filter(Unit):
    def _on_init(self, count):
        self.count = count
        self.connect(SignalType.PUSH_INPUT, self._on_push_input)

    def _on_push_input(self, input):
        if self.count <= 0:
            return

        if self.next_unit is None:
            return

        new_input = []
        count = self.count
        for image in input:
            new_input.append(image)
            count -= 1

            if count > 0:
                continue

            new_signal = Signal(SignalType.PUSH_INPUT, new_input)
            self._process_next(new_signal)

            new_input = []
            count = self.count

        # return False to stop this signal
        return False
