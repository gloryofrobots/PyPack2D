import unittest
import json
import os
import glob

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


class TestPack(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # SIZES = [100, 60, 30, 180, 200, 10, 2, 140, 70, 50]
        # PRESETS = [(510, 10), (10, 510), (100, 100), (2, 10), (10, 2), (10, 10)]
        #
        # pypack2d.utils.clear_dir(TEST_DIR)
        # from test import image_gen
        # image_gen.generate(TEST_DIR, 100, sizes=SIZES, presets=PRESETS)
        pass

    def setUp(self):
        pypack2d.utils.clear_dir(ATLAS_DIR)
        pypack2d.utils.clear_dir(UNPACKED_IMAGES_DIR)

        self.pack_settings = dict(
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

    def pack(self, pathname, atlasdir, pack_settings):
        stats = pypack2d.pack(pathname, atlasdir, pack_settings)
        print("\nCount images: %i efficiency : %4.2f " % (stats["count"], stats["efficiency"]))

    def test_pack(self):
        self.pack(TEST_PATHNAME, ATLAS_DIR, self.pack_settings)

    def unpack(self, atlasdir, dirname, save=False):
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
                self.assertTrue(pypack2d.utils.are_images_equal(old_image, image),
                                "Extracted and source Images not equal atlas:%s, source:%s"
                                % (filename, path))
                if save:
                    result_path = os.path.join(dirname, image_filename)
                    image.save(result_path)

    def test_unpack(self):
        # self.pack(TEST_PATHNAME, ATLAS_DIR, self.pack_settings)
        self.unpack(ATLAS_META_PATHNAME, UNPACKED_IMAGES_DIR, True)


if __name__ == "__main__":
    unittest.main()

# Packer : self.validate(bin)
