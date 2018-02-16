from pypack2d.pack2d.rectangle import Rectangle
from pypack2d.pack2d.border import Border


class BinBase(Rectangle):
    def _on_init(self):
        self.rotate = False
        self.border = Border(bbox=(0, 0, 0, 0))
        pass

    def set_border(self, border):
        self.border = border
        pass

    # overloaded
    def _get_width(self):
        return self._width + self.border.width

    # overloaded
    def _get_height(self):
        return self._height + self.border.height

    def get_rectangle_without_border(self):
        left = self.left + self.border.left
        top = self.top + self.border.top
        width = self.width - self.border.width
        height = self.height - self.border.height
        return Rectangle(left, top, width, height)
        pass

    def set_rotate(self, rotate):
        if self.rotate == rotate:
            return
            pass

        self.rotate = rotate
        self.set(0, 0, self.height, self.width)
        pass

    def flip(self):
        if self.is_rotate() is False:
            self.set_rotate(True)
            pass
        else:
            self.set_rotate(False)
            pass
        pass

    def rotate_up_right(self):
        if self.width <= self.height:
            return
            pass

        self.flip()
        pass

    def rotate_side_ways(self):
        if self.width >= self.height:
            return
            pass

        self.flip()
        pass

    def is_rotate(self):
        return self.rotate
        pass

    def get_uv(self, width, height):
        left = (self.left + self.border.left) / width
        top = (self.top + self.border.top) / height
        right = (self.right - self.border.right) / width
        bottom = (self.bottom - self.border.bottom) / height

        uv = (left, top, right, bottom)
        return uv
        pass


class Bin(BinBase):
    def clone(self):
        if self.rotate is True:
            bin = Bin(0, 0, self._height, self._width)
            pass
        else:
            bin = Bin(0, 0, self._width, self._height)
            pass

        bin.set_rotate(self.rotate)
        bin.set_id(self.id)
        return bin
        pass

    def _on_init(self):
        super(Bin, self)._on_init()
        self.id = None
        # self.id = Bin.initInstance()
        pass

    def set_id(self, id):
        self.id = id
        pass

    def get_id(self):
        return self.id
        pass

    pass