from pypack2d.pack2d.conveyer.accumulator import Accumulator
from pypack2d.pack2d.conveyer.sorter import Sorter
from pypack2d.pack2d.conveyer.control.control_local_search import PackingControlLocalSearch
from pypack2d.pack2d.conveyer.builder.builder import PackingConveyerBuilder


class PackingConveyerBuilderLocalSearch(PackingConveyerBuilder):
    def _onBuild(self, conveyer, factory, settings):
        accumulator = Accumulator()
        conveyer.pushUnit(accumulator)

        if settings.sortOrder is not None:
            sorting = factory.getInstance(settings.sortKey)
            sorter = Sorter(sorting, settings.sortOrder)
            conveyer.pushUnit(sorter)
            pass

        packer = factory.createInstance(settings.packingAlgorithm)
        control = PackingControlLocalSearch(packer, factory, settings)
        conveyer.pushUnit(control)
        pass

    pass
