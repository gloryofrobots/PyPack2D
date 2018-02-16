class Rectangle:
    @classmethod
    def from_bb(cls, left, top, right, bottom):
        rect = cls(0, 0, 0, 0)
        rect.set_bb(left, top, right, bottom)
        return rect
        pass

    @classmethod
    def new(cls):
        rect = cls(0, 0, 0, 0)
        return rect
        pass

    @classmethod
    def from_rectangle(cls, rect):
        rect = cls(rect.left, rect.top, rect.width, rect.height)
        return rect
        pass

    @classmethod
    def from_wh(cls, width, height):
        rect = cls(0, 0, width, height)
        return rect
        pass

    def __init__(self, x, y, width, height):
        self.set(x, y, width, height)
        self._on_init()
        pass

    def _on_init(self):
        pass

    def set(self, x, y, width, height):
        self._x = x
        self._y = y
        self._width = width
        self._height = height
        pass

    def set_bb(self, left, top, right, bottom):
        self.set(left, top, (right - left), (bottom - top))
        pass

    def set_coord(self, x, y):
        self._x = x
        self._y = y
        pass

    def is_zero_size(self):
        if self.left == 0 and self.width == 0 and self.top == 0 and self.height == 0:
            return True
            pass

        return False
        pass

    @property
    def area(self):
        return self.width * self.height

    def get_bb(self):
        return (self.left, self.top, self.right, self.bottom)
        pass

    @property
    def width(self):
        return self._get_width()

    def _get_width(self):
        return self._width
        pass

    @property
    def height(self):
        return self._get_height()

    def _get_height(self):
        return self._height
        pass

    @property
    def left(self):
        return self._x

    @property
    def right(self):
        if self.width is None:
            return
        return self.left + self.width
        pass

    @property
    def top(self):
        return self._y
        pass

    @property
    def bottom(self):
        return self.top + self.height
        pass

    def get_longer_side(self):
        if self.width > self.height:
            return self.width
            pass

        return self.height
        pass

    def get_shorter_side(self):
        if self.width < self.height:
            return self.width
            pass

        return self.height
        pass

    def is_contain(self, rect):
        if self.right < rect.right \
                or self.bottom < rect.bottom \
                or self.left > rect.left \
                or self.top > rect.top:
            return False
            pass

        return True
        pass

    def is_possible_to_fit(self, rect):
        if self.height < rect.height or self.width < rect.width:
            return False
            pass

        return True
        pass

    def is_intersect(self, rect):
        if self.left >= rect.right or self.top >= rect.bottom or self.right <= rect.left or self.bottom <= rect.top:
            return False
            pass

        return True
        pass

    def get_intersection(self, rect):
        if self.is_intersect(rect) is False:
            return None
            pass

        left = max(self.left, rect.left)
        top = max(self.top, rect.top)
        width = min(self.width, rect.width)
        height = min(self.height, rect.height)
        return Rectangle(left, top, width, height)
        pass

    def __repr__(self):
        return "Rectangle %s : %s <left %d top : %d right : %d bottom: %d>" % (
        str(self.__class__.__name__), hex(id(self)), self.left, self.top, self.right, self.bottom)
        pass

    pass
