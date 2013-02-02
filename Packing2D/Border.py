class Border(object):
    def __init__(self, bbox = None, border = None, borderSize = None, type = None, color = None):
        if bbox != None:
            self.init(bbox[0], bbox[1], bbox[2], bbox[3], type, color)
            pass
        elif border != None:
            self.init(border.left, border.top, border.right, border.bottom, border.type, border.color)
            return
            pass
        elif borderSize != None:
            self.init(borderSize, borderSize, borderSize, borderSize, type = None, color = None)
            pass
        pass
    
    def init(self, left, top, right, bottom, type = None, color = None):
        self.left = left
        self.top = top
        self.right = right
        self.bottom = bottom
        self.type = type
        self.color = color
        pass
    pass
