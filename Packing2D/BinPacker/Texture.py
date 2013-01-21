from PyBuilder.Atlas.AtlasGenerator.TexturePackerBinaryTree.Rectangle import Rectangle

class Texture:
    def __init__(self, name, width, height, isRotate, packer):
        self.name = name
        self.packer = packer
        self.setDimensions(width, height)
        self.node = None
        self.rotate = isRotate
        self.border = Rectangle(0,0,0,0)
        pass

    def setDimensions(self, width, height):
        self.rect = Rectangle(0, 0, width, height)
        pass

    def setBorder(self, border):
        self.border = border
        width = self.rect.getWidth() + border.left + border.right
        height = self.rect.getHeight() + border.top + border.bottom
        #print("setBorder",self.rect.getWidth(),self.rect.getHeight(),width, height)
        self.setDimensions(width, height)
        pass

    def getBorder(self):
        return self.border
        pass

#    def setRotate(self):
#        self.rotate = True
#        self.rect = Rectangle(0, 0, self.rect.height, self.rect.width)
#        pass

    def isRotate(self):
        return self.rotate
        pass

    def getName(self):
        return self.name
        pass

    def getNode(self):
        return self.node
        pass

    def setNode(self,node):
        self.node = node
        pass

    def getDestinationRect(self):
        return self.node.rect
        pass

    def getX(self):
        return self.node.rect.left
        pass

    def getY(self):
        return self.node.rect.top
        pass

    def getImageRect(self):
        return self.rect
        pass

    def canFitInRect(self,rect):
        return rect.contain(self.node.rect)
        pass

    def getUV(self):
        rect = self.getDestinationRect()
        left = (rect.left + self.border.left) / self.packer.getWidth()
        top = (rect.top + self.border.top) / self.packer.getHeight()
        right = (rect.right - self.border.right) / self.packer.getWidth()
        bottom = (rect.bottom - self.border.bottom) / self.packer.getHeight()

        uv = (left, top, right, bottom)
        return uv
        pass
    pass
  