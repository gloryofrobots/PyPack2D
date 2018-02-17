from pypack2d.pack.rectangle import Rectangle


class Splitter(object):
    def split(self, host_rect, rect):
        return self._on_split(host_rect, rect)

    def _on_split(self, host_rect, rect):
        raise NotImplementedError()


class SplitterHorizontal(Splitter):
    def _on_split(self, host_rect, rect):
        first = Rectangle(host_rect.left + rect.width, host_rect.top, host_rect.width - rect.width, rect.height)
        second = Rectangle(host_rect.left, host_rect.top + rect.height, host_rect.width, host_rect.height - rect.height)
        return first, second


class SplitterVertical(Splitter):
    def _on_split(self, host_rect, rect):
        first = Rectangle(host_rect.left + rect.width, host_rect.top, host_rect.width - rect.width, host_rect.height)
        second = Rectangle(host_rect.left, host_rect.top + rect.height, rect.width, host_rect.height - rect.height)
        return first, second


class SplitterShorterAxis(Splitter):
    def _on_split(self, host_rect, rect):
        if host_rect.width < host_rect.height:
            splitter = SplitterHorizontal()

        else:
            splitter = SplitterVertical()

        return splitter.split(host_rect, rect)


class SplitterShorterLeftOverAxis(Splitter):
    def _on_split(self, host_rect, rect):
        if (host_rect.width - rect.width) < (host_rect.height - rect.height):
            splitter = SplitterHorizontal()

        else:
            splitter = SplitterVertical()

        return splitter.split(host_rect, rect)


class SplitterLongerAxis(Splitter):
    def _on_split(self, host_rect, rect):
        if host_rect.width >= host_rect.height:
            splitter = SplitterHorizontal()

        else:
            splitter = SplitterVertical()

        return splitter.split(host_rect, rect)


class SplitterLongerLeftOverAxis(Splitter):
    def _on_split(self, host_rect, rect):
        if (host_rect.width - rect.width) >= (host_rect.height - rect.height):
            splitter = SplitterHorizontal()

        else:
            splitter = SplitterVertical()

        return splitter.split(host_rect, rect)


class SplitterMaxArea(Splitter):
    def _on_split(self, host_rect, rect):
        splitter_vertical = SplitterVertical()
        ver1, ver2 = splitter_vertical.split(host_rect, rect)
        min_ver = min(ver1.area, ver2.area)
        splitter_horizontal = SplitterHorizontal()
        hor1, hor2 = splitter_horizontal.split(host_rect, rect)
        min_hor = min(hor1.area, hor2.area)
        if min_hor < min_ver:
            return hor1, hor2

        return ver1, ver2


class SplitterMinArea(Splitter):
    def _on_split(self, host_rect, rect):
        splitter_vertical = SplitterVertical()
        ver1, ver2 = splitter_vertical.split(host_rect, rect)
        min_ver = max(ver1.area, ver2.area)
        splitter_horizontal = SplitterHorizontal()
        hor1, hor2 = splitter_horizontal.split(host_rect, rect)
        min_hor = max(hor1.area, hor2.area)
        if min_hor > min_ver:
            return hor1, hor2

        return ver1, ver2
