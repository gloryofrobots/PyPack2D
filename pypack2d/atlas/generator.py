from pypack2d.atlas.atlas import Atlas
from pypack2d.pack2d.pack2d import Pack2D
from pypack2d.pack2d.bin import Bin


class AtlasGenerator(object):
    def __init__(self):
        super(AtlasGenerator, self).__init__()
        self.packing = Pack2D()
        pass

    def initialise(self, settings, dirPath, relativeFileName, texMode, atlasType, fillColor):
        self.dir_path = dirPath
        self.relative_filename = relativeFileName

        self.settings = settings
        self.tex_mode = texMode
        self.atlas_type = atlasType
        self.fill_color = fillColor

        self.images = {}
        self.wasted_images = []
        self.atlases = []

        self.packing.initialise(settings)
        pass

    def get_new_atlas(self, binSet):
        index = len(self.atlases)
        counter = ""
        if index > 0:
            counter = "%i" % index
            pass

        atlas = Atlas()
        atlasFileName = self.relative_filename + counter + "." + self.atlas_type
        binWidth = binSet.width
        binHeight = binSet.height
        atlas.initialise(binWidth, binHeight, self.dir_path, atlasFileName, self.tex_mode, self.atlas_type, self.fill_color)
        return atlas
        pass

    def add_images(self, images):
        for image in images:
            self.add_image(image)
            pass
        pass

    def add_image(self, image):
        bin = Bin(0, 0, image.width, image.height)
        idBin = len(self.images)
        bin.set_id(idBin)
        self.packing.push(bin)
        self.images[idBin] = image
        pass

    def _work_with_waste(self, wasted):
        for wasteImage in wasted:
            image = self._get_image_for_bin(wasteImage)
            self.wasted_images.append(image)
            pass
        pass

    def _get_image_for_bin(self, bin):
        idBin = bin.get_id()
        image = self.images[idBin]
        return image
        pass

    def _work_with_result(self, binSets):
        for binSet in binSets:
            atlas = self.get_new_atlas(binSet)
            for bin in binSet:
                image = self._get_image_for_bin(bin)

                image.set_bin(bin)
                atlas.add_image(image)
                pass

            atlas.pack()
            atlas.save()

            if self.settings.isDebug is True:
                # atlas.show()
                pass

            self.atlases.append(atlas)
            pass
        pass

    def report(self, binSets):
        if len(binSets) is 0:
            return
            pass

        total = 0
        for binSet in binSets:
            total += binSet.get_efficiency()
            pass

        middle = total / len(binSets)
        print("Count images: %i efficiency : %4.2f " % (len(binSets), middle))
        pass

    def generate(self):
        self.packing.pack()

        wasted = self.packing.getWaste()
        self._work_with_waste(wasted)

        binSets = self.packing.getResult()
        self._work_with_result(binSets)

        if self.settings.isDebug is True:
            self.report(binSets)
            pass
        pass

    def get_wasted_images(self):
        return self.wasted_images
        pass

    pass
