import pypack2d
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


def clear_dir(dirname):
    for filename in glob.glob(dirname + "/*.*"):
        os.remove(filename)

def pack(pathname, atlasdir):
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
        max_width=128,
        max_height=128,
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
        border_mode=pypack2d.BorderMode.STRICT,

        atlas=dict(
            file_prefix="atlas",
            file_type="png",
            texture_mode="RGBA"
        )
    )

    stats = pypack2d.pack(pathname, atlasdir, pack_settings)

    print("Count images: %i efficiency : %4.2f " % (stats["count"], stats["efficiency"]))


def extract_image(atlas, uv, rotated):
    width, height = atlas.size
    # if rotated:
    #     width,height = height, width
    uv_left, uv_top, uv_right, uv_bottom = uv
    left = width * uv_left
    top = height * uv_top
    right = width * uv_right
    bottom = height * uv_bottom
    image = atlas.crop((left, top, right, bottom))
    image.load()
    # if rotated:
    #     image = image.rotate(-90)
    return image


def equal(im1, im2):
    from PIL import ImageChops
    # check equality in 2 ways
    # it is redundant but I want to be sure
    check1 = ImageChops.difference(im1, im2).getbbox() is None
    check2 = im1.tobytes() == im2.tobytes()
    return check1 is True and check2 is True


def unpack(atlasdir, dirname):
    for filename in glob.glob(atlasdir):
        datafile = open(filename, "r")
        data = datafile.read()
        data = json.loads(data)

        atlas = Image.open(data["path"])

        for image_data in data["images"]:
            uv = image_data["uv"]
            rotated = image_data["rotated"]
            image = extract_image(atlas, uv, rotated)
            path = image_data["path"]
            _, image_filename = os.path.split(path)
            result_path = os.path.join(dirname, image_filename)
            old_image = Image.open(path)
            if not equal(old_image, image):
                print("ERROR %s, %s" % (filename, result_path))
                # old_image.show()
                # image.show()
                # return
            image.save(result_path)


ATLAS_DIR = "img/atlas"
UNPACKED_IMAGES_DIR = "img/unpacked"
clear_dir(ATLAS_DIR)
clear_dir(UNPACKED_IMAGES_DIR)

pack(["img/test/*.png"], ATLAS_DIR)
unpack("img/atlas/*.json", UNPACKED_IMAGES_DIR)
