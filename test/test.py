import unittest
import json
import os
import glob
import random
import itertools

import pypack2d
import pypack2d.utils
from PIL import Image

ATLAS_DIR = "img/atlas"
UNPACKED_IMAGES_DIR = "img/unpacked"
TEST_DIR = "img/test"

TEST_PATHNAME = os.path.join(TEST_DIR, "*.png")
ATLAS_META_PATHNAME = os.path.join(ATLAS_DIR, "*.json")


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


def create_settings(custom=None):
    if custom is None:
        custom = {}

    pack_settings = dict(
        callback=callback,
        # algo=dict(type=pypack2d.PackingAlgorithm.GUILLOTINE, split=pypack2d.GuillotineSplitRule.MAX_AREA),
        algo=pypack2d.PackingAlgorithm.MAX_RECTANGLES,
        heuristic=pypack2d.PlaceHeuristic.BEST_AREA_FIT,
        sort_order=pypack2d.SortOrder.ASC,
        sort_key=pypack2d.SortKey.SIDE_RATIO,
        resize_mode=pypack2d.ResizeMode.NONE,
        packing_mode=pypack2d.PackingMode.LOCAL_SEARCH,

        rotate_mode=pypack2d.RotateMode.SIDE_WAYS,
        max_width=64,
        max_height=64,
        border=dict(
            mode=pypack2d.BorderMode.STRICT,
            rect=dict(left=1, top=1, right=1, bottom=1),
            type=pypack2d.BorderType.SOLID,
            color="#000",
        ),
        # border=dict(
        #     size=1,
        #     type=pypack2d.BorderType.PIXELS_FROM_EDGE,
        #     color="#fff"
        # ),

        atlas=dict(
            file_prefix="atlas",
            file_type="png",
            texture_mode="RGBA"
        )
    )

    pack_settings.update(custom)
    return pack_settings


class TestPack(unittest.TestCase):
    def setUp(self):
        pypack2d.utils.clear_dir(ATLAS_DIR)
        pypack2d.utils.clear_dir(UNPACKED_IMAGES_DIR)

    def enum_choice(self, e):
        return random.choice(list(e))

    def test_border_strict_solid(self):
        self.pack_unpack(dict(
            border=dict(
                mode=pypack2d.BorderMode.STRICT,
                rect=dict(left=1, top=1, right=1, bottom=1),
                type=pypack2d.BorderType.SOLID,
                color="#000"
            ),
        ))

    def test_border_strict_from_edge(self):
        self.pack_unpack(dict(
            border=dict(
                mode=pypack2d.BorderMode.STRICT,
                rect=dict(left=1, top=1, right=1, bottom=1),
                type=pypack2d.BorderType.PIXELS_FROM_EDGE,
            ),
        ))

    @unittest.expectedFailure
    def test_border_auto_from_edge_failure(self):
        self.pack_unpack(dict(
            border=dict(
                mode=pypack2d.BorderMode.AUTO,
                rect=dict(left=1, top=1, right=1, bottom=1),
                type=pypack2d.BorderType.PIXELS_FROM_EDGE,
            ),
        ))

    def test_border_auto_from_edge(self):
        self.pack_unpack(dict(
            border=dict(
                mode=pypack2d.BorderMode.AUTO,
                size=1,
                type=pypack2d.BorderType.PIXELS_FROM_EDGE,
            ),
        ))

    def test_shelf(self):
        self.pack_unpack(dict(
            algo=pypack2d.PackingAlgorithm.SHELF
        ))

    def test_guillotine(self):
        self.pack_unpack(dict(
            algo=pypack2d.PackingAlgorithm.GUILLOTINE
        ))

    def test_guillotine2(self):
        self.pack_unpack(dict(
            algo=dict(type=pypack2d.PackingAlgorithm.GUILLOTINE, split=pypack2d.GuillotineSplitRule.SHORTER_AXIS)
        ))

    def test_batch(self):
        self._test_batch()

    def _test_batch(self, max_count=-1):
        algo_set = list(pypack2d.PackingAlgorithm)

        heuristic_set = list(pypack2d.PlaceHeuristic)
        order_set = list(pypack2d.SortOrder)
        key_set = list(pypack2d.SortKey)
        resize_set = list(pypack2d.ResizeMode)

        packing_set = list(pypack2d.PackingMode)
        rotate_set = list(pypack2d.RotateMode)
        sets = [algo_set, heuristic_set, order_set, key_set, resize_set, packing_set, rotate_set]

        product = itertools.product(*sets)
        unique = set(product)
        count = 0
        print("Total length of batch tests %d, performing %d tests" % (len(unique), max_count))
        if max_count < 0:
            max_count = len(unique)

        for s in unique:
            if count > max_count:
                break
            with self.subTest(s=s):
                if count % 300 == 0:
                    print("running test", count)
                algo, heuristic, order, key, resize, packing, rotate = s
                settings = dict(
                    algo=algo,
                    heuristic=heuristic,
                    sort_order=order,
                    sort_key=key,
                    resize_mode=resize,
                    packing_mode=packing,
                    rotate_mode=rotate,
                )
                self.pack_unpack(settings)
                count += 1

    def pack_unpack(self, settings):
        self.pack(settings)
        self.unpack(settings, False)

    def pack(self, custom_settings):
        pack_settings = create_settings(custom_settings)
        # print(pack_settings)
        stats = pypack2d.pack(TEST_PATHNAME, ATLAS_DIR, pack_settings)
        # print("\nAlgo: %s Count images: %i efficiency : %4.2f " % (
        #      pack_settings["algo"], stats["count"], stats["efficiency"])
        # )

    def unpack(self, settings, save=False):
        self._unpack(settings, ATLAS_META_PATHNAME, UNPACKED_IMAGES_DIR, save)

    def _unpack(self, settings, atlasdir, dirname, save):
        for filename in glob.glob(atlasdir):
            datafile = open(filename, "r")
            data = datafile.read()
            datafile.close()
            data = json.loads(data)

            atlas = Image.open(data["path"])

            for image_data in data["images"]:
                uv = image_data["uv"]
                rotated = image_data["rotated"]
                image = pypack2d.utils.extract_image_from_atlas(atlas, uv, rotated)
                path = image_data["path"]
                _, image_filename = os.path.split(path)
                old_image = Image.open(path)
                if save:
                    result_path = os.path.join(dirname, image_filename)
                    image.save(result_path)
                self.assertTrue(pypack2d.utils.are_images_equal(old_image, image),
                                "Extracted and source Images not equal atlas:%s, source:%s\n"
                                "Settings: %s"
                                % (filename, path, settings))


if __name__ == "__main__":
    unittest.main()

# Packer : self.validate(bin)
