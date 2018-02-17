from pypack2d.pack2d.utils import min_sort, max_sort


class PlaceHeuristicException(BaseException):
    pass


class PlaceHeuristic(object):
    def choose(self, rect, first, second):
        if first is None and second is None:
            raise PlaceHeuristicException("PlaceHeuristic Incorrect arguments all is None")

        if first is None:
            return second, first

        if second is None:
            return first, second

        return self._choose(rect, first, second)

    def _choose(self, rect, first, second):
        raise NotImplementedError()


### SHELF
class PlaceHeuristicFirstFit(PlaceHeuristic):
    def _choose(self, rect, first, second):
        return first, second


class PlaceHeuristicBestWidthFit(PlaceHeuristic):
    def _choose(self, rect, first, second):
        left_over1 = first.width - rect.width
        left_over2 = second.width - rect.width
        return min_sort(left_over1, left_over2, first, second)


class PlaceHeuristicWorstWidthFit(PlaceHeuristic):
    def _choose(self, rect, first, second):
        left_over1 = first.width - rect.width
        left_over2 = second.width - rect.width
        return max_sort(left_over1, left_over2, first, second)


class PlaceHeuristicBestHeightFit(PlaceHeuristic):
    def _choose(self, rect, first, second):
        left_over1 = first.height - rect.height
        left_over2 = second.height - rect.height
        return min_sort(left_over1, left_over2, first, second)


class PlaceHeuristicWorstHeightFit(PlaceHeuristic):
    def _choose(self, rect, first, second):
        left_over1 = first.height - rect.height
        left_over2 = second.height - rect.height
        return max_sort(left_over1, left_over2, first, second)


### GUILLOTINE

class PlaceHeuristicBestShortSideFit(PlaceHeuristic):
    def _choose(self, rect, first, second):
        left_over1 = min(first.width - rect.width, first.height - rect.height)
        left_over2 = min(second.width - rect.width, second.height - rect.height)
        return min_sort(left_over1, left_over2, first, second)


class PlaceHeuristicWorstShortSideFit(PlaceHeuristic):
    def _choose(self, rect, first, second):
        left_over1 = min(first.width - rect.width, first.height - rect.height)
        left_over2 = min(second.width - rect.width, second.height - rect.height)
        return max_sort(left_over1, left_over2, first, second)


class PlaceHeuristicWorstLongSideFit(PlaceHeuristic):
    def _choose(self, rect, first, second):
        left_over1 = max(first.width - rect.width, first.height - rect.height)
        left_over2 = max(second.width - rect.width, second.height - rect.height)
        return max_sort(left_over1, left_over2, first, second)


class PlaceHeuristicBestLongSideFit(PlaceHeuristic):
    def _choose(self, rect, first, second):
        left_over1 = max(first.width - rect.width, first.height - rect.height)
        left_over2 = max(second.width - rect.width, second.height - rect.height)
        return min_sort(left_over1, left_over2, first, second)


class PlaceHeuristicBestAreaFit(PlaceHeuristic):
    def _choose(self, rect, first, second):
        left_over1 = first.area - rect.area
        left_over2 = second.area - rect.area
        return min_sort(left_over1, left_over2, first, second)


class PlaceHeuristicWorstAreaFit(PlaceHeuristic):
    def _choose(self, rect, first, second):
        left_over1 = first.area - rect.area
        left_over2 = second.area - rect.area
        return max_sort(left_over1, left_over2, first, second)


# MaxRects
class PlaceHeuristicBottomLeft(PlaceHeuristic):
    def _choose(self, rect, first, second):
        if first.top == second.top:
            if first.left <= second.left:
                return first, second

            return second, first

        return min_sort(first.top, second.top, first, second)
