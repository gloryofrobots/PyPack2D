__author__ = 'human88998999877'

def maxSort(val1, val2, first, second):
    if val1 > val2:
        return first,second
        pass

    return second, first
    pass

def minSort(val1, val2, first, second):
    if val1 < val2:
        return first,second
        pass

    return second, first
    pass

class PlaceHeuristic(object):
    def choose(self, rect, first, second):
        return self._choose(rect, first, second)
        pass

    def _choose(self, rect, first, second):
        raise NotImplementedError()
        pass
    pass

class PlaceHeuristicNextFit(PlaceHeuristic):
    def choose(self, rect, first, second):
        return first,second
        pass
    pass

class PlaceHeuristicBestShortSideFit(PlaceHeuristic):
    def choose(self, rect, first, second):
        leftOver1 = min( first.width - rect.width, first.height - rect.height )
        leftOver2  = min( second.width - rect.width, second.height - rect.height )
        return minSort(leftOver1, leftOver2, first, second)
        pass
    pass

class PlaceHeuristicWorstShortSideFit(PlaceHeuristic):
    def choose(self, rect, first, second):
        leftOver1 = min( first.width - rect.width, first.height - rect.height )
        leftOver2  = min( second.width - rect.width, second.height - rect.height )
        return maxSort(leftOver1, leftOver2, first, second)
        pass
    pass

class PlaceHeuristicWorstLongSideFit(PlaceHeuristic):
    def choose(self, rect, first, second):
        leftOver1 = max( first.width - rect.width, first.height - rect.height )
        leftOver2 = max( second.width - rect.width, second.height - rect.height )
        return maxSort(leftOver1, leftOver2, first, second)
        pass
    pass


class PlaceHeuristicBestLongSideFit(PlaceHeuristic):
    def choose(self, rect, first, second):
        leftOver1 = max( first.width - rect.width, first.height - rect.height )
        leftOver2 = max( second.width - rect.width, second.height - rect.height )
        return minSort(leftOver1, leftOver2, first, second)
        pass
    pass

class PlaceHeuristicBestAreaFit(PlaceHeuristic):
    def choose(self, rect, first, second):
        return minSort(first.area, second.area, first, second)
        pass
    pass

class PlaceHeuristicWorstAreaFit(PlaceHeuristic):
    def choose(self, rect, first, second):
        return maxSort(first.area, second.area, first, second)
        pass
    pass