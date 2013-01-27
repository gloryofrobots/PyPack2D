__author__ = 'human88998999877'

class PackingSettings(object):
    def __init__(self
                 , PackingAlgorithm
                 , PlaceHeuristic
                 , PackingMode
                 , SortOrder
                 , SortKey
                 , BinSizeMode
                 , PackingAlgorithmAbility
                 , MaxWidth
                 , MaxHeight
                 , Border
                 , BorderMode
                 , RotateMode):
        super(PackingSettings, self).__init__()

        self.packingAlgorithm = PackingAlgorithm
        self.placeHeuristic = PlaceHeuristic
        self.sortOrder = SortOrder
        self.sortKey = SortKey
        self.binSizeMode = BinSizeMode
        self.packingMode = PackingMode
        self.packingAlgorithmAbility = PackingAlgorithmAbility

        self.rotateMode = RotateMode
        self.maxWidth = MaxWidth
        self.maxHeight = MaxHeight
        self.border = Border
        self.borderMode = BorderMode
        pass
    pass

class PackingSettingsGuillotine(PackingSettings):
    def __init__(self
                 , PackingAlgorithm
                 , PlaceHeuristic
                 , PackingMode
                 , SortOrder
                 , SortKey
                 , BinSizeMode
                 , PackingAlgorithmAbility
                 , MaxWidth
                 , MaxHeight
                 , Border
                 , BorderMode
                 , RotateMode
                 , SplitRule):

        super(PackingSettingsGuillotine, self).__init__(PackingAlgorithm
                                                        , PlaceHeuristic
                                                        , PackingMode
                                                        , SortOrder
                                                        , SortKey
                                                        , BinSizeMode
                                                        , PackingAlgorithmAbility
                                                        , MaxWidth
                                                        , MaxHeight
                                                        , Border
                                                        , BorderMode
                                                        , RotateMode)
        self.splitRule = SplitRule
        pass
    pass