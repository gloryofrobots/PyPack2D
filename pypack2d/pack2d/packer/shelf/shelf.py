from pypack2d.pack2d.packer.packer import BinPacker
from pypack2d.pack2d.Rectangle import Rectangle


class Shelf(Rectangle):
    def _onInit(self):
        self.bins = []
        self.freeRect = Rectangle(self.left, self.top, self.width, self.height)
        pass

    def getFreeRect(self):
        return self.freeRect
        pass

    def canPlace(self, rect):
        if self.freeRect.height < rect.height or self.freeRect.width < rect.width:
            return False
            pass

        return True
        pass

    def isEmpty(self):
        return len(self.bins) == 0
        pass

    def place(self, bin):
        destinationRect = Rectangle(self.freeRect.left, self.freeRect.top, bin.width, bin.height)

        self.freeRect = Rectangle.fromBB(destinationRect.right, self.freeRect.top, self.right, self.bottom)
        self.bins.append(bin)
        return destinationRect
        pass

    pass


# TODO FLOOR CEILING

class BinPackerShelf(BinPacker):
    def _onInitialise(self, factory, settings):
        self.shelves = []
        pass

    def _onPackBin(self, bin):
        shelf = self.getShelf(bin, self.heuristic)

        # TODO ROTATE
        if shelf is None:
            return False
            pass

        destination = shelf.place(bin)

        bin.setCoord(destination.left, destination.top)
        return True
        pass

    def _onFlush(self):
        self.shelves = []
        pass

    def createNewShelf(self, bin):
        y = 0
        if len(self.shelves) is not 0:
            topShelf = self.shelves[len(self.shelves) - 1]
            y = topShelf.bottom
            pass

        if y + bin.height > self.maxHeight:
            return None
            pass

        shelf = Shelf(0, y, self.maxWidth, bin.height)
        self.shelves.append(shelf)
        return shelf
        pass

    def getShelf(self, bin, heuristic):
        bestShelf = None
        bestRect = None
        for shelf in self.shelves:
            if shelf.canPlace(bin) is False:
                continue
                pass

            rect = shelf.getFreeRect()
            best, worth = heuristic.choose(bin, bestRect, rect)

            if best is not bestRect:
                bestRect = best
                bestShelf = shelf
                pass
            pass

        if bestShelf is None:
            shelf = self.createNewShelf(bin)
            return shelf
            pass

        return bestShelf
        pass

    pass
