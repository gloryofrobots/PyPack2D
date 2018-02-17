import pypack2d
import pypack2d.utils

from PIL import Image
import json
import os
import glob


def callback(atlas):
    import json
    images = []
    for image in atlas:
        images.append(dict(
            uv=image.uv,
            path=image.path,
            rotated=image.is_rotated
        ))

    data_path = atlas.get_path_with_extension("json")
    data = dict(
        path=atlas.path,
        images=images
    )
    datafile = open(data_path, "w")
    with datafile as f:
        f.write(json.dumps(data))


def pack(pathname, atlasdir):
    pypack2d.utils.clear_dir(atlasdir)
    pack_settings = dict(
        callback=callback,
        # algo=dict(type=pypack2d.PackingAlgorithm.GUILLOTINE, split=pypack2d.GuillotineSplitRule.MAX_AREA),
        algo=pypack2d.PackingAlgorithm.MAX_RECTANGLES,
        heuristic=pypack2d.PlaceHeuristic.BEST_AREA_FIT,
        sort_order=pypack2d.SortOrder.ASC,
        sort_key=pypack2d.SortKey.SIDE_RATIO,
        resize_mode=pypack2d.ResizeMode.NONE,
        packing_mode=pypack2d.PackingMode.ONLINE,

        rotate_mode=pypack2d.RotateMode.SIDE_WAYS,
        max_width=512,
        max_height=512,
        border=dict(
            rect=dict(left=1, top=1, right=1, bottom=1),
            type=pypack2d.BorderType.SOLID,
            color="#000"
        ),
        # border=dict(
        #     size=1,
        #     type=pypack2d.BorderType.PIXELS_FROM_EDGE,
        #     color="#fff"
        # ),
        border_mode=pypack2d.BorderMode.NONE,

        atlas=dict(
            file_prefix="atlas",
            file_type="png",
            texture_mode="RGBA"
        )
    )

    stats = pypack2d.pack(pathname, atlasdir, pack_settings)

    print("Count images: %i efficiency : %4.2f " % (stats["count"], stats["efficiency"]))


def unpack(atlasdir, dirname):
    pypack2d.utils.clear_dir(dirname)
    count = 0
    for filename in glob.glob(atlasdir):
        datafile = open(filename, "r")
        data = datafile.read()
        data = json.loads(data)

        atlas = Image.open(data["path"])

        for image_data in data["images"]:
            uv = image_data["uv"]
            rotated = image_data["rotated"]
            image = pypack2d.utils.extract_image_from_atlas(atlas, uv, rotated)
            path = image_data["path"]
            _, image_filename = os.path.split(path)
            result_path = os.path.join(dirname, image_filename)
            image.save(result_path)
            count += 1
    print("Unpacked %d images" % count)


pack(["test/img/test/*.png"], "test/img/atlas")
unpack("test/img/atlas/*.json", "test/img/unpacked")
