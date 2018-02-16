from pypack2d.pack2d.conveyer.validator import Validator
from pypack2d.pack2d.settings import BinSizeMode, RotateMode


class PackingConveyerBuilder(object):
    def build(self, conveyer, factory, settings):
        if settings.rotate_mode == RotateMode.UP_RIGHT or settings.rotate_mode == RotateMode.SIDE_WAYS:
            rotator = factory.create_instance(settings.rotate_mode)
            conveyer.push_unit(rotator)
            pass

        validator = Validator(settings.max_width, settings.max_height)
        conveyer.push_unit(validator)

        self._on_build(conveyer, factory, settings)
        if settings.bin_size_mode == None or settings.bin_size_mode == BinSizeMode.STRICT:
            return
            pass

        shifter = factory.create_instance(settings.bin_size_mode)
        conveyer.push_unit(shifter)
        pass

    def _on_build(self, conveyer, factory, settings):
        pass

    pass
