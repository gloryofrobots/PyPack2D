from pypack2d.atlas.Atlas import Atlas
from pypack2d.pack2d.Packing2D import Packing2D
from pypack2d.pack2d.Bin import Bin

class AtlasGenerator(object):
    def __init__(self):
        super(AtlasGenerator,self).__init__()
        self.packing = Packing2D()
        pass

    def initialise(self, settings, dirPath, relativeFileName, texMode, atlasType, fillColor):
        self.dirPath = dirPath
        self.relativeFileName = relativeFileName

        self.settings = settings
        self.texMode = texMode
        self.atlasType = atlasType
        self.fillColor = fillColor

        self.images = {}
        self.wastedImages = []
        self.atlases = []

        self.packing.initialise(settings)
        pass

    def getNewAtlas(self, binSet):
        index = len(self.atlases)
        counter = ""
        if index > 0:
            counter = "%i" % index
            pass

        atlas = Atlas()
        atlasFileName = self.relativeFileName + counter + "." + self.atlasType
        binWidth = binSet.getWidth()
        binHeight = binSet.getHeight()
        atlas.initialise(binWidth, binHeight, self.dirPath, atlasFileName, self.texMode, self.atlasType, self.fillColor)
        return atlas
        pass

    def addImages(self, images):
        for image in images:
            self.addImage(image)
            pass
        pass

    def addImage(self, image):
        width = image.getWidth()
        height = image.getHeight()
        bin = Bin(0, 0, width, height)
        idBin = len(self.images)
        bin.setId(idBin)
        self.packing.push(bin)
        self.images[idBin] = image
        pass

    def _workWithWaste(self, wasted):
        for wasteImage in wasted:
            image = self._getImageForBin(wasteImage)
            self.wastedImages.append(image)
            pass
        pass

    def _getImageForBin(self, bin):
        idBin = bin.getId()
        image = self.images[idBin]
        return image
        pass

    def _workWithResult(self, binSets):
        for binSet in binSets:
            atlas = self.getNewAtlas(binSet)
            for bin in binSet:
                image = self._getImageForBin(bin)

                image.setBin(bin)
                atlas.addImage(image)
                pass

            atlas.pack()
            atlas.save()

            if self.settings.isDebug is True:
                #atlas.show()
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
            total += binSet.getEfficiency()
            pass

        middle = total / len(binSets)
        print ("Count images: %i efficiency : %4.2f " % (len(binSets), middle) )
        pass

    def generate(self):
        self.packing.pack()

        wasted = self.packing.getWaste()
        self._workWithWaste(wasted)

        binSets = self.packing.getResult()
        self._workWithResult(binSets)

        if self.settings.isDebug is True:
            self.report(binSets)
            pass
        pass


    def getWastedImages(self):
        return self.wastedImages
        pass
    pass
