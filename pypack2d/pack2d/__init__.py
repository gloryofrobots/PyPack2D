from pypack2d.pack2d import settings


# Initialise factory.
# This fat big factory is created for minimising of if elif statements in places where program choose object type for user option
# So we just have a dictionary with {typeName:class}. It`s bad style in memory usage aspect but it simplifies code

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


packingFactory = Factory()

from pypack2d.pack2d.conveyer.builder.online import PackingConveyerBuilderOnline
from pypack2d.pack2d.conveyer.builder.offline import PackingConveyerBuilderOffline
from pypack2d.pack2d.conveyer.builder.local_search import PackingConveyerBuilderLocalSearch

packingFactory.register(settings.PackingMode.ONLINE, PackingConveyerBuilderOnline)
packingFactory.register(settings.PackingMode.OFFLINE, PackingConveyerBuilderOffline)
packingFactory.register(settings.PackingMode.LOCAL_SEARCH, PackingConveyerBuilderLocalSearch)

###################################################################################

from pypack2d.pack2d.packer.guillotine import guillotine
from pypack2d.pack2d.packer.cell import cell
from pypack2d.pack2d.packer.shelf import shelf
from pypack2d.pack2d.packer.max_rectangles.max_rectangles import BinPackerMaxRectangles

packingFactory.register(settings.PackingAlgorithm.GUILLOTINE, guillotine)
packingFactory.register(settings.PackingAlgorithm.CELL, cell)
packingFactory.register(settings.PackingAlgorithm.SHELF, shelf)
packingFactory.register(settings.PackingAlgorithm.MAX_RECTANGLES, BinPackerMaxRectangles)

###################################################################################

from pypack2d.pack2d.conveyer.rotator import RotatorSideWays, RotatorUpRight

packingFactory.register(settings.RotateMode.SIDE_WAYS, RotatorSideWays)
packingFactory.register(settings.RotateMode.UP_RIGHT, RotatorUpRight)

###################################################################################

from pypack2d.pack2d.conveyer.size_shifter.size_shifter_pow2 import BinSizeShifterPow2
from pypack2d.pack2d.conveyer.size_shifter.size_shifter_maximal import BinSizeShifterMaximal
from pypack2d.pack2d.conveyer.size_shifter.size_shifter_pow2_minimize_last import BinSizeShifterPow2MinimizeLast

packingFactory.register(settings.BinSizeMode.MINIMIZE_MAXIMAL, BinSizeShifterMaximal)
packingFactory.register(settings.BinSizeMode.MINIMIZE_POW2, BinSizeShifterPow2)
packingFactory.register(settings.BinSizeMode.MINIMIZE_POW2_MINIMIZE_LAST, BinSizeShifterPow2MinimizeLast)

###################################################################################

from pypack2d.pack2d.packer.rectangle_sorting import RectangleSortingArea, RectangleSortingLongerSide \
    , RectangleSortingPerimeter, RectangleSortingShorterSide \
    , RectangleSortingSideLengthDifference, RectangleSortingSideRatio \
    , RectangleSortingWidth, RectangleSortingHeight

###################################################################################

packingFactory.register(settings.SortKey.AREA, RectangleSortingArea)
packingFactory.register(settings.SortKey.WIDTH, RectangleSortingWidth)
packingFactory.register(settings.SortKey.HEIGHT, RectangleSortingHeight)
packingFactory.register(settings.SortKey.SHORTER_SIDE, RectangleSortingShorterSide)
packingFactory.register(settings.SortKey.LONGER_SIDE, RectangleSortingLongerSide)
packingFactory.register(settings.SortKey.PERIMETER, RectangleSortingPerimeter)
packingFactory.register(settings.SortKey.SIDE_LENGTH_DIFFERENCE, RectangleSortingSideLengthDifference)
packingFactory.register(settings.SortKey.SIDE_RATIO, RectangleSortingSideRatio)

from pypack2d.pack2d.packer.place_heuristic import PlaceHeuristicBestAreaFit, \
    PlaceHeuristicBestLongSideFit \
    , PlaceHeuristicBestShortSideFit, PlaceHeuristicWorstAreaFit \
    , PlaceHeuristicWorstLongSideFit, PlaceHeuristicWorstWidthFit \
    , PlaceHeuristicWorstShortSideFit, PlaceHeuristicBestHeightFit \
    , PlaceHeuristicBestWidthFit, PlaceHeuristicBottomLeft \
    , PlaceHeuristicFirstFit, PlaceHeuristicWorstHeightFit

###################################################################################

packingFactory.register(settings.PlaceHeuristic.WORST_AREA_FIT, PlaceHeuristicWorstAreaFit)
packingFactory.register(settings.PlaceHeuristic.BEST_AREA_FIT, PlaceHeuristicBestAreaFit)

packingFactory.register(settings.PlaceHeuristic.BEST_LONG_SIDE_FIT, PlaceHeuristicBestLongSideFit)
packingFactory.register(settings.PlaceHeuristic.WORST_LONG_SIDE_FIT, PlaceHeuristicWorstLongSideFit)

packingFactory.register(settings.PlaceHeuristic.WORST_WIDTH_FIT, PlaceHeuristicWorstWidthFit)
packingFactory.register(settings.PlaceHeuristic.BEST_WIDTH_FIT, PlaceHeuristicBestWidthFit)

packingFactory.register(settings.PlaceHeuristic.BEST_SHORT_SIDE_FIT, PlaceHeuristicBestShortSideFit)
packingFactory.register(settings.PlaceHeuristic.WORST_SHORT_SIDE_FIT, PlaceHeuristicWorstShortSideFit)

packingFactory.register(settings.PlaceHeuristic.BEST_HEIGHT_FIT, PlaceHeuristicBestHeightFit)
packingFactory.register(settings.PlaceHeuristic.WORST_HEIGHT_FIT, PlaceHeuristicWorstHeightFit)

packingFactory.register(settings.PlaceHeuristic.FIRST_FIT, PlaceHeuristicFirstFit)

packingFactory.register(settings.PlaceHeuristic.BOTTOM_LEFT, PlaceHeuristicBottomLeft)

###################################################################################

from pypack2d.pack2d.packer.guillotine.splitter import SplitterHorizontal, SplitterLongerAxis \
    , SplitterLongerLeftOverAxis, SplitterMaxArea, SplitterShorterAxis \
    , SplitterShorterLeftOverAxis, SplitterMinArea, SplitterVertical

packingFactory.register(settings.GuillotineSplitRule.SHORTER_AXIS, SplitterShorterAxis)
packingFactory.register(settings.GuillotineSplitRule.SHORTER_LEFTOVER_AXIS, SplitterShorterLeftOverAxis)
packingFactory.register(settings.GuillotineSplitRule.LONGER_AXIS, SplitterLongerAxis)
packingFactory.register(settings.GuillotineSplitRule.LONGER_LEFTOVER_AXIS, SplitterLongerLeftOverAxis)
packingFactory.register(settings.GuillotineSplitRule.HORIZONTAL, SplitterHorizontal)
packingFactory.register(settings.GuillotineSplitRule.VERTICAL, SplitterVertical)
packingFactory.register(settings.GuillotineSplitRule.MAX_AREA, SplitterMaxArea)
packingFactory.register(settings.GuillotineSplitRule.MIN_AREA, SplitterMinArea)
