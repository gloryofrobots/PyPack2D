from pypack2d.pack2d.packer.packer import BinPacker
from pypack2d.pack2d.rectangle import Rectangle


class Cell(Rectangle):
    def cut(self, width):
        self.set_bb(self.left + width, self.top, self.right, self.bottom)
        pass

    def is_over(self):
        if self.width == 0 or self.height == 0:
            return True
            pass
        pass

    def can_place(self, rect):
        if self.height < rect.height or self.width < rect.width:
            return False
            pass

        return True
        pass

    def place(self, rect):
        left = self.left
        top = self.top
        destinationRect = Rectangle(left, top, rect.width, rect.height)
        self.cut(rect.width)
        return destinationRect
        pass

    pass


class BinPackerCell(BinPacker):
    def _on_set_size(self):
        self.cells = [Cell(0, 0, self.max_width, self.max_height)]
        pass

    def _on_pack_bin(self, bin):
        bestCell = self.get_best_cell(bin)

        if bestCell is None:
            return False
            pass

        destinationRect = bestCell.place(bin)

        newLine = Cell(destinationRect.left, destinationRect.bottom, destinationRect.width,
                       bestCell.height - bin.height)

        if bestCell.is_over() is True:
            self.cells.remove(bestCell)
            pass

        self.cells.append(newLine)

        self.normalise(destinationRect)

        bin.set_coord(destinationRect.left, destinationRect.top)
        return True
        pass

    def can_place(self, cell, rect):
        if cell.height < rect.height:
            return False
            pass

        if cell.width >= rect.width:
            return True
            pass

        rightEdge = cell.left + rect.width

        if rightEdge > self.max_width:
            return False
            pass

        for bin in self.binSet:
            if bin.left < rightEdge and bin.bottom > cell.top:
                return False
                pass
            pass

        return True
        pass

    pass

    def get_best_cell(self, bin):
        bestCell = None
        minTopLeft = self.max_height * 2
        for cell in self.cells:
            if self.can_place(cell, bin) is False:
                continue
                pass

            topLeft = cell.top + bin.height

            if minTopLeft < topLeft:
                continue
                pass

            bestCell = cell
            minTopLeft = topLeft
            pass

        return bestCell
        pass

    def normalise(self, destinationRect):
        newCells = []
        for cell in self.cells:
            if cell.left < destinationRect.right \
                    and cell.top < destinationRect.top:

                if cell.right < destinationRect.right:
                    cell.set_bb(cell.left, cell.top, cell.right, destinationRect.top)
                    pass
                else:
                    newCell = Cell(cell.left, cell.top, destinationRect.right, destinationRect.top)
                    cell.cut(newCell.width)
                    newCells.append(newCell)
                    pass

                pass

        if len(newCells) is not 0:
            self.cells.extend(newCells)
            pass
        pass

    pass
