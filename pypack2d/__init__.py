from pypack2d.pack.settings import (PackingMode, PlaceHeuristic, GuillotineSplitRule, ResizeMode,
                                      BorderMode, BorderType, PackingAlgorithm, PackingAlgorithmAbility,
                                      PackingSettings, RotateMode, SortKey, SortOrder)

from pypack2d.atlas import AtlasGenerator


def generator(destination_dir, packing_settings, *,
              file_prefix="atlas",
              texture_mode="RGBA",
              file_type="png",
              fill_color="#000"):
    settings = PackingSettings(**packing_settings)
    atlas_generator = AtlasGenerator(destination_dir, settings, file_prefix, file_type, texture_mode, fill_color)
    return atlas_generator


def generate(src_pathname, destination_dir,  packing_settings, **kwargs):
    gen = generator(destination_dir, packing_settings, **kwargs)
    if not isinstance(src_pathname, list):
        if not isinstance(src_pathname, str):
            raise TypeError("Expected source path name or list with path names")

        sources = [src_pathname]
    else:
        sources = src_pathname

    for src in sources:
        gen.add_glob(src)
    return gen.generate()

