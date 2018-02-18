from pypack2d.pack2d.settings import SortOrder


class RectangleSorting(object):
    def sort(self, input, order):
        is_reverse = self.get_reverse_from_order(order)
        self._on_sort(input, is_reverse)

    def _on_sort(self, input, reverse):
        input.sort(key=lambda image: self.get_sorting_attribute(image), reverse=reverse)

    def get_sorting_attribute(self, image):
        pass

    def get_reverse_from_order(self, order):
        if order == SortOrder.DESC:
            return True

        return False


class RectangleSortingArea(RectangleSorting):
    def get_sorting_attribute(self, image):
        return image.width * image.height


class RectangleSortingWidth(RectangleSorting):
    def get_sorting_attribute(self, image):
        return image.width


class RectangleSortingHeight(RectangleSorting):
    def get_sorting_attribute(self, image):
        return image.height


class RectangleSortingShorterSide(RectangleSorting):
    def get_sorting_attribute(self, image):
        width = image.width
        height = image.height
        if width < height:
            return width

        return height


class RectangleSortingLongerSide(RectangleSorting):
    def get_sorting_attribute(self, image):
        width = image.width
        height = image.height
        if width > height:
            return width

        return height


class RectangleSortingPerimeter(RectangleSorting):
    def get_sorting_attribute(self, image):
        width = image.width
        height = image.height
        return width + height


class RectangleSortingSideLengthDifference(RectangleSorting):
    def get_sorting_attribute(self, image):
        width = image.width
        height = image.height
        return width - height


class RectangleSortingSideRatio(RectangleSorting):
    def get_sorting_attribute(self, image):
        width = image.width
        height = image.height
        return width / height
