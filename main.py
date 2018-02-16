import pypack2d

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
    # border=dict(
    #         rect=dict(left=1, top=1, right=1, bottom=1),
    #         type=pypack2d.BorderType.SOLID,
    #         color="#000"
    # ),
    border=dict(size=1,
                type=pypack2d.BorderType.PIXELS_FROM_EDGE,
                color="#fff"
    ),
    border_mode=pypack2d.BorderMode.AUTO,
    split_rule=pypack2d.GuillotineSplitRule.SHORTER_AXIS,
    debug=True,
)

generator = pypack2d.generator("img/res", settings, file_prefix="atlas")

generator.add_glob("img/src/*.png")

stats = generator.generate()
print("Count images: %i efficiency : %4.2f " % (stats["count"], stats["efficiency"]))
