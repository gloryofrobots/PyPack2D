from pypack2d.pack2d import settings
from pypack2d.atlas.generator import AtlasGenerator
from pypack2d.atlas.atlas_image import AtlasImage
import glob

options = settings.PackingSettings()
options.packing_algo = settings.PackingAlgorithm.MAX_RECTANGLES
options.place_heuristic = settings.PlaceHeuristic.BEST_WIDTH_FIT
options.sort_order = settings.SortOrder.ASC
options.sort_key = settings.SortKey.AREA
options.bin_size_mode = settings.BinSizeMode.STRICT
options.packing_mode = settings.PackingMode.OFFLINE

options.rotate_mode = settings.RotateMode.AUTO
options.max_width = 256
options.max_height = 256
options.border = None
# options.border_mode = settings.BorderMode.STRICT
options.border_mode = None
options.debug = True
options.border_size = 0

options.split_rule = settings.GuillotineSplitRule.SHORTER_AXIS


generator = AtlasGenerator()
generator.initialise(options, "img/res", "atlas", "RGB", "png", "#fff")


for infile in glob.glob("img/src/*.png"):
    im = AtlasImage(infile)
    generator.add_image(im)

generator.generate()

