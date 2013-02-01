from Packing2D.Rectangle import Rectangle

class Bin(Rectangle):
    id = 0

    @staticmethod
    def initInstance():
        id = Bin.id
        Bin.id += 1
        return id
        pass

    def __init__(self, x, y, width, height):
        super(Bin, self).__init__( x, y, width, height)
        self.rotate = False
        self.border = (0,0,0,0)
        self.id = Bin.initInstance()
        pass

    def getId(self):
        return self.id
        pass

    def setBorder(self, border):
        self.border = border

        self.width = self.width + border[0] + border[2]
        self.height = self.height + border[1] + border[3]
        pass

    def getBorder(self):
        return self.border
        pass

    def getRectangleWithoutBorder(self):
        left = self.left + self.border[0]
        top = self.top + self.border[1]
        width = self.width - (self.border[0] + self.border[2])
        height = self.height - (self.border[1] + self.border[3])
        return Rectangle( left, top, width, height )
        pass
    
    def setRotate(self, rotate):
        if self.rotate == rotate:
            return
            pass
        
        self.rotate = rotate
        self.set(0, 0, self.height, self.width)
        pass

    def flip(self):
        if self.isRotate() is False:
            self.setRotate(True)
            pass
        else:
            self.setRotate(False)
            pass
        pass

    def rotateUpRight(self):
        if self.width <= self.height:
            return
            pass

        self.flip()
        pass

    def rotateSideWays(self):
        if self.width >= self.height:
            return
            pass

        self.flip()
        pass

    def isRotate(self):
        return self.rotate
        pass
    
#    def getUV(self):
#        rect = self.getDestinationRect()
#        left = (rect.left + self.border.left) / self.packer.getWidth()
#        top = (rect.top + self.border.top) / self.packer.getHeight()
#        right = (rect.right - self.border.right) / self.packer.getWidth()
#        bottom = (rect.bottom - self.border.bottom) / self.packer.getHeight()
#
#        uv = (left, top, right, bottom)
#        return uv
#        pass
    pass
  