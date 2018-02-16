from pypack2d.pack2d.conveyer.validator import Validator
from pypack2d.pack2d import BinSizeMode, RotateMode


class PackingConveyerBuilder(object):
    def build(self, conveyer, factory, settings):
        if settings.rotateMode == RotateMode.UP_RIGHT or settings.rotateMode == RotateMode.SIDE_WAYS:
            rotator = factory.getInstance(settings.rotateMode)
            conveyer.push_unit(rotator)
            pass

        validator = Validator(settings.maxWidth, settings.maxHeight)
        conveyer.push_unit(validator)

        self._on_build(conveyer, factory, settings)
        if settings.binSizeMode == None or settings.binSizeMode == BinSizeMode.STRICT:
            return
            pass

        shifter = factory.getInstance(settings.binSizeMode)
        conveyer.push_unit(shifter)
        pass

    def _on_build(self, conveyer, factory, settings):
        pass

    pass
