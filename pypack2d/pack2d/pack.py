from pypack2d.pack2d.conveyer.conveyer import Conveyer
from pypack2d.pack2d import Factories

from pypack2d.pack2d.conveyer.signal import SignalType, Signal


class Pack2D(object):
    def __init__(self, settings):
        super(Pack2D, self).__init__()
        self.factories = Factories
        self.conveyer = Conveyer()
        builder = self.factories.conveyer_builder.create_instance(settings.packing_mode)
        builder.build(self.conveyer, self.factories, settings)
        signal = Signal(SignalType.PREPARE_TO_PACK, None)
        self.conveyer.process_signal(signal)

    def pack(self):
        signal = Signal(SignalType.START_PACK, None)
        self.conveyer.process_signal(signal)

    def get_result(self):
        return self.conveyer.get_result()

    def get_waste(self):
        return self.conveyer.get_waste()

    def push(self, input):
        _input = input
        if isinstance(input, list) is False:
            _input = [input]

        signal = Signal(SignalType.PUSH_INPUT, _input)
        self.conveyer.process_signal(signal)
