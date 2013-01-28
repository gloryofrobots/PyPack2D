__author__ = 'human88998999877'

from Packing2D.BinPacker.BinPacker import BinPacker,BinPackerValidateSettingsError
from Packing2D import PlaceHeuristic,GuillotineSplitRule


from Packing2D.BinPackerGuillotine.Splitter import SplitterHorizontal,SplitterLongerAxis \
                                                    ,SplitterLongerLeftOverAxis,SplitterMaxArea, SplitterShorterAxis\
                                                    ,SplitterShorterLeftOverAxis, SplitterMinArea,SplitterVertical


from Packing2D.BinPackerGuillotine.PlaceHeuristic import PlaceHeuristicBestAreaFit,PlaceHeuristicBestLongSideFit\
                                                            ,PlaceHeuristicBestShortSideFit,PlaceHeuristicNextFit\
                                                            ,PlaceHeuristicWorstAreaFit,PlaceHeuristicWorstLongSideFit\
                                                            ,PlaceHeuristicWorstShortSideFit

from Packing2D.BinPackerGuillotine.PackNode import PackNode
class BinPackerGuillotine(BinPacker):
    def _onInitialise(self, factory, settings):
        self.splitter = None
        self._initSplitter(settings)

        self.heuristic = None
        self._initHeuristic(settings)

        self.packNode =  PackNode(0, 0, settings.maxWidth,  settings.maxHeight)
        pass
    
    def _onPackBin(self, bin):
        leaf = self.packNode.insert( bin, self.splitter, self.heuristic )
        if leaf == None:
            return False
            pass

        bin.setCoord(leaf.left, leaf.top)
        return True
        pass

    def _onFlush(self):
        self.packNode =  PackNode(0, 0, self.settings.maxWidth,  self.settings.maxHeight)
        pass

    def _initHeuristic(self, settings):
        if settings.placeHeuristic == PlaceHeuristic.NEXT_FIT:
            self.heuristic = PlaceHeuristicNextFit()
            pass
        elif settings.placeHeuristic == PlaceHeuristic.BEST_AREA_FIT:
            self.heuristic = PlaceHeuristicBestAreaFit()
            pass
        elif settings.placeHeuristic == PlaceHeuristic.BEST_LONG_SIDE_FIT:
            self.heuristic = PlaceHeuristicBestLongSideFit()
            pass
        elif settings.placeHeuristic == PlaceHeuristic.BEST_SHORT_SIDE_FIT:
            self.heuristic = PlaceHeuristicBestShortSideFit()
            pass
        elif settings.placeHeuristic == PlaceHeuristic.WORST_SHORT_SIDE_FIT:
            self.heuristic = PlaceHeuristicWorstShortSideFit()
            pass
        elif settings.placeHeuristic == PlaceHeuristic.WORST_LONG_SIDE_FIT:
            self.heuristic = PlaceHeuristicWorstLongSideFit()
            pass
        elif settings.placeHeuristic == PlaceHeuristic.WORST_AREA_FIT:
            self.heuristic = PlaceHeuristicWorstAreaFit()
            pass
        else:
            raise BinPackerValidateSettingsError( "Place heuristic incorrect %s" % str(settings.placeHeuristic) )
            pass
        pass

    def _initSplitter(self, settings):
        if settings.splitRule == GuillotineSplitRule.SHORTER_AXIS:
           self.splitter = SplitterShorterAxis()
           pass
        elif settings.splitRule == GuillotineSplitRule.SHORTER_LEFTOVER_AXIS:
           self.splitter = SplitterShorterLeftOverAxis()
           pass
        elif settings.splitRule == GuillotineSplitRule.LONGER_AXIS:
           self.splitter = SplitterLongerAxis()
           pass
        elif settings.splitRule == GuillotineSplitRule.LONGER_LEFTOVER_AXIS:
           self.splitter = SplitterLongerLeftOverAxis()
           pass
        elif settings.splitRule == GuillotineSplitRule.HORIZONTAL:
           self.splitter = SplitterHorizontal()
           pass
        elif settings.splitRule == GuillotineSplitRule.VERTICAL:
           self.splitter = SplitterVertical()
           pass
        elif settings.splitRule == GuillotineSplitRule.MAX_AREA:
           self.splitter = SplitterMaxArea()
           pass
        elif settings.splitRule == GuillotineSplitRule.MIN_AREA:
           self.splitter = SplitterMinArea()
           pass
        else:
           raise BinPackerValidateSettingsError( "Split Rule incorrect %s" % str(settings.splitRule) )
           pass
        pass
    pass

