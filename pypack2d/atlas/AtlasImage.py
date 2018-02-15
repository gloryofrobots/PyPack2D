from pypack2d.pack2d import BorderType
from pypack2d.atlas.BorderDraw import BorderDrawEdge,BorderDrawRectangle
from PIL import Image

class AtlasImage(object):
    def __init__(self, path = None, img = None):
        super(AtlasImage, self).__init__()
        if  path != None:
            self._initFromFilename(path)
            pass
        elif img is not None:
            self._initFromImage(img)
            pass

        self._initialise()
        self.uv = (0,0,0,0)
        self.bin = None
        pass

    def _initFromFilename(self, path):
        self.img = Image.open(path)
        self.path = path
        pass

    def _initFromImage(self, img):
        self.img = img
        self.path = None
        pass

    def __repr__(self):
        return "<%s %s (%i,%i)>" %( self.__class__.__name__, self.path, self.width, self.height)
        pass

    def getBin(self):
        return self.bin
        pass

    def _initialise(self):
        self.width = self.img.size[0]
        self.height = self.img.size[1]
        pass

    def getImagePIL(self):
        return self.img
        pass

    def getPath(self):
        return  self.path
        pass

    def getWidth(self):
        return self.width
        pass

    def getHeight(self):
        return self.height
        pass

    def setBin(self, bin):
        self.bin = bin

        if self.bin.isRotate():
            self.rotate()
            pass

        border = self.bin.getBorder()

        if border.isEmpty() is True:
            return
            pass

        self.drawBorder(border)
        pass

    def rotate(self):
        self.img = self.img.rotate(-90)
        self._initialise()
        pass

    def drawBorder(self, border):
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

    def getUV(self):
        return self.uv
        pass

    def isRotate(self):
        return self.bin.isRotate()
        pass

    def pack(self, atlas):

        canvas = atlas.getCanvas()

        self.uv = self.bin.getUV(atlas.width, atlas.height)

        if self.bin is None:
            raise BaseException("Atlas Image pack error. Bin not determined")
            pass

        canvas.paste(self.img, box = (self.bin.left, self.bin.top))
        self._onPack(atlas)
        pass

    def _onPack(self,atlas):
        pass
    pass

class AtlasImagePyBuilder(AtlasImage):
    def __init__(self, path, onPackCallback = None):
        super(AtlasImagePyBuilder, self).__init__(path)
        self.onPackCallback = onPackCallback
        pass

    def _onPack(self,atlas):
        self.onPackCallback(self, atlas)
        pass
    pass