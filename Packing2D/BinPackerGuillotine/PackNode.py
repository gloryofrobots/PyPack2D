
from Packing2D.Rectangle import Rectangle

class PackNode(Rectangle):
    """
    Creates an area which can recursively pack other areas of smaller sizes into itself.
    """
    def __init__(self, *args):
        super(PackNode, self).__init__(*args)
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
            best,worth = placer.choose(rect, self.firstChild, self.secondChild)
            leaf = best.insert(rect, splitter, placer)
            if leaf is None:
                return worth.insert(rect, splitter, placer)
                pass
            else:
                return leaf
                pass
            pass
        
        if rect.width > self.width or rect.height > self.height:
            return None
            pass

        rectangles = splitter.split(self, rect)

        self.firstChild = PackNode( rectangles[0] )
        self.secondChild = PackNode( rectangles[1] )
        
        leaf = PackNode( Rectangle(self.left, self.top, self.left+rect.width, self.top+rect.height) )
        return leaf
        pass
    pass