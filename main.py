from pypack2d.pack2d import settings
from pypack2d.atlas.generator import AtlasGenerator
from pypack2d.atlas.atlas_image import AtlasImage
import glob

options = settings.PackingSettings(
    algo=settings.PackingAlgorithm.MAX_RECTANGLES,
    heuristic=settings.PlaceHeuristic.BEST_AREA_FIT,
    sort_order=settings.SortOrder.DESC,
    sort_key=settings.SortKey.AREA,
    bin_size_mode=settings.BinSizeMode.STRICT,
    packing_mode=settings.PackingMode.OFFLINE,

    rotate_mode=settings.RotateMode.AUTO,
    max_width=256,
    max_height=256,
    border=None,
    # border_mode = settings.BorderMode.STRICT
    border_mode=None,
    border_size=0,
    split_rule=settings.GuillotineSplitRule.SHORTER_AXIS,
    debug=True,
)

generator = AtlasGenerator()
generator.initialise(options, "img/res", "atlas", "RGB", "png", "#fff")

for infile in glob.glob("img/src/*.png"):
    im = AtlasImage(infile)
    generator.add_image(im)

generator.generate()
