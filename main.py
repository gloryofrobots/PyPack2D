import pypack2d
from pypack2d.pack2d.border import Border

settings = dict(
    algo=pypack2d.PackingAlgorithm.MAX_RECTANGLES,
    heuristic=pypack2d.PlaceHeuristic.BEST_AREA_FIT,
    sort_order=pypack2d.SortOrder.DESC,
    sort_key=pypack2d.SortKey.AREA,
    bin_size_mode=pypack2d.BinSizeMode.STRICT,
    packing_mode=pypack2d.PackingMode.OFFLINE,

    rotate_mode=pypack2d.RotateMode.AUTO,
    max_width=256,
    max_height=256,
    # border=dict(rect=(1, 1, 1, 1), type=pypack2d.BorderType.SOLID, color="#000"),
    border=dict(size=1, type=pypack2d.BorderType.SOLID, color="#000"),
    border_mode=pypack2d.BorderMode.AUTO,
    split_rule=pypack2d.GuillotineSplitRule.SHORTER_AXIS,
    debug=True,
)

generator = pypack2d.generator("img/res", settings, file_prefix="atlas")

generator.add_glob("img/src/*.png")

stats = generator.generate()
print("Count images: %i efficiency : %4.2f " % (stats["count"], stats["efficiency"]))
