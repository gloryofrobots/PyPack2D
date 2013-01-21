
class Rectangle:
    def __init__(self, x, y, width, height):
        self.set(x, y, width, height)
        pass

    def set(self, x, y, width, height):
        self._x = x
        self._y = y
        self._width = width
        self._height = height
        pass

    def setCoord(self, x, y):
        self._x = x
        self._y = y
        pass
    
#    def increasePosition(self, add):
#        self._x += add.left
#        self._y += add.top
#        pass
    
    def isZeroSize(self):
        if self._x == 0 and self._width == 0 and self._y == 0 and self._height == 0:
            return True
            pass
        
        return False
        pass
    
    def getArea(self):
        return self._width * self._height
        pass

    area = property(fget=getArea)

    def getCoord(self):
        return ( self.left, self.top, self.right , self.bottom )
        pass

    def getWidth(self):
        return self._width
        pass

    width = property(fget=getWidth)

    def getHeight(self):
        return self._height
        pass

    height = property(fget=getHeight)

    def getLeft(self):
        return self._x
        pass
    
    left = property(fget=getLeft)
    
    def getRight(self):
        return self._x + self._width
        pass
    
    right = property(fget=getRight)
    
    def getTop(self):
        return self._y
        pass

    top = property(fget=getTop)

    def getBottom(self):
        return self._y + self._height
        pass

    bottom = property(fget=getBottom)

    def contain(self, rect):
        #print("I am ",self)
        #print("other ", rect)

        if self.width < rect.width \
            or self.height < rect.height \
            or self.left > rect.left \
            or self.top >  rect.top:
            return False
            pass

        return True
        pass

    def __repr__(self):
        return "Rectangle<left %d top : %d right : %d bottom: %d>" % (self._x,self._y, self._width, self._height)
        pass
    pass