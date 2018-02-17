from pypack2d.pack.packer.packer import BinPacker
from pypack2d.pack.rectangle import Rectangle


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
        destination_rect = Rectangle(left, top, rect.width, rect.height)
        self.cut(rect.width)
        return destination_rect


class BinPackerCell(BinPacker):
    def _on_set_size(self):
        self.cells = [Cell(0, 0, self.max_width, self.max_height)]

    def _on_pack_bin(self, bin):
        best_cell = self.get_best_cell(bin)

        if best_cell is None:
            return False

        destination_rect = best_cell.place(bin)

        new_line = Cell(destination_rect.left, destination_rect.bottom,
                        destination_rect.width, best_cell.height - bin.height)

        if best_cell.is_over() is True:
            self.cells.remove(best_cell)

        self.cells.append(new_line)

        self.normalise(destination_rect)

        bin.set_coord(destination_rect.left, destination_rect.top)
        return True

    def can_place(self, cell, rect):
        if cell.height < rect.height:
            return False

        if cell.width >= rect.width:
            return True

        right_edge = cell.left + rect.width

        if right_edge > self.max_width:
            return False

        for bin in self.bin_set:
            if bin.left < right_edge and bin.bottom > cell.top:
                return False

        return True

    def get_best_cell(self, bin):
        best_cell = None
        min_top_left = self.max_height * 2
        for cell in self.cells:
            if self.can_place(cell, bin) is False:
                continue

            top_left = cell.top + bin.height

            if min_top_left < top_left:
                continue

            best_cell = cell
            min_top_left = top_left

        return best_cell

    def normalise(self, destination_rect):
        new_cells = []
        for cell in self.cells:
            if cell.left < destination_rect.right \
                    and cell.top < destination_rect.top:

                if cell.right < destination_rect.right:
                    cell.set_bb(cell.left, cell.top, cell.right, destination_rect.top)

                else:
                    new_cell = Cell(cell.left, cell.top, destination_rect.right, destination_rect.top)
                    cell.cut(new_cell.width)
                    new_cells.append(new_cell)

        if len(new_cells) is not 0:
            self.cells.extend(new_cells)
