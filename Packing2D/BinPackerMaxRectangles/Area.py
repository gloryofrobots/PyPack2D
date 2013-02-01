__author__ = 'human88998999877'
from Packing2D.Rectangle import Rectangle

class Area(Rectangle):
    def __init__(self, *args):
        super(Area, self).__init__(*args)
        self._isBad = False
        pass

    def markBad(self, mark):
        self._isBad = mark
        pass

    def isBad(self):
        return self._isBad
        pass
    pass