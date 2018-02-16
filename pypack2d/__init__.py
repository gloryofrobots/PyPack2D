from pypack2d.pack2d.settings import (PackingMode, PlaceHeuristic, GuillotineSplitRule, BinSizeMode,
                                      BorderMode, BorderType, PackingAlgorithm, PackingAlgorithmAbility,
                                      PackingSettings, RotateMode, SortKey, SortOrder)

from pypack2d.atlas import AtlasGenerator

def generator(destination_dir, packing_settins, **kwargs):
    settings = PackingSettings(**packing_settins)
    atlas_generator = AtlasGenerator(destination_dir, settings, **kwargs)
    return atlas_generator


