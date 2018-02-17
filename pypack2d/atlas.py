from pypack2d.pack2d.pack import Pack2D
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
        if path is not None:
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

    def _initialise(self):
        self.width = self.img.size[0]
        self.height = self.img.size[1]

    def get_pil_image(self):
        return self.img

    def set_bin(self, bin):
        self.bin = bin

        if self.bin.is_rotate():
            self.__rotate()

        border = self.bin.border

        if border.is_empty() is True:
            return

        self.draw_border(border)

    def __rotate(self):
        self.img = self.img.rotate(-90, expand=True)
        self._initialise()

    def draw_border(self, border):
        draw = None
        if border.type == BorderType.PIXELS_FROM_EDGE:
            draw = BorderDrawEdge()

        elif border.type == BorderType.SOLID:
            draw = BorderDrawRectangle()

        self.img = draw.draw(self, border)
        self._initialise()

    @property
    def is_rotated(self):
        return self.bin.is_rotate()

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
    def __init__(self, width, height, dir_path, filename, tex_mode, atlas_type, fill_color):
        super(Atlas, self).__init__()
        self.width = width
        self.height = height
        self.dirname = dir_path
        self.filename = filename
        self.texture_mode = tex_mode
        self.image_type = atlas_type
        self.fill_color = fill_color

        self.canvas = None
        self.images = []

    def add_image(self, image):
        self.images.append(image)
        return True

    def get_canvas(self):
        return self.canvas

    def get_path_with_extension(self, ext):
        return os.path.join(self.dirname, ("%s.%s" % (self.filename, ext)))

    @property
    def path(self):
        return self.get_path_with_extension(self.image_type)

    def save(self, callback):
        callback(self)
        self.canvas.save(self.path, self.image_type)

    def show(self):
        self.canvas.show()

    def pack(self):
        self.canvas = Image.new(self.texture_mode, (self.width, self.height), self.fill_color)
        for img in self.images:
            img.pack(self)

    def __iter__(self):
        return self.images.__iter__()


class AtlasGenerator(object):
    def __init__(self, destination_directory, packing_settings,
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

    def get_new_atlas(self, bin_set):
        index = len(self.atlases)
        counter = ""
        if index > 0:
            counter = "%i" % index

        atlas_filename = self.relative_filename + counter
        bin_width = bin_set.width
        bin_height = bin_set.height
        atlas = Atlas(bin_width, bin_height, self.dir_path, atlas_filename, self.tex_mode, self.atlas_type,
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
        bin_id = len(self.images)
        bin.set_id(bin_id)
        self.packing.push(bin)
        self.images[bin_id] = image

    def _work_with_waste(self, wasted):
        for wasteImage in wasted:
            image = self._get_image_for_bin(wasteImage)
            self.wasted_images.append(image)

    def _get_image_for_bin(self, bin):
        image = self.images[bin.id]
        return image

    def _work_with_result(self, bin_sets):
        for bin_set in bin_sets:
            atlas = self.get_new_atlas(bin_set)
            for bin in bin_set:
                image = self._get_image_for_bin(bin)

                image.set_bin(bin)
                atlas.add_image(image)

            atlas.pack()
            atlas.save(self.packing_settings.callback)

            self.atlases.append(atlas)

    @staticmethod
    def stats(bin_sets):
        if len(bin_sets) is 0:
            return

        total = 0
        for bin_set in bin_sets:
            total += bin_set.get_efficiency()

        eff = total / len(bin_sets)
        return dict(count=len(bin_sets), efficiency=eff)

    def generate(self):
        self.packing.pack()

        wasted = self.packing.get_waste()
        self._work_with_waste(wasted)

        bin_sets = self.packing.get_result()
        self._work_with_result(bin_sets)

        stats = self.stats(bin_sets)
        return stats

    def get_wasted_images(self):
        return self.wasted_images
