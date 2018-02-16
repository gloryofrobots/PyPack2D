from pypack2d.pack2d.packer.packer import BinPacker
from pypack2d.pack2d.rectangle import Rectangle


class Shelf(Rectangle):
    def _on_init(self):
        self.bins = []
        self.freeRect = Rectangle(self.left, self.top, self.width, self.height)

    def get_free_rect(self):
        return self.freeRect

    def can_place(self, rect):
        if self.freeRect.height < rect.height or self.freeRect.width < rect.width:
            return False

        return True

    def is_empty(self):
        return len(self.bins) == 0

    def place(self, bin):
        destinationRect = Rectangle(self.freeRect.left, self.freeRect.top, bin.width, bin.height)

        self.freeRect = Rectangle.from_bb(destinationRect.right, self.freeRect.top, self.right, self.bottom)
        self.bins.append(bin)
        return destinationRect


# TODO FLOOR CEILING

class BinPackerShelf(BinPacker):
    def _on_init(self, factories, settings):
        self.shelves = []

    def _on_pack_bin(self, bin):
        shelf = self.get_shelf(bin, self.heuristic)

        # TODO ROTATE
        if shelf is None:
            return False

        destination = shelf.place(bin)

        bin.set_coord(destination.left, destination.top)
        return True

    def _on_flush(self):
        self.shelves = []

    def create_new_shelf(self, bin):
        y = 0
        if len(self.shelves) is not 0:
            topShelf = self.shelves[len(self.shelves) - 1]
            y = topShelf.bottom

        if y + bin.height > self.max_height:
            return None

        shelf = Shelf(0, y, self.max_width, bin.height)
        self.shelves.append(shelf)
        return shelf

    def get_shelf(self, bin, heuristic):
        bestShelf = None
        bestRect = None
        for shelf in self.shelves:
            if shelf.can_place(bin) is False:
                continue

            rect = shelf.get_free_rect()
            best, worth = heuristic.choose(bin, bestRect, rect)

            if best is not bestRect:
                bestRect = best
                bestShelf = shelf

        if bestShelf is None:
            shelf = self.create_new_shelf(bin)
            return shelf

        return bestShelf
