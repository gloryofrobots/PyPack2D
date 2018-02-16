from pypack2d.pack2d.settings import SortOrder


class RectangleSorting(object):
    def sort(self, input, order):
        isReverse = self.get_reverse_from_order(order)
        self._on_sort(input, isReverse)
        pass

    def _on_sort(self, input, isReverse):
        input.sort(key=lambda image: self.get_sorting_attribute(image), reverse=isReverse)
        pass

    def get_sorting_attribute(self, image):
        pass

    def get_reverse_from_order(self, order):
        if order == SortOrder.DESC:
            return True
            pass

        return False
        pass

    pass


class RectangleSortingArea(RectangleSorting):
    def get_sorting_attribute(self, image):
        return image.width * image.height
        pass

    pass


class RectangleSortingWidth(RectangleSorting):
    def get_sorting_attribute(self, image):
        return image.width
        pass

    pass


class RectangleSortingHeight(RectangleSorting):
    def get_sorting_attribute(self, image):
        return image.heght
        pass

    pass


class RectangleSortingShorterSide(RectangleSorting):
    def get_sorting_attribute(self, image):
        width = image.width
        height = image.height
        if width < height:
            return width
            pass

        return height
        pass

    pass


class RectangleSortingLongerSide(RectangleSorting):
    def get_sorting_attribute(self, image):
        width = image.width
        height = image.height
        if width > height:
            return width
            pass

        return height
        pass

    pass


class RectangleSortingPerimeter(RectangleSorting):
    def get_sorting_attribute(self, image):
        width = image.width
        height = image.height
        return width + height
        pass

    pass


class RectangleSortingSideLengthDifference(RectangleSorting):
    def get_sorting_attribute(self, image):
        width = image.width
        height = image.height
        return width - height
        pass

    pass


class RectangleSortingSideRatio(RectangleSorting):
    def get_sorting_attribute(self, image):
        width = image.width
        height = image.height
        return width / height
        pass

    pass
