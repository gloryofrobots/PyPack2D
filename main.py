import pypack2d

pack_settings = dict(
    algo=pypack2d.PackingAlgorithm.MAX_RECTANGLES,
    heuristic=pypack2d.PlaceHeuristic.BEST_AREA_FIT,
    sort_order=pypack2d.SortOrder.DESC,
    sort_key=pypack2d.SortKey.AREA,
    resize_mode=pypack2d.ResizeMode.MINIMIZE_POW2,
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
)


# stats = pypack2d.generate(["img/src/001.png", "img/src/000.png"], "img/res", pack_settings, file_prefix="atlas")
stats = pypack2d.generate(["img/src/*.png"], "img/res", pack_settings, file_prefix="atlas")
# generator = pypack2d.generator("img/res", settings,  src="img/src/*.png", file_prefix="atlas",)
# generator.add_glob("img/src/*.png")
# stats = generator.generate()

print("Count images: %i efficiency : %4.2f " % (stats["count"], stats["efficiency"]))


# Packer : self.validate(bin)

# def _on_debug(self):
#     return
#     from PIL import Image, ImageDraw
#     from random import choice, randrange
#
#     COLORS = []
#     for i in range(1000):
#         r = randrange(0, 255)
#         g = randrange(0, 255)
#         b = randrange(0, 255)
#         COLORS.append((r, g, b))
#
#     canvas = Image.new("RGBA", (self.binSet.width, self.binSet.height), color=(128, 128, 128))
#     draw = ImageDraw.Draw(canvas)
#
#     for area in self.areas:
#         draw.rectangle([area.left, area.top, area.right - 1, area.bottom - 1], outline=choice(COLORS))
#
#     for bin in self.binSet:
#         # img = Image.new("RGBA", (bin.width, bin.height), color = choice(COLORS))
#         draw.rectangle([bin.left, bin.top, bin.right - 1, bin.bottom - 1], fill=choice(COLORS))
#         # canvas.paste(img, (bin.left, bin.top))
#
#     canvas.show()
