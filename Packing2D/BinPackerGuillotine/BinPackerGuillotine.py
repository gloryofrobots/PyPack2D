__author__ = 'human88998999877'

from PyBuilder.Atlas.AtlasGenerator.TexturePackerBinaryTree.Rectangle import Rectangle
from PyBuilder.Atlas.AtlasGenerator.TexturePackerBinaryTree.Texture import Texture
from PyBuilder.Atlas.AtlasGenerator.TexturePackerBinaryTree.PackNode import PackNode

def getLowPow2( x ):
    y = 1
    if y > x:
        return None
    while True:
        if y >= x:
            return y / 2
            pass
        y *= 2
        pass
    pass

def getNearestPow2( x ):
    y = 1
    if y > x:
        return None
    while True:
        if y >= x:
            return y
            pass
        y *= 2
        pass
    pass


from Packing2D.BinPacker.BinPacker import BinPacker,BinPackerValidateSettingsError
from Packing2D import PackingAlgorithmAbility,PlaceHeuristic,GuillotineSplitRule,BorderMode


#GuillotineSplitRule = Enum("SHORTER_AXIS"
#                           , "LONGER_AXIS"
#                           , "SHORTER_LEFTOVER_AXIS"
#                           , "LONGER_LEFTOVER_AXIS"
#                           , "MAX_AREA"
#                           , "MIN_AREA")
#PlaceHeuristic = Enum(  "NEXT_FIT"
#                      , "BEST_WIDTH_FIT"
#                      , "BEST_HEIGHT_FIT"
#                      , "WORST_WIDTH_FIT"
#                      , "WORST_HEIGHT_FIT"
#                      , "BEST_AREA_FIT"
#                      , "BEST_SHORT_SIDE_FIT"
#                      , "BEST_LONG_SIDE_FIT"
#                      , "WORST_AREA_FIT"
#                      , "WORST_SHORT_SIDE_FIT"
#                      , "WORST_LONG_SIDE_FIT"
#                      , "BOTTOM_LEFT"
#                      , "BEST_FIT")


class Splitter(object):
    def split(self, hostRect, rect):
        return self._onSplit(hostRect, rect)
        pass

    def _onSplit(self, hostRect, rect):
        raise NotImplementedError()
        pass
    pass



class SplitterHorizontal(Splitter):
    def _onSplit(self, hostRect, rect):
        first = Rectangle(hostRect.left+rect.width, hostRect.top, hostRect.right, hostRect.top+rect.height)
        second = Rectangle(hostRect.left, hostRect.top+rect.height, hostRect.right,hostRect.bottom)
        return first,second
        pass
    pass

class SplitterVertical(Splitter):
    def _onSplit(self, hostRect, rect):
        first = Rectangle(hostRect.left+rect.width, hostRect.top, hostRect.right, hostRect.top+rect.height)
        second = Rectangle(hostRect.left, hostRect.top+rect.height, hostRect.right,hostRect.bottom)
        return first,second
        pass
    pass

class SplitterShorterAxis(Splitter):
    pass


class PlaceHeuristic(object):
    def choose(self, first, second):
        return self._choose(first, second)
        pass

    def _choose(self, first, second):
        raise NotImplementedError()
        pass
    pass

class PlaceHeuristicNextFit(PlaceHeuristic):
    def _choose(self, first, second):
        return first
        pass
    pass

class BinPackerGuillotine(BinPacker):

    def _onInitialise(self, factory, settings):
        self.splitter = None
        if settings.splitRule == GuillotineSplitRule.SHORTER_AXIS:
            self.splitter = SplitterShorterAxis()
            pass
        else:
            raise BinPackerValidateSettingsError( "Split Rule incorrect %s" % str(settings.splitRule) )
            pass

        self.heuristic = None
        if settings.placeHeuristic == PlaceHeuristic.NEXT_FIT:
            self.heuristic = PlaceHeuristicNextFit()
            pass
        else:
            raise BinPackerValidateSettingsError( "Place heuristic incorrect %s" % str(settings.placeHeuristic) )
            pass

        self.packNode =  PackNode(0, 0, settings.maxWidth,  settings.maxHeight)
        pass
    
    def _onPackBin(self, bin):
        leaf = self.packNode.insert( bin )
        if leaf == None:
            return False
            pass

        bin.setCoord(leaf.left, leaf.top)
        return True
        pass

from Packing2D.Rectangle import Rectangle

class PackNode(Rectangle):
    """
    Creates an area which can recursively pack other areas of smaller sizes into itself.
    """
    def __init__(self, x, y, width, height):
        super(Rectangle, self).__init__(x, y, width, height)
        self.firstChild = None
        self.secondChild = None
        pass

    def hasChildren(self):
        if self.secondChild is None \
            and self.firstChild is None:
            return False
            pass

        return True
        pass

    def __repr__(self):
        return "<%s %s>" % (self.__class__.__name__, str(self.rect))
        pass

    def getFreeBranch(self, rect, placer):
        if self.hasChildren() is True:
            best,worth = placer.getPlace(self.firstChild, self.secondChild)
            leaf = best.getFreeBranch(rect)
            if leaf is None:
                return worth.getFreeBranch(rect)
                pass
            else:
                return leaf
                pass
            pass

        if rect.width > self.getWidth() or rect.height > self.getHeight():
            return None
            pass

        return self
        pass

    def insert(self, rect, splitter, placer):
        if self.hasChildren() is True:
            best,worth = placer.getPlace(self.firstChild, self.secondChild)
            leaf = best.insert(rect)
            if leaf is None:
                return worth.insert(rect)
                pass
            else:
                return leaf
                pass
            pass
        
        if rect.width > self.width or rect.height > self.height:
            return None
            pass

        rectangles = splitter.getRects(self, rect)

        self.firstChild = PackNode( rectangles[0] )
        self.secondChild = PackNode( rectangles[1] )
        
        leaf = PackNode( Rectangle(self.left, self.top, self.left+rect.width, self.top+rect.height) )
        return leaf
        pass
    pass
