__author__ = 'human88998999877'

class PackingSettings(object):
    def __init__(self
                 , PackingAlgorithm
                 , PlaceHeuristic
                 , PackingMode = None
                 , SortOrder = None
                 , SortKey = None
                 , BinSizeMode = None
                 , PackingAlgorithmAbility = None
                 , MaxWidth = None
                 , MaxHeight = None
                 , Border = None
                 , BorderMode = None
                 , IsRotate = None ):
        super(PackingSettings, self).__init__()

        self.packingAlgorithm = PackingAlgorithm
        self.placeHeuristic = PlaceHeuristic
        self.sortOrder = SortOrder
        self.sortKey = SortKey
        self.binSizeMode = BinSizeMode
        self.packingMode = PackingMode
        self.packingAlgorithmAbility = PackingAlgorithmAbility

        self.isRotate = IsRotate
        self.maxWidth = MaxWidth
        self.maxHeight = MaxHeight
        self.border = Border
        self.borderMode = BorderMode
        pass
    pass

class PackingSettingsGuillotine(PackingSettings):
    def __init__(self, PackingAlgorithm, PlaceHeuristic, SplitRule, SortOrder = None
                 , SortKey = None, BinSizeMode = None, PackingAlgorithmAbility = None):

        super(PackingSettingsGuillotine, self).__init__(PackingAlgorithm, PlaceHeuristic, SortOrder
                                                  ,SortKey, BinSizeMode, PackingAlgorithmAbility)

        self.splitRule = SplitRule
        pass
    pass