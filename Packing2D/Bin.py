from Packing2D.Rectangle import Rectangle
from Packing2D.Border import Border

class Bin(Rectangle):
    id = 0

    @staticmethod
    def initInstance():
        id = Bin.id
        Bin.id += 1
        return id
        pass

    def _onInit(self):
        self.rotate = False
        self.border = Border(bbox = (0,0,0,0))
        self.id = Bin.initInstance()
        pass

    def getId(self):
        return self.id
        pass

    def setBorder(self, border):
        self.border = border
        pass

    def getBorder(self):
        return self.border
        pass

    #overloaded
    def _getWidth(self):
        return self._width + self.border.width
        pass

    #overloaded
    def _getHeight(self):
        return self._height + self.border.height
        pass
    
    def getRectangleWithoutBorder(self):
        left = self.left + self.border.left
        top = self.top + self.border.top
        width = self.width - self.border.width
        height = self.height - self.border.height
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
    
    def getUV(self, width, height):
        left = (self.left + self.border.left) / width
        top = (self.top + self.border.top) / height
        right = (self.right - self.border.right) / width
        bottom = (self.bottom - self.border.bottom) / height

        uv = (left, top, right, bottom)
        return uv
        pass
    pass
  