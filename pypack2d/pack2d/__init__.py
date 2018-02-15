from enum import Enum


class SortOrder(Enum):
    ASC = "ASC"
    DESC = "DESC"


class SortKey(Enum):
    AREA = "AREA"
    WIDTH = "WIDTH"
    HEIGHT = "HEIGHT"
    SHORTER_SIDE = "SHORTER_SIDE"
    LONGER_SIDE = "LONGER_SIDE"
    PERIMETER = "PERIMETER"
    SIDE_LENGTH_DIFFERENCE = "SIDE_LENGTH_DIFFERENCE"
    SIDE_RATIO = "SIDE_RATIO"


class PackingMode(Enum):
    ONLINE = "ONLINE"
    OFFLINE = "OFFLINE"
    LOCAL_SEARCH = "LOCAL_SEARCH"


class PackingAlgorithm(Enum):
    SHELF = "SHELF"
    CELL = "CELL"
    GUILLOTINE = "GUILLOTINE"
    MAX_RECTANGLES = "MAX_RECTANGLES"


class PlaceHeuristic(Enum):
    FIRST_FIT = "FIRST_FIT"
    BEST_WIDTH_FIT = "BEST_WIDTH_FIT"
    BEST_HEIGHT_FIT = "BEST_HEIGHT_FIT"
    WORST_WIDTH_FIT = "WORST_WIDTH_FIT"
    WORST_HEIGHT_FIT = "WORST_HEIGHT_FIT"
    BEST_AREA_FIT = "BEST_AREA_FIT"
    BEST_SHORT_SIDE_FIT = "BEST_SHORT_SIDE_FIT"
    BEST_LONG_SIDE_FIT = "BEST_LONG_SIDE_FIT"
    WORST_AREA_FIT = "WORST_AREA_FIT"
    WORST_SHORT_SIDE_FIT = "WORST_SHORT_SIDE_FIT"
    WORST_LONG_SIDE_FIT = "WORST_LONG_SIDE_FIT"
    BOTTOM_LEFT = "BOTTOM_LEFT"
    BEST_FIT = "BEST_FIT"


class BinSizeMode(Enum):
    STRICT = "STRICT"
    MINIMIZE_MAXIMAL = "MINIMIZE_MAXIMAL"
    MINIMIZE_POW2 = "MINIMIZE_POW2"
    MINIMIZE_POW2_MINIMIZE_LAST = "MINIMIZE_POW2_MINIMIZE_LAST"


class PackingAlgorithmAbility(Enum):
    RECTANGLE_MERGE = "RECTANGLE_MERGE"
    WASTE_MAP = "WASTE_MAP"
    FLOOR_CEILING = "FLOOR_CEILING"


class GuillotineSplitRule(Enum):
    SHORTER_AXIS = "SHORTER_AXIS"
    LONGER_AXIS = "LONGER_AXIS"
    SHORTER_LEFTOVER_AXIS = "SHORTER_LEFTOVER_AXIS"
    LONGER_LEFTOVER_AXIS = "LONGER_LEFTOVER_AXIS"
    MAX_AREA = "MAX_AREA"
    MIN_AREA = "MIN_AREA"
    HORIZONTAL = "HORIZONTAL"
    VERTICAL = "VERTICAL"


class BorderMode(Enum):
    NONE = "NONE"
    STRICT = "STRICT"
    AUTO = "AUTO"


class BorderType(Enum):
    PIXELS_FROM_EDGE = "PIXELS_FROM_EDGE"
    SOLID = "SOLID"


class RotateMode(Enum):
    NONE = "NONE"
    UP_RIGHT = "UP_RIGHT"
    SIDE_WAYS = "SIDE_WAYS"
    AUTO = "AUTO"


# Initialise factory.
# This fat big factory is created for minimising of if elif statements in places where program choose object type for user option
# So we just have a dictionary with {typeName:class}. It`s bad style in memory usage aspect but it simplifies code

from pypack2d.pack2d.MappedFactory import MappedFactory

packingFactory = MappedFactory()

from pypack2d.pack2d.PackingConveyerBuilder.PackingConveyerBuilderOnline import PackingConveyerBuilderOnline
from pypack2d.pack2d.PackingConveyerBuilder.PackingConveyerBuilderOffline import PackingConveyerBuilderOffline
from pypack2d.pack2d.PackingConveyerBuilder.PackingConveyerBuilderLocalSearch import PackingConveyerBuilderLocalSearch

packingFactory.register(PackingMode.ONLINE, PackingConveyerBuilderOnline)
packingFactory.register(PackingMode.OFFLINE, PackingConveyerBuilderOffline)
packingFactory.register(PackingMode.LOCAL_SEARCH, PackingConveyerBuilderLocalSearch)

###################################################################################

from pypack2d.pack2d.packer.guillotine import guillotine
from pypack2d.pack2d.packer.cell import cell
from pypack2d.pack2d.packer.shelf import shelf
from pypack2d.pack2d.packer.max_rectangles.max_rectangles import BinPackerMaxRectangles

packingFactory.register(PackingAlgorithm.GUILLOTINE, guillotine)
packingFactory.register(PackingAlgorithm.CELL, cell)
packingFactory.register(PackingAlgorithm.SHELF, shelf)
packingFactory.register(PackingAlgorithm.MAX_RECTANGLES, BinPackerMaxRectangles)

###################################################################################

from pypack2d.pack2d.PackingConveyer.Rotator import RotatorSideWays, RotatorUpRight

packingFactory.register(RotateMode.SIDE_WAYS, RotatorSideWays)
packingFactory.register(RotateMode.UP_RIGHT, RotatorUpRight)

###################################################################################

from pypack2d.pack2d.PackingConveyer.BinSizeShifter.BinSizeShifterPow2 import BinSizeShifterPow2
from pypack2d.pack2d.PackingConveyer.BinSizeShifter.BinSizeShifterMaximal import BinSizeShifterMaximal
from pypack2d.pack2d.PackingConveyer.BinSizeShifter.BinSizeShifterPow2MinimizeLast import BinSizeShifterPow2MinimizeLast

packingFactory.register(BinSizeMode.MINIMIZE_MAXIMAL, BinSizeShifterMaximal)
packingFactory.register(BinSizeMode.MINIMIZE_POW2, BinSizeShifterPow2)
packingFactory.register(BinSizeMode.MINIMIZE_POW2_MINIMIZE_LAST, BinSizeShifterPow2MinimizeLast)

###################################################################################

from pypack2d.pack2d.packer.rectangle_sorting import RectangleSortingArea, RectangleSortingLongerSide \
    , RectangleSortingPerimeter, RectangleSortingShorterSide \
    , RectangleSortingSideLengthDifference, RectangleSortingSideRatio \
    , RectangleSortingWidth, RectangleSortingHeight

###################################################################################

packingFactory.register(SortKey.AREA, RectangleSortingArea)
packingFactory.register(SortKey.WIDTH, RectangleSortingWidth)
packingFactory.register(SortKey.HEIGHT, RectangleSortingHeight)
packingFactory.register(SortKey.SHORTER_SIDE, RectangleSortingShorterSide)
packingFactory.register(SortKey.LONGER_SIDE, RectangleSortingLongerSide)
packingFactory.register(SortKey.PERIMETER, RectangleSortingPerimeter)
packingFactory.register(SortKey.SIDE_LENGTH_DIFFERENCE, RectangleSortingSideLengthDifference)
packingFactory.register(SortKey.SIDE_RATIO, RectangleSortingSideRatio)

from pypack2d.pack2d.packer.place_heuristic import PlaceHeuristicBestAreaFit, \
    PlaceHeuristicBestLongSideFit \
    , PlaceHeuristicBestShortSideFit, PlaceHeuristicWorstAreaFit \
    , PlaceHeuristicWorstLongSideFit, PlaceHeuristicWorstWidthFit \
    , PlaceHeuristicWorstShortSideFit, PlaceHeuristicBestHeightFit \
    , PlaceHeuristicBestWidthFit, PlaceHeuristicBottomLeft \
    , PlaceHeuristicFirstFit, PlaceHeuristicWorstHeightFit

###################################################################################

packingFactory.register(PlaceHeuristic.WORST_AREA_FIT, PlaceHeuristicWorstAreaFit)
packingFactory.register(PlaceHeuristic.BEST_AREA_FIT, PlaceHeuristicBestAreaFit)

packingFactory.register(PlaceHeuristic.BEST_LONG_SIDE_FIT, PlaceHeuristicBestLongSideFit)
packingFactory.register(PlaceHeuristic.WORST_LONG_SIDE_FIT, PlaceHeuristicWorstLongSideFit)

packingFactory.register(PlaceHeuristic.WORST_WIDTH_FIT, PlaceHeuristicWorstWidthFit)
packingFactory.register(PlaceHeuristic.BEST_WIDTH_FIT, PlaceHeuristicBestWidthFit)

packingFactory.register(PlaceHeuristic.BEST_SHORT_SIDE_FIT, PlaceHeuristicBestShortSideFit)
packingFactory.register(PlaceHeuristic.WORST_SHORT_SIDE_FIT, PlaceHeuristicWorstShortSideFit)

packingFactory.register(PlaceHeuristic.BEST_HEIGHT_FIT, PlaceHeuristicBestHeightFit)
packingFactory.register(PlaceHeuristic.WORST_HEIGHT_FIT, PlaceHeuristicWorstHeightFit)

packingFactory.register(PlaceHeuristic.FIRST_FIT, PlaceHeuristicFirstFit)

packingFactory.register(PlaceHeuristic.BOTTOM_LEFT, PlaceHeuristicBottomLeft)

###################################################################################

from pypack2d.pack2d.packer.guillotine.splitter import SplitterHorizontal, SplitterLongerAxis \
    , SplitterLongerLeftOverAxis, SplitterMaxArea, SplitterShorterAxis \
    , SplitterShorterLeftOverAxis, SplitterMinArea, SplitterVertical

packingFactory.register(GuillotineSplitRule.SHORTER_AXIS, SplitterShorterAxis)
packingFactory.register(GuillotineSplitRule.SHORTER_LEFTOVER_AXIS, SplitterShorterLeftOverAxis)
packingFactory.register(GuillotineSplitRule.LONGER_AXIS, SplitterLongerAxis)
packingFactory.register(GuillotineSplitRule.LONGER_LEFTOVER_AXIS, SplitterLongerLeftOverAxis)
packingFactory.register(GuillotineSplitRule.HORIZONTAL, SplitterHorizontal)
packingFactory.register(GuillotineSplitRule.VERTICAL, SplitterVertical)
packingFactory.register(GuillotineSplitRule.MAX_AREA, SplitterMaxArea)
packingFactory.register(GuillotineSplitRule.MIN_AREA, SplitterMinArea)

###################################################################################
