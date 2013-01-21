__author__ = 'human88998999877'
from Packing2D.Enum.Enum import Enum

SortOrder = Enum("ASC", "DESC")

SortKey = Enum("AREA"
               ,"SHORTER_SIDE"
               ,"LONGER_SIDE"
               ,"PERIMETER"
               ,"SIDE_LENGTH_DIFFERENCE"
               ,"SIDE_RATIO")

PackingMode = Enum("ONLINE", "OFFLINE", "LOCAL_SEARCH")

PackingAlgorithm = Enum("SHELF", "SKYLINE", "GUILLOTINE")

PlaceHeuristic = Enum(  "NEXT_FIT"
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
                      , "BEST_FIT")

BinSizeMode = Enum("STRICT","AUTO_MINIMIZE")

PackingAlgorithmAbility = Enum("RECTANGLE_MERGE", "WASTE_MAP", "FLOOR_CEILING")

GuillotineSplitRule = Enum("SHORTER_AXIS"
                           , "LONGER_AXIS"
                           , "SHORTER_LEFTOVER_AXIS"
                           , "LONGER_LEFTOVER_AXIS"
                           , "MAX_AREA"
                           , "MIN_AREA")

BorderMode = Enum("NONE","STRICT","AUTO")


