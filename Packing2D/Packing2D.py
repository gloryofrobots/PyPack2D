__author__ = 'human88998999877'
from Packing2D.PackingConveyer.Conveyer import Conveyer
from Packing2D.MappedFactory import MappedFactory

from Packing2D import PackingAlgorithm,PackingMode,PackingAlgorithmAbility,PlaceHeuristic,SortOrder,SortKey
from Packing2D.RectangleSorting.RectangleSorting import *

from Packing2D import GuillotineSplitRule,BinSizeMode,BorderMode,\
    PackingAlgorithm,PackingAlgorithmAbility,PackingMode,PlaceHeuristic,SortKey,SortOrder

"""

SortOrder = Enum("ASC", "DESC")

SortKey = Enum("AREA"
               ,"WIDTH"
               ,"HEIGHT"
               ,"SHORTER_SIDE"
               ,"LONGER_SIDE"
               ,"PERIMETER"
               ,"SIDE_LENGTH_DIFFERENCE"
               ,"SIDE_RATIO")

PackingMode = Enum("ONLINE", "OFFLINE", "LOCAL_SEARCH")

PackingAlgorithm = Enum("SHELF", "SKYLINE", "GUILLOTINE")

PlaceHeuristic = Enum(  "NEXT_FIT"
                      , "BEST_WIDTH_FIT"
                      , "BEST_HEIGHT_FIT"
                      , "WORST_WIDTH_FIT"
                      , "WORST_HEIGHT_FIT"
                      , "BEST_AREA_FIT"
                      , "BEST_SHORT_SIDE_FIT"
                      , "BEST_LONG_SIDE_FIT"
                      , "WORST_AREA_FIT"
                      , "WORST_SHORT_SIDE_FIT"
                      , "WORST_LONG_SIDE_FIT"
                      , "BOTTOM_LEFT"
                      , "BEST_FIT")

BinSizeMode = Enum("STRICT","MINIMIZE_MAXIMAL", "MINIMIZE_POW2")

PackingAlgorithmAbility = Enum("RECTANGLE_MERGE", "WASTE_MAP", "FLOOR_CEILING")

GuillotineSplitRule = Enum("SHORTER_AXIS"
                           , "LONGER_AXIS"
                           , "SHORTER_LEFTOVER_AXIS"
                           , "LONGER_LEFTOVER_AXIS"
                           , "MAX_AREA"
                           , "MIN_AREA"
                           , "HORIZONTAL")

BorderMode = Enum("NONE","STRICT","AUTO")


"""



from Packing2D.PackingConveyer.Signal import SignalType,Signal

class Packing2D(object):
    def __init__(self):
        super(Packing2D, self).__init__()
        self.conveyer = None

        self.factory = MappedFactory()
        self._initObjectFactory(self.factory)
        pass

    def _initObjectFactory(self, factory):
        from Packing2D.PackingConveyerBuilder.PackingConveyerBuilderOnline import PackingConveyerBuilderOnline
        from Packing2D.PackingConveyerBuilder.PackingConveyerBuilderOffline import PackingConveyerBuilderOffline
        from Packing2D.PackingConveyerBuilder.PackingConveyerBuilderLocalSearch import PackingConveyerBuilderLocalSearch
        factory.register(PackingMode.ONLINE, PackingConveyerBuilderOnline)
        factory.register(PackingMode.OFFLINE, PackingConveyerBuilderOffline)
        factory.register(PackingMode.LOCAL_SEARCH, PackingConveyerBuilderLocalSearch)

        from Packing2D.BinPackerGuillotine.BinPackerGuillotine import BinPackerGuillotine
        factory.register(PackingAlgorithm.GUILLOTINE, BinPackerGuillotine)

        from Packing2D.PackingConveyer.BinSizeShifter.BinSizeShifterPow2 import BinSizeShifterPow2
        from Packing2D.PackingConveyer.BinSizeShifter.BinSizeShifterMaximal import BinSizeShifterMaximal
        factory.register(BinSizeMode.MINIMIZE_MAXIMAL, BinSizeShifterMaximal)
        factory.register(BinSizeMode.MINIMIZE_POW2, BinSizeShifterPow2)

        from Packing2D.RectangleSorting.RectangleSorting import RectangleSortingArea, RectangleSortingLongerSide\
                                                                , RectangleSortingPerimeter, RectangleSortingShorterSide\
                                                                , RectangleSortingSideLengthDifference, RectangleSortingSideRatio\
                                                                , RectangleSortingWidth ,RectangleSortingHeight

        factory.register(SortKey.AREA, RectangleSortingArea)
        factory.register(SortKey.WIDTH, RectangleSortingWidth)
        factory.register(SortKey.HEIGHT, RectangleSortingHeight)
        factory.register(SortKey.SHORTER_SIDE, RectangleSortingShorterSide)
        factory.register(SortKey.LONGER_SIDE, RectangleSortingLongerSide)
        factory.register(SortKey.PERIMETER, RectangleSortingPerimeter)
        factory.register(SortKey.SIDE_LENGTH_DIFFERENCE, RectangleSortingSideLengthDifference)
        factory.register(SortKey.SIDE_RATIO, RectangleSortingSideRatio)
        pass

    def initialise(self, settings):
        self.conveyer = Conveyer()
        builder = self.factory.getInstance(settings.packingMode)
        builder.build(self.conveyer, self.factory, settings)
        signal = Signal(SignalType.PREPARE_TO_PACK, None)
        self.conveyer.processSignal(signal)
        pass

    def pack(self):
        signal = Signal(SignalType.START_PACK, None)
        self.conveyer.processSignal(signal)
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
        self.conveyer.processSignal(signal)
        pass
    pass
pass