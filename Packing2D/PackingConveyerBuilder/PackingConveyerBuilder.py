__author__ = 'human88998999877'
from Packing2D.PackingConveyer.Validator import Validator

class PackingConveyerBuilder(object):
    def build(self, conveyer, factory, settings):
        validator = Validator( settings.maxWidth, settings.maxHeight )
        conveyer.pushUnit(validator)

        self._onBuild(conveyer, factory, settings)
        pass

    def _onBuild(self, conveyer, factory, settings):
        pass
    pass
  