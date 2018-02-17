from pypack2d.pack import settings


class FactoryError(BaseException):
    pass


class Factory(object):
    def __init__(self):
        super(Factory, self).__init__()
        self._types = {}

    def register(self, name, class_type):
        if self.has_type(name):
            raise FactoryError("TypeName already register %s" % name)

        self._types[name] = class_type

    def has_type(self, name):
        if name not in self._types:
            return False

        return True

    def __create_instance(self, name):
        ctor = self._types[name]
        instance = ctor()
        return instance

    def create_instance(self, name):
        if self.has_type(name) is False:
            raise FactoryError("TypeName not register %s" % name)

        instance = self.__create_instance(name)
        return instance


# Factories used instead of long if-elif chain

class Factories:
    conveyer_builder = Factory()
    packer = Factory()
    rotator = Factory()
    size_shifter = Factory()
    sorting = Factory()
    heuristic = Factory()
    splitter = Factory()

    def __init__(self):
        raise TypeError("This is static class")


from pypack2d.pack.conveyer.builder.online import PackingConveyerBuilderOnline
from pypack2d.pack.conveyer.builder.offline import PackingConveyerBuilderOffline
from pypack2d.pack.conveyer.builder.local_search import PackingConveyerBuilderLocalSearch

Factories.conveyer_builder.register(settings.PackingMode.ONLINE, PackingConveyerBuilderOnline)
Factories.conveyer_builder.register(settings.PackingMode.OFFLINE, PackingConveyerBuilderOffline)
Factories.conveyer_builder.register(settings.PackingMode.LOCAL_SEARCH, PackingConveyerBuilderLocalSearch)

###################################################################################

from pypack2d.pack.packer.guillotine import guillotine
from pypack2d.pack.packer.cell import cell
from pypack2d.pack.packer.shelf import shelf
from pypack2d.pack.packer.max_rectangles.max_rectangles import BinPackerMaxRectangles

Factories.packer.register(settings.PackingAlgorithm.GUILLOTINE, guillotine)
Factories.packer.register(settings.PackingAlgorithm.CELL, cell)
Factories.packer.register(settings.PackingAlgorithm.SHELF, shelf)
Factories.packer.register(settings.PackingAlgorithm.MAX_RECTANGLES, BinPackerMaxRectangles)

###################################################################################

from pypack2d.pack.conveyer.rotator import RotatorSideWays, RotatorUpRight

Factories.rotator.register(settings.RotateMode.SIDE_WAYS, RotatorSideWays)
Factories.rotator.register(settings.RotateMode.UP_RIGHT, RotatorUpRight)

###################################################################################

from pypack2d.pack.conveyer.size_shifter.size_shifter_pow2 import BinSizeShifterPow2
from pypack2d.pack.conveyer.size_shifter.size_shifter_maximal import BinSizeShifterMaximal
from pypack2d.pack.conveyer.size_shifter.size_shifter_pow2_minimize_last import BinSizeShifterPow2MinimizeLast

Factories.size_shifter.register(settings.ResizeMode.MINIMIZE_MAXIMAL, BinSizeShifterMaximal)
Factories.size_shifter.register(settings.ResizeMode.MINIMIZE_POW2, BinSizeShifterPow2)
Factories.size_shifter.register(settings.ResizeMode.MINIMIZE_POW2_MINIMIZE_LAST, BinSizeShifterPow2MinimizeLast)

###################################################################################

from pypack2d.pack.packer.rectangle_sorting import (RectangleSortingArea, RectangleSortingLongerSide,
                                                      RectangleSortingPerimeter, RectangleSortingShorterSide,
                                                      RectangleSortingSideLengthDifference, RectangleSortingSideRatio,
                                                      RectangleSortingWidth, RectangleSortingHeight)

###################################################################################

Factories.sorting.register(settings.SortKey.AREA, RectangleSortingArea)
Factories.sorting.register(settings.SortKey.WIDTH, RectangleSortingWidth)
Factories.sorting.register(settings.SortKey.HEIGHT, RectangleSortingHeight)
Factories.sorting.register(settings.SortKey.SHORTER_SIDE, RectangleSortingShorterSide)
Factories.sorting.register(settings.SortKey.LONGER_SIDE, RectangleSortingLongerSide)
Factories.sorting.register(settings.SortKey.PERIMETER, RectangleSortingPerimeter)
Factories.sorting.register(settings.SortKey.SIDE_LENGTH_DIFFERENCE, RectangleSortingSideLengthDifference)
Factories.sorting.register(settings.SortKey.SIDE_RATIO, RectangleSortingSideRatio)

from pypack2d.pack.packer.place_heuristic import (
    PlaceHeuristicBestAreaFit, PlaceHeuristicBestLongSideFit, PlaceHeuristicBestShortSideFit,
    PlaceHeuristicWorstAreaFit, PlaceHeuristicWorstLongSideFit, PlaceHeuristicWorstWidthFit,
    PlaceHeuristicWorstShortSideFit, PlaceHeuristicBestHeightFit, PlaceHeuristicBestWidthFit, PlaceHeuristicBottomLeft,
    PlaceHeuristicFirstFit, PlaceHeuristicWorstHeightFit)
###################################################################################

Factories.heuristic.register(settings.PlaceHeuristic.WORST_AREA_FIT, PlaceHeuristicWorstAreaFit)
Factories.heuristic.register(settings.PlaceHeuristic.BEST_AREA_FIT, PlaceHeuristicBestAreaFit)

Factories.heuristic.register(settings.PlaceHeuristic.BEST_LONG_SIDE_FIT, PlaceHeuristicBestLongSideFit)
Factories.heuristic.register(settings.PlaceHeuristic.WORST_LONG_SIDE_FIT, PlaceHeuristicWorstLongSideFit)

Factories.heuristic.register(settings.PlaceHeuristic.WORST_WIDTH_FIT, PlaceHeuristicWorstWidthFit)
Factories.heuristic.register(settings.PlaceHeuristic.BEST_WIDTH_FIT, PlaceHeuristicBestWidthFit)

Factories.heuristic.register(settings.PlaceHeuristic.BEST_SHORT_SIDE_FIT, PlaceHeuristicBestShortSideFit)
Factories.heuristic.register(settings.PlaceHeuristic.WORST_SHORT_SIDE_FIT, PlaceHeuristicWorstShortSideFit)

Factories.heuristic.register(settings.PlaceHeuristic.BEST_HEIGHT_FIT, PlaceHeuristicBestHeightFit)
Factories.heuristic.register(settings.PlaceHeuristic.WORST_HEIGHT_FIT, PlaceHeuristicWorstHeightFit)

Factories.heuristic.register(settings.PlaceHeuristic.FIRST_FIT, PlaceHeuristicFirstFit)

Factories.heuristic.register(settings.PlaceHeuristic.BOTTOM_LEFT, PlaceHeuristicBottomLeft)

###################################################################################

from pypack2d.pack.packer.guillotine.splitter import (SplitterHorizontal, SplitterLongerAxis,
                                                        SplitterLongerLeftOverAxis, SplitterMaxArea,
                                                        SplitterShorterAxis,
                                                        SplitterShorterLeftOverAxis, SplitterMinArea, SplitterVertical)

Factories.splitter.register(settings.GuillotineSplitRule.SHORTER_AXIS, SplitterShorterAxis)
Factories.splitter.register(settings.GuillotineSplitRule.SHORTER_LEFTOVER_AXIS, SplitterShorterLeftOverAxis)
Factories.splitter.register(settings.GuillotineSplitRule.LONGER_AXIS, SplitterLongerAxis)
Factories.splitter.register(settings.GuillotineSplitRule.LONGER_LEFTOVER_AXIS, SplitterLongerLeftOverAxis)
Factories.splitter.register(settings.GuillotineSplitRule.HORIZONTAL, SplitterHorizontal)
Factories.splitter.register(settings.GuillotineSplitRule.VERTICAL, SplitterVertical)
Factories.splitter.register(settings.GuillotineSplitRule.MAX_AREA, SplitterMaxArea)
Factories.splitter.register(settings.GuillotineSplitRule.MIN_AREA, SplitterMinArea)
