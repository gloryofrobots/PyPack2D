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
    def __init__(self):
        super(PackingSettings, self).__init__()
        self.packing_algo = None
        self.place_heuristic = None
        self.sort_order = None
        self.sort_key = None
        self.bin_size_mode = None
        self.packing_mode = None

        self.rotate_mode = None
        self.max_width = None
        self.max_height = None
        self.border = None
        self.border_mode = None
        self.debug = False
        self.border_size = None

        self.split_rule = None
        pass

    pass
