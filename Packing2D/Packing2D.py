__author__ = 'human88998999877'
from Packing2D.PackingConveyer.Conveyer import Conveyer
from Packing2D.MappedFactory import MappedFactory

from Packing2D import PackingAlgorithm,PackingMode,PackingAlgorithmAbility,PlaceHeuristic,SortOrder,SortKey
from Packing2D.RectangleSorting.RectangleSorting import *

from Packing2D.PackingConveyer.Signal import SignalType,Signal


class Packing2DInvalidInputError(BaseException):
    pass

class Packing2D(object):
    def __init__(self):
        super(Packing2D, self).__init__()
        self.conveyer = None

        self.factory = MappedFactory()
        self._initObjectFactory(self.factory)
        pass

    def _initObjectFactory(self, factory):
        pass

    def createInstance(self, name):
        instance = self.factory.createInstance(name, cached = True)
        return instance
        pass

    def initialise(self, settings):
        self.conveyer = Conveyer()
        builder = self.createInstance(settings.packingMode)
        builder.build(self.conveyer, self.factory, settings)
        pass

    def push(self, input):
        _input = input
        if isinstance(input, list) is False:
            _input = [input]
            pass

        signal = Signal(SignalType.PUSH_INPUT, _input)
        self.conveyer.processSignal(signal)
        pass
    pass
pass