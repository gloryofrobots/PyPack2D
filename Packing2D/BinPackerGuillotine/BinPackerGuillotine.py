__author__ = 'human88998999877'

from Packing2D.BinPacker.BinPacker import BinPacker,BinPackerValidateSettingsError
from Packing2D import PlaceHeuristic,GuillotineSplitRule


from Packing2D.BinPackerGuillotine.Splitter import SplitterHorizontal,SplitterLongerAxis \
                                                    ,SplitterLongerLeftOverAxis,SplitterMaxArea, SplitterShorterAxis\
                                                    ,SplitterShorterLeftOverAxis, SplitterMinArea,SplitterVertical


from Packing2D.BinPackerGuillotine.PackNode import PackNode

#TODO RECTANGLE MERGE
class BinPackerGuillotine(BinPacker):
    def _onInitialise(self, factory, settings):
        self.splitter = None
        self._initSplitter(settings)

        self.heuristic = None

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

