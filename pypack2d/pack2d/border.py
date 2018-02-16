class Border(object):
    def __init__(self, border_type, color, left, top, right, bottom):
        self.left = left
        self.top = top
        self.right = right
        self.bottom = bottom
        self.type = border_type
        self.color = color

    @staticmethod
    def empty():
        return Border.from_size(None, None, 0)

    @staticmethod
    def from_border(border):
        return Border(border.type, border.color, border.left, border.top, border.right, border.bottom)

    @staticmethod
    def from_size(border_type, color, size):
        return Border(border_type, color, size, size, size, size)

    @staticmethod
    def from_rect(border_type, color, rect):
        return Border(border_type, color, rect[0], rect[1], rect[2], rect[3])

    def is_empty(self):
        if self.left == 0 and self.right == 0 and self.top == 0 and self.bottom == 0:
            return True

        return False

    @property
    def width(self):
        return self.left + self.right

    @property
    def height(self):
        return self.top + self.bottom
