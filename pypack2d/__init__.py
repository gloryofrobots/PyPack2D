from pypack2d.pack2d.settings import (PackingMode, PlaceHeuristic, GuillotineSplitRule, ResizeMode,
                                      BorderMode, BorderType, PackingAlgorithm, PackingAlgorithmAbility,
                                      PackingSettings, RotateMode, SortKey, SortOrder)

from pypack2d.atlas import AtlasGenerator
from pypack2d import utils


def pack(src_pathname, destination_dir, settings=None, **kwargs):
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


def json_writer(atlas):
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
