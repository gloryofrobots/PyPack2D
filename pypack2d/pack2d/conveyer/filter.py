from pypack2d.pack2d.conveyer.unit import Unit
from pypack2d.pack2d.conveyer.signal import Signal, SignalType


# split input sequence S on groups of sub sequences S1..Sn where  length each of them == count
class Filter(Unit):
    def _on_init(self, count):
        self.count = count
        self.connect(SignalType.PUSH_INPUT, self._on_push_input)

    def _on_push_input(self, input):
        if self.count <= 0:
            return

        if self.nextUnit is None:
            return

        newInput = []
        count = self.count
        for image in input:
            newInput.append(image)
            count -= 1

            if count > 0:
                continue

            newSignal = Signal(SignalType.PUSH_INPUT, newInput)
            self._process_next(newSignal)

            newInput = []
            count = self.count


        # return False to stop this signal
        return False
