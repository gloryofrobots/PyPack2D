from pypack2d.pack2d.rectangle import Rectangle


class Splitter(object):
    def split(self, hostRect, rect):
        return self._on_split(hostRect, rect)

    def _on_split(self, hostRect, rect):
        raise NotImplementedError()


class SplitterHorizontal(Splitter):
    def _on_split(self, hostRect, rect):
        first = Rectangle(hostRect.left + rect.width, hostRect.top, hostRect.width - rect.width, rect.height)
        second = Rectangle(hostRect.left, hostRect.top + rect.height, hostRect.width, hostRect.height - rect.height)
        return first, second


class SplitterVertical(Splitter):
    def _on_split(self, hostRect, rect):
        first = Rectangle(hostRect.left + rect.width, hostRect.top, hostRect.width - rect.width, hostRect.height)
        second = Rectangle(hostRect.left, hostRect.top + rect.height, rect.width, hostRect.height - rect.height)
        return first, second


class SplitterShorterAxis(Splitter):
    def _on_split(self, hostRect, rect):
        if hostRect.width < hostRect.height:
            splitter = SplitterHorizontal()

        else:
            splitter = SplitterVertical()

        return splitter.split(hostRect, rect)


class SplitterShorterLeftOverAxis(Splitter):
    def _on_split(self, hostRect, rect):
        if (hostRect.width - rect.width) < (hostRect.height - rect.height):
            splitter = SplitterHorizontal()

        else:
            splitter = SplitterVertical()

        return splitter.split(hostRect, rect)


class SplitterLongerAxis(Splitter):
    def _on_split(self, hostRect, rect):
        if hostRect.width >= hostRect.height:
            splitter = SplitterHorizontal()

        else:
            splitter = SplitterVertical()

        return splitter.split(hostRect, rect)


class SplitterLongerLeftOverAxis(Splitter):
    def _on_split(self, hostRect, rect):
        if (hostRect.width - rect.width) >= (hostRect.height - rect.height):
            splitter = SplitterHorizontal()

        else:
            splitter = SplitterVertical()

        return splitter.split(hostRect, rect)


class SplitterMaxArea(Splitter):
    def _on_split(self, hostRect, rect):
        splitterVertical = SplitterVertical()
        ver1, ver2 = splitterVertical.split(hostRect, rect)
        minVer = min(ver1.area, ver2.area)
        splitterHorizontal = SplitterHorizontal()
        hor1, hor2 = splitterHorizontal.split(hostRect, rect)
        minHor = min(hor1.area, hor2.area)
        if minHor < minVer:
            return hor1, hor2

        return ver1, ver2


class SplitterMinArea(Splitter):
    def _on_split(self, hostRect, rect):
        splitterVertical = SplitterVertical()
        ver1, ver2 = splitterVertical.split(hostRect, rect)
        minVer = max(ver1.area, ver2.area)
        splitterHorizontal = SplitterHorizontal()
        hor1, hor2 = splitterHorizontal.split(hostRect, rect)
        minHor = max(hor1.area, hor2.area)
        if minHor > minVer:
            return hor1, hor2

        return ver1, ver2
