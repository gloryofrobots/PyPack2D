from pypack2d.pack2d.conveyer.validator import Validator
from pypack2d.pack2d.settings import ResizeMode, RotateMode


class PackingConveyerBuilder(object):
    def build(self, conveyer, factories, settings):
        if settings.rotate_mode == RotateMode.UP_RIGHT or settings.rotate_mode == RotateMode.SIDE_WAYS:
            rotator = factories.rotator.create_instance(settings.rotate_mode)
            conveyer.push_unit(rotator)

        validator = Validator(settings.max_width, settings.max_height)
        conveyer.push_unit(validator)

        self._on_build(conveyer, factories, settings)
        if settings.resize_mode is None or settings.resize_mode == ResizeMode.NONE:
            return

        shifter = factories.size_shifter.create_instance(settings.resize_mode)
        conveyer.push_unit(shifter)

    def _on_build(self, conveyer, factories, settings):
        pass
