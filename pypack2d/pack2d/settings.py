from enum import Enum


class SortOrder(Enum):
    ASC = "ASC"
    DESC = "DESC"


class SortKey(Enum):
    AREA = "AREA"
    WIDTH = "WIDTH"
    HEIGHT = "HEIGHT"
    SHORTER_SIDE = "SHORTER_SIDE"
    LONGER_SIDE = "LONGER_SIDE"
    PERIMETER = "PERIMETER"
    SIDE_LENGTH_DIFFERENCE = "SIDE_LENGTH_DIFFERENCE"
    SIDE_RATIO = "SIDE_RATIO"


class PackingMode(Enum):
    ONLINE = "ONLINE"
    OFFLINE = "OFFLINE"
    LOCAL_SEARCH = "LOCAL_SEARCH"


class PackingAlgorithm(Enum):
    SHELF = "SHELF"
    CELL = "CELL"
    GUILLOTINE = "GUILLOTINE"
    MAX_RECTANGLES = "MAX_RECTANGLES"


class PlaceHeuristic(Enum):
    FIRST_FIT = "FIRST_FIT"
    BEST_WIDTH_FIT = "BEST_WIDTH_FIT"
    BEST_HEIGHT_FIT = "BEST_HEIGHT_FIT"
    WORST_WIDTH_FIT = "WORST_WIDTH_FIT"
    WORST_HEIGHT_FIT = "WORST_HEIGHT_FIT"
    BEST_AREA_FIT = "BEST_AREA_FIT"
    BEST_SHORT_SIDE_FIT = "BEST_SHORT_SIDE_FIT"
    BEST_LONG_SIDE_FIT = "BEST_LONG_SIDE_FIT"
    WORST_AREA_FIT = "WORST_AREA_FIT"
    WORST_SHORT_SIDE_FIT = "WORST_SHORT_SIDE_FIT"
    WORST_LONG_SIDE_FIT = "WORST_LONG_SIDE_FIT"
    BOTTOM_LEFT = "BOTTOM_LEFT"
    BEST_FIT = "BEST_FIT"


class BinSizeMode(Enum):
    STRICT = "STRICT"
    MINIMIZE_MAXIMAL = "MINIMIZE_MAXIMAL"
    MINIMIZE_POW2 = "MINIMIZE_POW2"
    MINIMIZE_POW2_MINIMIZE_LAST = "MINIMIZE_POW2_MINIMIZE_LAST"


class PackingAlgorithmAbility(Enum):
    RECTANGLE_MERGE = "RECTANGLE_MERGE"
    WASTE_MAP = "WASTE_MAP"
    FLOOR_CEILING = "FLOOR_CEILING"


class GuillotineSplitRule(Enum):
    SHORTER_AXIS = "SHORTER_AXIS"
    LONGER_AXIS = "LONGER_AXIS"
    SHORTER_LEFTOVER_AXIS = "SHORTER_LEFTOVER_AXIS"
    LONGER_LEFTOVER_AXIS = "LONGER_LEFTOVER_AXIS"
    MAX_AREA = "MAX_AREA"
    MIN_AREA = "MIN_AREA"
    HORIZONTAL = "HORIZONTAL"
    VERTICAL = "VERTICAL"


class BorderMode(Enum):
    NONE = "NONE"
    STRICT = "STRICT"
    AUTO = "AUTO"


class BorderType(Enum):
    PIXELS_FROM_EDGE = "PIXELS_FROM_EDGE"
    SOLID = "SOLID"


class RotateMode(Enum):
    NONE = "NONE"
    UP_RIGHT = "UP_RIGHT"
    SIDE_WAYS = "SIDE_WAYS"
    AUTO = "AUTO"


class PackingSettings(object):
    def __init__(self, *,
                 algo=PackingAlgorithm.MAX_RECTANGLES,
                 heuristic=PlaceHeuristic.BEST_AREA_FIT,
                 sort_key=SortKey.WIDTH,
                 sort_order=SortOrder.ASC,
                 bin_size_mode=BinSizeMode.MINIMIZE_MAXIMAL,
                 packing_mode=PackingMode.ONLINE,
                 rotate_mode=RotateMode.AUTO,
                 max_width=1024,
                 max_height=1024,
                 border=None,
                 border_mode=None,
                 border_size=None,
                 split_rule=None,
                 debug=False
                 ):
        super(PackingSettings, self).__init__()
        self.packing_algo = algo
        self.place_heuristic = heuristic
        self.sort_key = sort_key
        self.sort_order = sort_order
        self.bin_size_mode = bin_size_mode
        self.packing_mode = packing_mode

        self.rotate_mode = rotate_mode
        self.max_width = max_width
        self.max_height = max_height
        self.border = border
        self.border_mode = border_mode
        self.border_size = border_size

        self.split_rule = split_rule
        self.debug = debug
        pass

    pass
