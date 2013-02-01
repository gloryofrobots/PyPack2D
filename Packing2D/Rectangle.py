class BBox(object):
    def __init__(self, left, top, right, bottom):
        pass

class Rectangle:
    @staticmethod
    def createFromBB(left, top, right, bottom):
        rect = Rectangle()
        rect.setBB(left, top , right, bottom)
        return rect
        pass

    def __init__(self, *args):
        if len(args) == 4:
            self._createFromLeftTopWidthHeight(*args)
            pass
        elif len(args) == 2:
            self._createFromWidthHeight(*args)
            pass

        elif len(args) == 1:
            self._createFromRectangle(*args)
            pass
        elif len(args) == 0:
            self._createFromWidthHeight(0,0)
            pass
        pass

    def _createFromRectangle(self, rect):
        self.set(rect.left, rect.top, rect.width, rect.height)
        pass

    def _createFromLeftTopWidthHeight(self, x, y, width, height):
        self.set(x, y, width, height)
        pass

    def _createFromWidthHeight(self,width, height):
        self.set(0, 0, width, height)
        pass

    def set(self, x, y, width, height):
        self._x = x
        self._y = y
        self._width = width
        self._height = height
        pass

    def setBB(self, left, top, right, bottom):
        self._x = left
        self._y = top
        self._width = right - left
        self._height = bottom - top
        pass

    def setCoord(self, x, y):
        self._x = x
        self._y = y
        pass
    
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

    def setWidth(self, width):
        self._width = width
        pass
    
    width = property(fget = getWidth, fset = setWidth)

    def getHeight(self):
        return self._height
        pass

    def setHeight(self, height):
        self._height = height
        pass

    height = property(fget = getHeight, fset = setHeight)

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

    def getLongerSide(self):
        if self.width > self.height:
            return self.width
            pass

        return self.height
        pass

    def getShorterSide(self):
        if self.width < self.height:
            return self.width
            pass

        return self.height
        pass

    def isContain(self, rect):
        if self.right < rect.right \
            or self.bottom < rect.bottom \
            or self.left > rect.left \
            or self.top >  rect.top:
            return False
            pass

        return True
        pass

    def isPossibleToFit(self, rect):
        if self.height < rect.height or self.width < rect.width:
            return False
            pass

        return True
        pass

    def isIntersect(self, rect):
        if self.left >= rect.right or self.top >= rect.bottom or self.right <= rect.left or self.bottom <= rect.top:
            return False
            pass

        return True
        pass

    def getIntersection(self, rect):
        if self.isIntersect(rect) is False:
            return None
            pass

        left = max(self.left, rect.left)
        top = max(self.top,rect.top)
        width = min(self.width, rect.width)
        height = min(self.height, rect.height)
        return Rectangle(left, top, width, height)
        pass

    def __repr__(self):
        return "Rectangle %s : %s <left %d top : %d right : %d bottom: %d>" % (str(self.__class__.__name__), hex(id(self)), self.left, self.top, self.right, self.bottom)
        pass
    pass