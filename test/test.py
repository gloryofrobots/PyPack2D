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

    pack_settings.update(custom)
    return pack_settings


class TestPack(unittest.TestCase):
    def setUp(self):
        pypack2d.utils.clear_dir(ATLAS_DIR)
        pypack2d.utils.clear_dir(UNPACKED_IMAGES_DIR)

    # def test_border_strict_solid(self):
    #     self.pack_unpack(dict(
    #         border_mode=pypack2d.BorderMode.STRICT,
    #         border=dict(
    #             rect=dict(left=1, top=1, right=1, bottom=1),
    #             type=pypack2d.BorderType.SOLID,
    #             color="#000"
    #         ),
    #     ))
    #
    # def test_border_strict_from_edge(self):
    #     self.pack_unpack(dict(
    #         border_mode=pypack2d.BorderMode.STRICT,
    #         border=dict(
    #             rect=dict(left=1, top=1, right=1, bottom=1),
    #             type=pypack2d.BorderType.PIXELS_FROM_EDGE,
    #         ),
    #     ))
    #
    # @unittest.expectedFailure
    # def test_border_auto_from_edge_failure(self):
    #     self.pack_unpack(dict(
    #         border_mode=pypack2d.BorderMode.AUTO,
    #         border=dict(
    #             rect=dict(left=1, top=1, right=1, bottom=1),
    #             type=pypack2d.BorderType.PIXELS_FROM_EDGE,
    #         ),
    #     ))
    #
    # def test_border_auto_from_edge(self):
    #     self.pack_unpack(dict(
    #         border_mode=pypack2d.BorderMode.AUTO,
    #         border=dict(
    #             size=1,
    #             type=pypack2d.BorderType.PIXELS_FROM_EDGE,
    #         ),
    #     ))

    # def test_shelf(self):
    #     self.pack_unpack(dict(
    #         algo=pypack2d.PackingAlgorithm.SHELF
    #     ))

    # def test_cell(self):
    #     self.pack_unpack(dict(
    #         algo=pypack2d.PackingAlgorithm.CELL
    #     ))

    def test_guillotine(self):
        self.pack_unpack(dict(
            algo=pypack2d.PackingAlgorithm.GUILLOTINE
        ))

    def test_guillotine2(self):
        self.pack_unpack(dict(
            algo=dict(type=pypack2d.PackingAlgorithm.GUILLOTINE, split=pypack2d.GuillotineSplitRule.SHORTER_AXIS)
        ))

    def pack_unpack(self, settings):
        self.pack(settings)
        self.unpack()

    def pack(self, custom_settings):
        pack_settings = create_settings(custom_settings)
        stats = pypack2d.pack(TEST_PATHNAME, ATLAS_DIR, pack_settings)
        print("\nCount images: %i efficiency : %4.2f " % (stats["count"], stats["efficiency"]))

    def unpack(self, save=False):
        self._unpack(ATLAS_META_PATHNAME, UNPACKED_IMAGES_DIR, save)

    def _unpack(self, atlasdir, dirname, save):
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


if __name__ == "__main__":
    unittest.main()

# Packer : self.validate(bin)
