from Packing2D import SortOrder
__author__ = 'human88998999877'

class RectangleSorting(object):
    def sort(self, input, order):
        isReverse = self.getReverseFromOrder(order)
        self._onSort(input, isReverse)
        pass

    def _onSort(self, input, isReverse):
        sorted(input, key = lambda image: self.getSortingAttribute(image), reverse = isReverse)
        pass

    def getSortingAttribute(self, image):
        pass
    
    def getReverseFromOrder(self, order):
        if order == SortOrder.ASC:
            return True
            pass
        
        return True
        pass
    pass


class RectangleSortingArea(RectangleSorting):
    def getSortingAttribute(self, image):
        
        pass
    pass

class RectangleSortingShorterSide(Sort):
    def getSortingAttribute(self, image):

        pass
    pass

class RectangleSortingLongerSide(Sort):
    def getSortingAttribute(self, image):

        pass
    pass

class RectangleSortingPerimeter(Sort):
    def getSortingAttribute(self, image):

        pass
    pass

class RectangleSortingSideLengthDifference(Sort):
    def getSortingAttribute(self, image):

        pass
    pass

class RectangleSortingSideRatio(Sort):
    def getSortingAttribute(self, image):

        pass
    pass



