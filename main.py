import pypack2d.pack2d as packing
from pypack2d.pack2d.settings import PackingSettings
from pypack2d.atlas.AtlasGenerator import AtlasGenerator
from pypack2d.atlas.AtlasImage import AtlasImage
from PIL import Image
import glob, os

settings = PackingSettings()
settings.packingAlgorithm = packing.PackingAlgorithm.MAX_RECTANGLES
settings.placeHeuristic = packing.PlaceHeuristic.BEST_WIDTH_FIT
settings.sortOrder = packing.SortOrder.ASC
settings.sortKey = packing.SortKey.AREA
settings.binSizeMode = packing.BinSizeMode.STRICT
settings.packingMode = packing.PackingMode.OFFLINE

settings.rotateMode = packing.RotateMode.AUTO
settings.maxWidth = 256
settings.maxHeight = 256
settings.border = None
# settings.borderMode = packing.BorderMode.STRICT
settings.borderMode = None
settings.isDebug = True
settings.borderSize = 0

settings.splitRule = packing.GuillotineSplitRule.SHORTER_AXIS


generator = AtlasGenerator()
generator.initialise(settings, "img/res", "atlas", "RGB", "png", "#fff")


for infile in glob.glob("img/src/*.png"):
    im = AtlasImage(infile)
    generator.addImage(im)

generator.generate()

