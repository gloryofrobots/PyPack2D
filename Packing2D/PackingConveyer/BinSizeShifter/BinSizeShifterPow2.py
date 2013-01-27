__author__ = 'human88998999877'

from Packing2D.PackingConveyer.BinSizeShifter.BinSizeShifter import BinSizeShifter
from Packing2D.Rectangle import Rectangle

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

class BinSizeShifterPow2(BinSizeShifter):
    def _onShift(self, binSet):
        self.normaliseSize(binSet)
        pass

    def _normaliseSize(self, binSet, newWidth, newHeight):
        #print("normaliseSize")
        #print(newWidth,newHeight)

        newRect = Rectangle( 0, 0, newWidth, newHeight )

        if self.canChangeRect(binSet, newRect) is False:
            #print("CANT CHANGE",newRect)
            return False
            pass
        
        binSet.setSize(int(newRect.width), int(newRect.height))
        return True
        pass
    pass

    def normaliseSize(self, binSet):
        newWidth = getLowPow2( binSet.getWidth() )
        newHeight = getLowPow2( binSet.getHeight() )

        if self._normaliseSize(binSet, newWidth, newHeight) is False:
            if self._normaliseSize(binSet, binSet.getWidth(), newHeight) is False:
                if self._normaliseSize(binSet, newWidth, binSet.getHeight()) is False:
                    return False
                    pass
                pass
            pass

        self.normaliseSize(binSet)
        return True
        pass

    def canChangeRect(self, binSet, newRect):
        for bin in binSet:
            if newRect.contain(bin) is False:
                return False
                pass
            pass

        return True
        pass
    pass