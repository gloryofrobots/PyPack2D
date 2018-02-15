from pypack2d.pack2d.PackingConveyer.Filter import Filter
from pypack2d.pack2d.PackingConveyer.PackingControl.PackingControl import PackingControl
from pypack2d.pack2d.PackingConveyerBuilder.PackingConveyerBuilder import PackingConveyerBuilder


class PackingConveyerBuilderOnline(PackingConveyerBuilder):
    def _onBuild(self, conveyer, factory, settings):
        filter = Filter(1)
        conveyer.pushUnit( filter )
        packer = factory.getInstance(settings.packingAlgorithm)
        control = PackingControl(packer, factory, settings)
        conveyer.pushUnit(control)
        pass
    pass

