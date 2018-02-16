from pypack2d.pack2d.packer.packer import BinPacker
from pypack2d.pack2d.rectangle import Rectangle


class Shelf(Rectangle):
    def _on_init(self):
        self.bins = []
        self.freeRect = Rectangle(self.left, self.top, self.width, self.height)
        pass

    def get_free_rect(self):
        return self.freeRect
        pass

    def can_place(self, rect):
        if self.freeRect.height < rect.height or self.freeRect.width < rect.width:
            return False
            pass

        return True
        pass

    def is_empty(self):
        return len(self.bins) == 0
        pass

    def place(self, bin):
        destinationRect = Rectangle(self.freeRect.left, self.freeRect.top, bin.width, bin.height)

        self.freeRect = Rectangle.from_bb(destinationRect.right, self.freeRect.top, self.right, self.bottom)
        self.bins.append(bin)
        return destinationRect
        pass

    pass


# TODO FLOOR CEILING

class BinPackerShelf(BinPacker):
    def _on_init(self, factory, settings):
        self.shelves = []
        pass

    def _on_pack_bin(self, bin):
        shelf = self.get_shelf(bin, self.heuristic)

        # TODO ROTATE
        if shelf is None:
            return False
            pass

        destination = shelf.place(bin)

        bin.set_coord(destination.left, destination.top)
        return True
        pass

    def _on_flush(self):
        self.shelves = []
        pass

    def create_new_shelf(self, bin):
        y = 0
        if len(self.shelves) is not 0:
            topShelf = self.shelves[len(self.shelves) - 1]
            y = topShelf.bottom
            pass

        if y + bin.height > self.max_height:
            return None
            pass

        shelf = Shelf(0, y, self.max_width, bin.height)
        self.shelves.append(shelf)
        return shelf
        pass

    def get_shelf(self, bin, heuristic):
        bestShelf = None
        bestRect = None
        for shelf in self.shelves:
            if shelf.can_place(bin) is False:
                continue
                pass

            rect = shelf.get_free_rect()
            best, worth = heuristic.choose(bin, bestRect, rect)

            if best is not bestRect:
                bestRect = best
                bestShelf = shelf
                pass
            pass

        if bestShelf is None:
            shelf = self.create_new_shelf(bin)
            return shelf
            pass

        return bestShelf
        pass

    pass
