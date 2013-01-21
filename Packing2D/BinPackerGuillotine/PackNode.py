from PyBuilder.Atlas.AtlasGenerator.TexturePackerBinaryTree.Rectangle import Rectangle

class PackNode(object):
    """
    Creates an area which can recursively pack other areas of smaller sizes into itself.
    """
    def __init__(self, rect):
        super().__init__()
        self.rect = rect
        self.rightTree = None
        self.bottomTree = None
        pass

    def hasChildren(self):
        if self.bottomTree is None \
            and self.rightTree is None:
            return False
            pass

        return True
        pass

    def getLeft(self):
        return self.rect.left
        pass

    def getTop(self):
        return self.rect.top
        pass

    def getWidth(self):
        return self.rect.width
        pass

    def getHeight(self):
        return self.rect.height
        pass

    def __repr__(self):
        return "<%s %s>" % (self.__class__.__name__, str(self.rect))
        pass

#    def getFreeSpaceRight(self):
#        if self.rightTree is None:
#            return self.getWidth()
#            pass
#
#        return self.rightTree.getFreeSpaceRight()
#        pass
#
#    def getFreeSpaceBottom(self):
#        if self.bottomTree is None:
#            return self.getHeight()
#            pass
#
#        return self.bottomTree.getFreeSpaceBottom()
#        pass

    def getFreeBranch(self, rect):
        if self.hasChildren() is True:
            leaf = self.rightTree.getFreeBranch(rect)
            if leaf is None:
                return self.bottomTree.getFreeBranch(rect)
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

    def insert(self, rect):
        #print ("insert",area)
        if self.hasChildren() is True:
            leaf = self.rightTree.insert(rect)
            if leaf is None:
                return self.bottomTree.insert(rect)
                pass
            else:
                return leaf
                pass
            pass

        if rect.width <= self.getWidth() and rect.height <= self.getHeight():
            self.rightTree = PackNode(  Rectangle( self.rect.left+rect.width, self.rect.top, self.rect.right, self.rect.top+rect.height) )
            #print("c 0")
            #print(self.child[0])
            self.bottomTree = PackNode( Rectangle(self.rect.left, self.rect.top+rect.height, self.rect.right, self.rect.bottom) )
            #print("c 1")
            #print(self.child[1])
            leaf = PackNode( Rectangle(self.rect.left, self.rect.top, self.rect.left+rect.width, self.rect.top+rect.height) )
            return leaf
            pass

        return None
        pass
    pass