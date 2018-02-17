from pypack2d.pack.settings import (PackingMode, PlaceHeuristic, GuillotineSplitRule, ResizeMode,
                                    BorderMode, BorderType, PackingAlgorithm, PackingAlgorithmAbility,
                                    PackingSettings, RotateMode, SortKey, SortOrder)

from pypack2d.atlas import AtlasGenerator


def generate(src_pathname, destination_dir, settings=None, **kwargs):
    if settings is None:
        packing_settings = kwargs
    else:
        packing_settings = settings

    atlas_settings = packing_settings.pop("atlas", {})
    settings = PackingSettings(**packing_settings)
    gen = AtlasGenerator(destination_dir, settings, **atlas_settings)
    if not isinstance(src_pathname, list):
        if not isinstance(src_pathname, str):
            raise TypeError("Expected source path name or list with path names")

        sources = [src_pathname]
    else:
        sources = src_pathname

    for src in sources:
        gen.add_glob(src)
    return gen.generate()



