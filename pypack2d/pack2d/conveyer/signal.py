from enum import Enum


class SignalType(Enum):
    PUSH_INPUT = "PUSH_INPUT"
    START_PACK = "START_PACK"
    PREPARE_TO_PACK = "PREPARE_TO_PACK"
    END_PACK = "END_PACK"
    WASTE_INPUT = "WASTE_INPUT"
    CREATE_PACKER = "CREATE_PACKER"


class Signal(object):
    def __init__(self, signalType, data):
        super(Signal, self).__init__()
        self._type = signalType
        self._data = data
        pass

    type = property(lambda self: self._type)
    data = property(lambda self: self._data)
    pass
