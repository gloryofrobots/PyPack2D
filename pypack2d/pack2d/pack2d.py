from pypack2d.pack2d.conveyer.conveyer import Conveyer
from pypack2d.pack2d import packingFactory

from pypack2d.pack2d.conveyer.signal import SignalType,Signal

class Pack2D(object):
    def __init__(self):
        super(Pack2D, self).__init__()
        self.conveyer = None

        self.factory = packingFactory

        pass

    def initialise(self, settings):
        self.conveyer = Conveyer()
        builder = self.factory.create_instance(settings.packingMode)
        builder.build(self.conveyer, self.factory, settings)
        signal = Signal(SignalType.PREPARE_TO_PACK, None)
        self.conveyer.process_signal(signal)
        pass

    def pack(self):
        signal = Signal(SignalType.START_PACK, None)
        self.conveyer.process_signal(signal)
        pass

    def getResult(self):
        return self.conveyer.getResult()
        pass

    def getWaste(self):
        return self.conveyer.getWaste()
        pass

    def push(self, input):
        _input = input
        if isinstance(input, list) is False:
            _input = [input]
            pass

        signal = Signal(SignalType.PUSH_INPUT, _input)
        self.conveyer.process_signal(signal)
        pass
    pass