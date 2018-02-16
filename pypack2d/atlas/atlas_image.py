from pypack2d.pack2d.settings import BorderType
from pypack2d.atlas.border_draw import BorderDrawEdge, BorderDrawRectangle
from PIL import Image


class AtlasImage(object):
    def __init__(self, path=None, img=None):
        super(AtlasImage, self).__init__()
        self.img = None
        if path != None:
            self._init_from_filename(path)

        elif img is not None:
            self._init_from_image(img)

        self._initialise()
        self.uv = (0, 0, 0, 0)
        self.bin = None

    def _init_from_filename(self, path):
        self.img = Image.open(path)
        self.path = path

    def _init_from_image(self, img):
        self.img = img
        self.path = None

    def __repr__(self):
        return "<%s %s (%i,%i)>" % (self.__class__.__name__, self.path, self.width, self.height)

    def getBin(self):
        return self.bin

    def _initialise(self):
        self.width = self.img.size[0]
        self.height = self.img.size[1]

    def get_image_PIL(self):
        return self.img

    def set_bin(self, bin):
        self.bin = bin

        if self.bin.is_rotate():
            self.rotate()

        border = self.bin.border

        if border.is_empty() is True:
            return

        self.draw_border(border)

    def rotate(self):
        self.img = self.img.rotate(-90)
        self._initialise()

    def draw_border(self, border):
        draw = None
        if border.type == BorderType.PIXELS_FROM_EDGE:
            draw = BorderDrawEdge()

        elif border.type == BorderType.SOLID:
            draw = BorderDrawRectangle()

        self.img = draw.draw(self, border)
        self._initialise()

    def is_rotate(self):
        return self.bin.isRotate()

    def pack(self, atlas):

        canvas = atlas.get_canvas()

        self.uv = self.bin.get_uv(atlas.width, atlas.height)

        if self.bin is None:
            raise BaseException("Atlas Image pack error. Bin not determined")

        canvas.paste(self.img, box=(self.bin.left, self.bin.top))
        self._on_pack(atlas)

    def _on_pack(self, atlas):
        pass


class AtlasImagePyBuilder(AtlasImage):
    def __init__(self, path, onPackCallback=None):
        super(AtlasImagePyBuilder, self).__init__(path)
        self.onPackCallback = onPackCallback

    def _on_pack(self, atlas):
        self.onPackCallback(self, atlas)
