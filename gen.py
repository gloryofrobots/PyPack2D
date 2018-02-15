
PlaceHeuristic = ["FIRST_FIT"
    , "BEST_WIDTH_FIT"
    , "BEST_HEIGHT_FIT"
    , "WORST_WIDTH_FIT"
    , "WORST_HEIGHT_FIT"
    , "BEST_AREA_FIT"
    , "BEST_SHORT_SIDE_FIT"
    , "BEST_LONG_SIDE_FIT"
    , "WORST_AREA_FIT"
    , "WORST_SHORT_SIDE_FIT"
    , "WORST_LONG_SIDE_FIT"
    , "BOTTOM_LEFT"
    , "BEST_FIT"]

BinSizeMode = ["STRICT", "MINIMIZE_MAXIMAL", "MINIMIZE_POW2", "MINIMIZE_POW2_MINIMIZE_LAST"]

PackingAlgorithmAbility = ["RECTANGLE_MERGE", "WASTE_MAP", "FLOOR_CEILING"]


GuillotineSplitRule = ["SHORTER_AXIS"
    , "LONGER_AXIS"
    , "SHORTER_LEFTOVER_AXIS"
    , "LONGER_LEFTOVER_AXIS"
    , "MAX_AREA"
    , "MIN_AREA"
    , "HORIZONTAL"
    , "VERTICAL"]

BorderMode = ["NONE", "STRICT", "AUTO"]
BorderType = ["PIXELS_FROM_EDGE", "SOLID"]

RotateMode = ["NONE", "UP_RIGHT", "SIDE_WAYS", "AUTO"]
def gen(name, fields):
    result = ["class %s(Enum):" % name]
    for f in fields:
        result.append("    %s = \"%s\"" % (f, f))
    result = "\n".join(result)
    print(result)
    print()


gen("PlaceHeuristic", PlaceHeuristic)
gen("BinSizeMode", BinSizeMode)
gen("PackingAlgorithmAbility", PackingAlgorithmAbility)
gen("GuillotineSplitRule", GuillotineSplitRule)
gen("BorderMode", BorderMode)
gen("BorderType", BorderType)
gen("RotateMode", RotateMode)

