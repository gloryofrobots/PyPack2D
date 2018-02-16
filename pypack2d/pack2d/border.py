class Border(object):
    def __init__(self, bbox=None, border=None, border_size=None, type=None, color=None):
        self.left = None
        self.top = None
        self.right = None
        self.bottom = None
        self.type = None
        self.color = None

        if bbox is not None:
            self.init(bbox[0], bbox[1], bbox[2], bbox[3], type, color)

        elif border is not None:
            self.init(border.left, border.top, border.right, border.bottom, border.type, border.color)
            return

        elif border_size is not None:
            self.init(border_size, border_size, border_size, border_size, type, color)

    def init(self, left, top, right, bottom, type=None, color=None):
        self.left = left
        self.top = top
        self.right = right
        self.bottom = bottom
        self.type = type
        self.color = color

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
