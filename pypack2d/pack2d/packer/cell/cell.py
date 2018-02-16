from pypack2d.pack2d.packer.packer import BinPacker
from pypack2d.pack2d.rectangle import Rectangle


class Cell(Rectangle):
    def cut(self, width):
        self.set_bb(self.left + width, self.top, self.right, self.bottom)

    def is_over(self):
        if self.width == 0 or self.height == 0:
            return True

    def can_place(self, rect):
        if self.height < rect.height or self.width < rect.width:
            return False

        return True

    def place(self, rect):
        left = self.left
        top = self.top
        destinationRect = Rectangle(left, top, rect.width, rect.height)
        self.cut(rect.width)
        return destinationRect


class BinPackerCell(BinPacker):
    def _on_set_size(self):
        self.cells = [Cell(0, 0, self.max_width, self.max_height)]

    def _on_pack_bin(self, bin):
        bestCell = self.get_best_cell(bin)

        if bestCell is None:
            return False

        destinationRect = bestCell.place(bin)

        newLine = Cell(destinationRect.left, destinationRect.bottom, destinationRect.width,
                       bestCell.height - bin.height)

        if bestCell.is_over() is True:
            self.cells.remove(bestCell)

        self.cells.append(newLine)

        self.normalise(destinationRect)

        bin.set_coord(destinationRect.left, destinationRect.top)
        return True

    def can_place(self, cell, rect):
        if cell.height < rect.height:
            return False

        if cell.width >= rect.width:
            return True

        rightEdge = cell.left + rect.width

        if rightEdge > self.max_width:
            return False

        for bin in self.binSet:
            if bin.left < rightEdge and bin.bottom > cell.top:
                return False

        return True

    def get_best_cell(self, bin):
        bestCell = None
        minTopLeft = self.max_height * 2
        for cell in self.cells:
            if self.can_place(cell, bin) is False:
                continue

            topLeft = cell.top + bin.height

            if minTopLeft < topLeft:
                continue

            bestCell = cell
            minTopLeft = topLeft

        return bestCell

    def normalise(self, destinationRect):
        newCells = []
        for cell in self.cells:
            if cell.left < destinationRect.right \
                    and cell.top < destinationRect.top:

                if cell.right < destinationRect.right:
                    cell.set_bb(cell.left, cell.top, cell.right, destinationRect.top)

                else:
                    newCell = Cell(cell.left, cell.top, destinationRect.right, destinationRect.top)
                    cell.cut(newCell.width)
                    newCells.append(newCell)

        if len(newCells) is not 0:
            self.cells.extend(newCells)
