from pypack2d.pack2d.conveyer.accumulator import Accumulator
from pypack2d.pack2d.conveyer.sorter import Sorter
from pypack2d.pack2d.conveyer.control.control_local_search import PackingControlLocalSearch
from pypack2d.pack2d.conveyer.builder.builder import PackingConveyerBuilder


class PackingConveyerBuilderLocalSearch(PackingConveyerBuilder):
    def _on_build(self, conveyer, factory, settings):
        accumulator = Accumulator()
        conveyer.push_unit(accumulator)

        if settings.sort_order is not None:
            sorting = factory.create_instance(settings.sort_key)
            sorter = Sorter(sorting, settings.sort_order)
            conveyer.push_unit(sorter)

        packer = factory.createInstance(settings.packingAlgorithm)
        control = PackingControlLocalSearch(packer, factory, settings)
        conveyer.push_unit(control)
