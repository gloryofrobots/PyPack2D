from pypack2d.pack2d.PackingConveyer.Accumulator import Accumulator
from pypack2d.pack2d.PackingConveyer.Sorter import Sorter
from pypack2d.pack2d.PackingConveyer.PackingControl.PackingControlLocalSearch import PackingControlLocalSearch
from pypack2d.pack2d.PackingConveyerBuilder.PackingConveyerBuilder import PackingConveyerBuilder


class PackingConveyerBuilderLocalSearch(PackingConveyerBuilder):
    def _onBuild(self, conveyer, factory, settings):
        accumulator = Accumulator()
        conveyer.pushUnit( accumulator )

        if settings.sortOrder is not None:
            sorting = factory.getInstance(settings.sortKey)
            sorter = Sorter(sorting, settings.sortOrder)
            conveyer.pushUnit( sorter )
            pass

        packer = factory.createInstance(settings.packingAlgorithm)
        control = PackingControlLocalSearch(packer, factory, settings)
        conveyer.pushUnit(control)
        pass
    pass