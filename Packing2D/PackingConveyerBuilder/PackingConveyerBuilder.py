__author__ = 'human88998999877'
from Packing2D.PackingConveyer.Validator import Validator
from Packing2D import BinSizeMode

class PackingConveyerBuilder(object):
    def build(self, conveyer, factory, settings):
        validator = Validator( settings.maxWidth, settings.maxHeight )
        conveyer.pushUnit(validator)

        self._onBuild(conveyer, factory, settings)
        if settings.binSizeMode == None or settings.binSizeMode == BinSizeMode.STRICT:
            return
            pass

        shifter = factory.getInstance(settings.binSizeMode)
        conveyer.pushUnit(shifter)
        pass

    def _onBuild(self, conveyer, factory, settings):
        pass
    pass
  