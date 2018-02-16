from pypack2d.pack2d.pack2d import Pack2D
from pypack2d.pack2d.bin import Bin
from pypack2d.pack2d.settings import BorderType
from pypack2d.border_draw import BorderDrawEdge, BorderDrawRectangle
import glob
import os

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


class Atlas(object):
    def __init__(self, width, height, dirPath, fileName, texMode, atlasType, fillColor):
        super(Atlas, self).__init__()
        self.width = width
        self.height = height
        self.dirPath = dirPath
        self.fileName = fileName
        self.textureMode = texMode
        self.atlasType = atlasType
        self.fillColor = fillColor

        self.canvas = None
        self.images = []

    def add_image(self, image):
        self.images.append(image)
        return True

    def get_canvas(self):
        return self.canvas

    def save(self):
        path = os.path.join(self.dirPath, self.fileName)
        self.canvas.save(path, self.atlasType)

    def show(self):
        self.canvas.show()

    def pack(self):
        self.canvas = Image.new(self.textureMode, (self.width, self.height), self.fillColor)
        for img in self.images:
            img.pack(self)


class AtlasGenerator(object):
    def __init__(self, destination_directory, packing_settings, *,
                 file_prefix="atlas",
                 texture_mode="RGBA",
                 file_type="png",
                 fill_color="#000"):
        super().__init__()
        self.dir_path = destination_directory
        self.relative_filename = file_prefix

        self.packing_settings = packing_settings
        self.tex_mode = texture_mode
        self.atlas_type = file_type
        self.fill_color = fill_color

        self.images = {}
        self.wasted_images = []
        self.atlases = []
        self.packing = Pack2D(packing_settings)

    def get_new_atlas(self, binSet):
        index = len(self.atlases)
        counter = ""
        if index > 0:
            counter = "%i" % index

        atlasFileName = self.relative_filename + counter + "." + self.atlas_type
        binWidth = binSet.width
        binHeight = binSet.height
        atlas = Atlas(binWidth, binHeight, self.dir_path, atlasFileName, self.tex_mode, self.atlas_type,
                      self.fill_color)
        return atlas

    def add_file(self, filename):
        image = AtlasImage(path=filename)
        self._add_image(image)

    def add_glob(self, pathname, recursive=False):
        for infile in glob.glob(pathname, recursive=recursive):
            self.add_file(infile)

    def add_image(self, img):
        image = AtlasImage(img=img)
        self._add_image(image)

    def _add_image(self, image):
        bin = Bin(0, 0, image.width, image.height)
        idBin = len(self.images)
        bin.set_id(idBin)
        self.packing.push(bin)
        self.images[idBin] = image

    def _work_with_waste(self, wasted):
        for wasteImage in wasted:
            image = self._get_image_for_bin(wasteImage)
            self.wasted_images.append(image)

    def _get_image_for_bin(self, bin):
        idBin = bin.get_id()
        image = self.images[idBin]
        return image

    def _work_with_result(self, binSets):
        for binSet in binSets:
            atlas = self.get_new_atlas(binSet)
            for bin in binSet:
                image = self._get_image_for_bin(bin)

                image.set_bin(bin)
                atlas.add_image(image)

            atlas.pack()
            atlas.save()

            if self.packing_settings.debug is True:
                pass
                # atlas.show()

            self.atlases.append(atlas)

    def stats(self, binSets):
        if len(binSets) is 0:
            return

        total = 0
        for binSet in binSets:
            total += binSet.get_efficiency()

        eff = total / len(binSets)
        return dict(count=len(binSets), efficiency=eff)

    def generate(self):
        self.packing.pack()

        wasted = self.packing.get_waste()
        self._work_with_waste(wasted)

        binSets = self.packing.get_result()
        self._work_with_result(binSets)

        stats = self.stats(binSets)
        return stats

    def get_wasted_images(self):
        return self.wasted_images
