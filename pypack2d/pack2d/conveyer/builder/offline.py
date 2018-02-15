from pypack2d.pack2d.conveyer.accumulator import Accumulator
from pypack2d.pack2d.conveyer.sorter import Sorter
from pypack2d.pack2d.conveyer.control.control import PackingControl
from pypack2d.pack2d.conveyer.builder.builder import PackingConveyerBuilder


class PackingConveyerBuilderOffline(PackingConveyerBuilder):
    def _onBuild(self, conveyer, factory, settings):
        accumulator = Accumulator()
        conveyer.pushUnit(accumulator)

        if settings.sortOrder is not None:
            sorting = factory.getInstance(settings.sortKey)
            sorter = Sorter(sorting, settings.sortOrder)
            conveyer.pushUnit(sorter)
            pass

        packer = factory.getInstance(settings.packingAlgorithm)
        control = PackingControl(packer, factory, settings)
        conveyer.pushUnit(control)
        pass

    pass
