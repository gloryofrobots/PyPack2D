__author__ = 'human88998999877'
from Packing2D.PackingConveyer.Conveyer import Conveyer
from Packing2D.MappedFactory import MappedFactory

from Packing2D import GuillotineSplitRule, BinSizeMode, BorderMode,\
    PackingAlgorithm, PackingAlgorithmAbility, PackingMode,PlaceHeuristic,SortKey, SortOrder, RotateMode

from Packing2D.PackingConveyer.Signal import SignalType,Signal

class Packing2D(object):
    def __init__(self):
        super(Packing2D, self).__init__()
        self.conveyer = None

        self.factory = MappedFactory()
        self._initObjectFactory(self.factory)
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

    def _initObjectFactory(self, factory):
        from Packing2D.PackingConveyerBuilder.PackingConveyerBuilderOnline import PackingConveyerBuilderOnline
        from Packing2D.PackingConveyerBuilder.PackingConveyerBuilderOffline import PackingConveyerBuilderOffline
        from Packing2D.PackingConveyerBuilder.PackingConveyerBuilderLocalSearch import PackingConveyerBuilderLocalSearch

        factory.register(PackingMode.ONLINE, PackingConveyerBuilderOnline)
        factory.register(PackingMode.OFFLINE, PackingConveyerBuilderOffline)
        factory.register(PackingMode.LOCAL_SEARCH, PackingConveyerBuilderLocalSearch)

        ###################################################################################

        from Packing2D.BinPackerGuillotine.BinPackerGuillotine import BinPackerGuillotine
        from Packing2D.BinPackerCell.BinPackerCell import BinPackerCell
        from Packing2D.BinPackerShelf.BinPackerShelf import BinPackerShelf
        from Packing2D.BinPackerMaxRectangles.BinPackerMaxRectangles import BinPackerMaxRectangles

        factory.register(PackingAlgorithm.GUILLOTINE, BinPackerGuillotine)
        factory.register(PackingAlgorithm.CELL, BinPackerCell)
        factory.register(PackingAlgorithm.SHELF, BinPackerShelf)
        factory.register(PackingAlgorithm.MAX_RECTANGLES, BinPackerMaxRectangles)

        ###################################################################################

        from Packing2D.PackingConveyer.Rotator import RotatorSideWays,RotatorUpRight
        factory.register(RotateMode.SIDE_WAYS, RotatorSideWays)
        factory.register(RotateMode.UP_RIGHT, RotatorUpRight)
        
        ###################################################################################

        from Packing2D.PackingConveyer.BinSizeShifter.BinSizeShifterPow2 import BinSizeShifterPow2
        from Packing2D.PackingConveyer.BinSizeShifter.BinSizeShifterMaximal import BinSizeShifterMaximal

        factory.register(BinSizeMode.MINIMIZE_MAXIMAL, BinSizeShifterMaximal)
        factory.register(BinSizeMode.MINIMIZE_POW2, BinSizeShifterPow2)

        ###################################################################################

        from Packing2D.BinPacker.RectangleSorting.RectangleSorting import RectangleSortingArea, RectangleSortingLongerSide\
                                                                , RectangleSortingPerimeter, RectangleSortingShorterSide\
                                                                , RectangleSortingSideLengthDifference, RectangleSortingSideRatio\
                                                                , RectangleSortingWidth ,RectangleSortingHeight

        ###################################################################################

        factory.register(SortKey.AREA, RectangleSortingArea)
        factory.register(SortKey.WIDTH, RectangleSortingWidth)
        factory.register(SortKey.HEIGHT, RectangleSortingHeight)
        factory.register(SortKey.SHORTER_SIDE, RectangleSortingShorterSide)
        factory.register(SortKey.LONGER_SIDE, RectangleSortingLongerSide)
        factory.register(SortKey.PERIMETER, RectangleSortingPerimeter)
        factory.register(SortKey.SIDE_LENGTH_DIFFERENCE, RectangleSortingSideLengthDifference)
        factory.register(SortKey.SIDE_RATIO, RectangleSortingSideRatio)


        from Packing2D.BinPacker.PlaceChooseHeuristic.PlaceChooseHeuristic  import PlaceHeuristicBestAreaFit,PlaceHeuristicBestLongSideFit\
                                                            ,PlaceHeuristicBestShortSideFit ,PlaceHeuristicWorstAreaFit\
                                                            ,PlaceHeuristicWorstLongSideFit,PlaceHeuristicWorstWidthFit\
                                                            ,PlaceHeuristicWorstShortSideFit,PlaceHeuristicBestHeightFit\
                                                            ,PlaceHeuristicBestWidthFit,PlaceHeuristicBottomLeft\
                                                            ,PlaceHeuristicFirstFit, PlaceHeuristicWorstHeightFit

        ###################################################################################

        factory.register(PlaceHeuristic.WORST_AREA_FIT, PlaceHeuristicWorstAreaFit)
        factory.register(PlaceHeuristic.BEST_AREA_FIT, PlaceHeuristicBestAreaFit)

        factory.register(PlaceHeuristic.BEST_LONG_SIDE_FIT, PlaceHeuristicBestLongSideFit)
        factory.register(PlaceHeuristic.WORST_LONG_SIDE_FIT, PlaceHeuristicWorstLongSideFit)

        factory.register(PlaceHeuristic.WORST_WIDTH_FIT, PlaceHeuristicWorstWidthFit)
        factory.register(PlaceHeuristic.BEST_WIDTH_FIT, PlaceHeuristicBestWidthFit)

        factory.register(PlaceHeuristic.BEST_SHORT_SIDE_FIT, PlaceHeuristicBestShortSideFit)
        factory.register(PlaceHeuristic.WORST_SHORT_SIDE_FIT, PlaceHeuristicWorstShortSideFit)

        factory.register(PlaceHeuristic.BEST_HEIGHT_FIT, PlaceHeuristicBestHeightFit)
        factory.register(PlaceHeuristic.WORST_HEIGHT_FIT, PlaceHeuristicWorstHeightFit)

        factory.register(PlaceHeuristic.FIRST_FIT, PlaceHeuristicFirstFit)

        factory.register(PlaceHeuristic.BOTTOM_LEFT, PlaceHeuristicBottomLeft)
        pass
    pass