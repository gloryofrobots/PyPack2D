__author__ = 'human88998999877'
from Packing2D.Enum.Enum import Enum

SignalType = Enum(
    "PUSH_INPUT" #send from filters, accumulators, Packing2D
    , "START_PACK" #send from Packing2D
    , "PREPARE_TO_PACK" #send from Packing2D
    , "END_PACK" #send from PackingControl
    , "WASTE_INPUT")

class Signal(object):
    def __init__(self, signalType, data):
        super(Signal, self).__init__()
        self._type = signalType
        self._data = data
        pass

    type = property( lambda self: self._type )
    data = property( lambda self: self._data )
    pass

