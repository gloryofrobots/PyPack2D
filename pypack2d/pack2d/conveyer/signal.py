from enum import Enum


class SignalType(Enum):
    PUSH_INPUT = "PUSH_INPUT"
    START_PACK = "START_PACK"
    PREPARE_TO_PACK = "PREPARE_TO_PACK"
    END_PACK = "END_PACK"
    WASTE_INPUT = "WASTE_INPUT"
    CREATE_PACKER = "CREATE_PACKER"


class Signal(object):
    def __init__(self, signal_type, data):
        super(Signal, self).__init__()
        self.type = signal_type
        self.data = data
