from pypack2d.pack2d.conveyer.filter import Filter
from pypack2d.pack2d.conveyer.control.control import PackingControl
from pypack2d.pack2d.conveyer_builder.builder import PackingConveyerBuilder


class PackingConveyerBuilderOnline(PackingConveyerBuilder):
    def _onBuild(self, conveyer, factory, settings):
        filter = Filter(1)
        conveyer.pushUnit(filter)
        packer = factory.getInstance(settings.packingAlgorithm)
        control = PackingControl(packer, factory, settings)
        conveyer.pushUnit(control)
        pass

    pass
