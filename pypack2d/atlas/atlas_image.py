from pypack2d.pack2d import BorderType
from pypack2d.atlas.border_draw import BorderDrawEdge, BorderDrawRectangle
from PIL import Image


class AtlasImage(object):
    def __init__(self, path=None, img=None):
        super(AtlasImage, self).__init__()
        self.img = None
        if path != None:
            self._init_from_filename(path)
            pass
        elif img is not None:
            self._init_from_image(img)
            pass

        self._initialise()
        self.uv = (0, 0, 0, 0)
        self.bin = None
        pass

    def _init_from_filename(self, path):
        self.img = Image.open(path)
        self.path = path
        pass

    def _init_from_image(self, img):
        self.img = img
        self.path = None
        pass

    def __repr__(self):
        return "<%s %s (%i,%i)>" % (self.__class__.__name__, self.path, self.width, self.height)
        pass

    def getBin(self):
        return self.bin
        pass

    def _initialise(self):
        self.width = self.img.size[0]
        self.height = self.img.size[1]
        pass

    def get_image_PIL(self):
        return self.img
        pass

    def set_bin(self, bin):
        self.bin = bin

        if self.bin.is_rotate():
            self.rotate()
            pass

        border = self.bin.border

        if border.is_empty() is True:
            return
            pass

        self.draw_border(border)
        pass

    def rotate(self):
        self.img = self.img.rotate(-90)
        self._initialise()
        pass

    def draw_border(self, border):
        draw = None
        if border.type == BorderType.PIXELS_FROM_EDGE:
            draw = BorderDrawEdge()
            pass
        elif border.type == BorderType.SOLID:
            draw = BorderDrawRectangle()
            pass

        self.img = draw.draw(self, border)
        self._initialise()
        pass

    def is_rotate(self):
        return self.bin.isRotate()

    def pack(self, atlas):

        canvas = atlas.get_canvas()

        self.uv = self.bin.get_uv(atlas.width, atlas.height)

        if self.bin is None:
            raise BaseException("Atlas Image pack error. Bin not determined")
            pass

        canvas.paste(self.img, box=(self.bin.left, self.bin.top))
        self._on_pack(atlas)
        pass

    def _on_pack(self, atlas):
        pass

    pass


class AtlasImagePyBuilder(AtlasImage):
    def __init__(self, path, onPackCallback=None):
        super(AtlasImagePyBuilder, self).__init__(path)
        self.onPackCallback = onPackCallback
        pass

    def _on_pack(self, atlas):
        self.onPackCallback(self, atlas)
        pass

    pass
