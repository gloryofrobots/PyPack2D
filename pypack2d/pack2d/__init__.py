from pypack2d.pack2d.Enum.Enum import Enum

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

PackingAlgorithm = Enum("SHELF", "CELL", "GUILLOTINE", "MAX_RECTANGLES")

PlaceHeuristic = Enum(  "FIRST_FIT"
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

BinSizeMode = Enum("STRICT","MINIMIZE_MAXIMAL", "MINIMIZE_POW2","MINIMIZE_POW2_MINIMIZE_LAST")

PackingAlgorithmAbility = Enum("RECTANGLE_MERGE", "WASTE_MAP", "FLOOR_CEILING")

GuillotineSplitRule = Enum("SHORTER_AXIS"
                           , "LONGER_AXIS"
                           , "SHORTER_LEFTOVER_AXIS"
                           , "LONGER_LEFTOVER_AXIS"
                           , "MAX_AREA"
                           , "MIN_AREA"
                           , "HORIZONTAL"
                           , "VERTICAL")

BorderMode = Enum("NONE","STRICT","AUTO")
BorderType = Enum("PIXELS_FROM_EDGE", "SOLID")


RotateMode = Enum("NONE", "UP_RIGHT", "SIDE_WAYS", "AUTO")

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

from pypack2d.pack2d.BinPackerGuillotine.BinPackerGuillotine import BinPackerGuillotine
from pypack2d.pack2d.BinPackerCell.BinPackerCell import BinPackerCell
from pypack2d.pack2d.BinPackerShelf.BinPackerShelf import BinPackerShelf
from pypack2d.pack2d.BinPackerMaxRectangles.BinPackerMaxRectangles import BinPackerMaxRectangles

packingFactory.register(PackingAlgorithm.GUILLOTINE, BinPackerGuillotine)
packingFactory.register(PackingAlgorithm.CELL, BinPackerCell)
packingFactory.register(PackingAlgorithm.SHELF, BinPackerShelf)
packingFactory.register(PackingAlgorithm.MAX_RECTANGLES, BinPackerMaxRectangles)

###################################################################################

from pypack2d.pack2d.PackingConveyer.Rotator import RotatorSideWays,RotatorUpRight
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

from pypack2d.pack2d.BinPacker.RectangleSorting.RectangleSorting import RectangleSortingArea, RectangleSortingLongerSide\
                                                        , RectangleSortingPerimeter, RectangleSortingShorterSide\
                                                        , RectangleSortingSideLengthDifference, RectangleSortingSideRatio\
                                                        , RectangleSortingWidth ,RectangleSortingHeight

###################################################################################

packingFactory.register(SortKey.AREA, RectangleSortingArea)
packingFactory.register(SortKey.WIDTH, RectangleSortingWidth)
packingFactory.register(SortKey.HEIGHT, RectangleSortingHeight)
packingFactory.register(SortKey.SHORTER_SIDE, RectangleSortingShorterSide)
packingFactory.register(SortKey.LONGER_SIDE, RectangleSortingLongerSide)
packingFactory.register(SortKey.PERIMETER, RectangleSortingPerimeter)
packingFactory.register(SortKey.SIDE_LENGTH_DIFFERENCE, RectangleSortingSideLengthDifference)
packingFactory.register(SortKey.SIDE_RATIO, RectangleSortingSideRatio)


from pypack2d.pack2d.BinPacker.PlaceChooseHeuristic.PlaceChooseHeuristic  import PlaceHeuristicBestAreaFit,PlaceHeuristicBestLongSideFit\
                                                    ,PlaceHeuristicBestShortSideFit ,PlaceHeuristicWorstAreaFit\
                                                    ,PlaceHeuristicWorstLongSideFit,PlaceHeuristicWorstWidthFit\
                                                    ,PlaceHeuristicWorstShortSideFit,PlaceHeuristicBestHeightFit\
                                                    ,PlaceHeuristicBestWidthFit,PlaceHeuristicBottomLeft\
                                                    ,PlaceHeuristicFirstFit, PlaceHeuristicWorstHeightFit

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

from pypack2d.pack2d.BinPackerGuillotine.Splitter import SplitterHorizontal,SplitterLongerAxis \
                                                    ,SplitterLongerLeftOverAxis,SplitterMaxArea, SplitterShorterAxis\
                                                    ,SplitterShorterLeftOverAxis, SplitterMinArea,SplitterVertical

packingFactory.register(GuillotineSplitRule.SHORTER_AXIS, SplitterShorterAxis)
packingFactory.register(GuillotineSplitRule.SHORTER_LEFTOVER_AXIS, SplitterShorterLeftOverAxis)
packingFactory.register(GuillotineSplitRule.LONGER_AXIS, SplitterLongerAxis)
packingFactory.register(GuillotineSplitRule.LONGER_LEFTOVER_AXIS, SplitterLongerLeftOverAxis)
packingFactory.register(GuillotineSplitRule.HORIZONTAL, SplitterHorizontal)
packingFactory.register(GuillotineSplitRule.VERTICAL, SplitterVertical)
packingFactory.register(GuillotineSplitRule.MAX_AREA, SplitterMaxArea)
packingFactory.register(GuillotineSplitRule.MIN_AREA, SplitterMinArea)

###################################################################################