from pypack2d.pack.conveyer.filter import Filter
from pypack2d.pack.conveyer.control.control import PackingControl
from pypack2d.pack.conveyer.builder.builder import PackingConveyerBuilder


class PackingConveyerBuilderOnline(PackingConveyerBuilder):
    def _on_build(self, conveyer, factories, settings):
        _filter = Filter(1)
        conveyer.push_unit(_filter)
        packer = factories.packer.create_instance(settings.packing_algo, factories, settings)
        control = PackingControl(packer, settings)
        conveyer.push_unit(control)
