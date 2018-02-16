from pypack2d.pack2d.conveyer.filter import Filter
from pypack2d.pack2d.conveyer.control.control import PackingControl
from pypack2d.pack2d.conveyer.builder.builder import PackingConveyerBuilder


class PackingConveyerBuilderOnline(PackingConveyerBuilder):
    def _on_build(self, conveyer, factory, settings):
        filter = Filter(1)
        conveyer.push_unit(filter)
        packer = factory.create_instance(settings.packingAlgorithm)
        control = PackingControl(packer, factory, settings)
        conveyer.push_unit(control)
        pass

    pass
