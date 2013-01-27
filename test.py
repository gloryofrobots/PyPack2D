__author__ = 'human88998999877'

from Packing2D.PackingSettings import PackingSettings,PackingSettingsGuillotine
import os
from Packing2D import GuillotineSplitRule,BinSizeMode,BorderMode,\
    PackingAlgorithm,PackingAlgorithmAbility,PackingMode,PlaceHeuristic,SortKey,SortOrder,RotateMode
from Atlas.AtlasImage import AtlasImage
from Atlas.AtlasGenerator import AtlasGenerator

#   def __init__(self
#                 , PackingAlgorithm
#                 , PlaceHeuristic
#                 , PackingMode = None
#                 , SortOrder = None
#                 , SortKey = None
#                 , BinSizeMode = None
#                 , PackingAlgorithmAbility = None
#                 , MaxWidth = None
#                 , MaxHeight = None
#                 , Border = None
#                 , BorderMode = None
#                 , IsRotate = None ):


"""
SortKey = Enum("AREA"
               ,"WIDTH"
               ,"HEIGHT"
               ,"SHORTER_SIDE"
               ,"LONGER_SIDE"
               ,"PERIMETER"
               ,"SIDE_LENGTH_DIFFERENCE"
               ,"SIDE_RATIO")

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


                      GuillotineSplitRule = Enum("SHORTER_AXIS"
                           , "LONGER_AXIS"
                           , "SHORTER_LEFTOVER_AXIS"
                           , "LONGER_LEFTOVER_AXIS"
                           , "MAX_AREA"
                           , "MIN_AREA"
                           , "HORIZONTAL"
                           , "VERTICAL")
"""
def createAtlasInDirectory(dir):
    generator = AtlasGenerator()
    settings = PackingSettingsGuillotine(PackingAlgorithm.GUILLOTINE, PlaceHeuristic.NEXT_FIT
                               , PackingMode.OFFLINE, SortOrder.DESC, SortKey.SHORTER_SIDE
                               , BinSizeMode.STRICT, None, 2048, 2048, (0,0,0,0), BorderMode.STRICT
                               , RotateMode.HEIGHT_LONGER , GuillotineSplitRule.MIN_AREA  )


    dirPath = "D:\\Projects\\PyPack2D\\input\\coocked\\"
    relativeFileName = 'atlas'
    texMode = "RGBA"
    atlasType = "png"
    fillColor = (128,128,128,255)
    generator.initialise(settings,dirPath, relativeFileName, texMode, atlasType, fillColor)

    for root, dirs, files in os.walk(dir, topdown=False):
        for name in files:
            fileName = os.path.join(root, name)
            image = AtlasImage(fileName)
            generator.addImage(image)
            pass
        pass

    generator.generate()
    pass

createAtlasInDirectory("D:\\Projects\\PyPack2D\\input\\test\\")