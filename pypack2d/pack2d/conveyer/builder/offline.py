from pypack2d.pack2d.conveyer.accumulator import Accumulator
from pypack2d.pack2d.conveyer.sorter import Sorter
from pypack2d.pack2d.conveyer.control.control import PackingControl
from pypack2d.pack2d.conveyer.builder.builder import PackingConveyerBuilder


class PackingConveyerBuilderOffline(PackingConveyerBuilder):
    def _on_build(self, conveyer, factories, settings):
        accumulator = Accumulator()
        conveyer.push_unit(accumulator)

        if settings.sort_order is not None:
            sorting = factories.sorting.create_instance(settings.sort_key)
            sorter = Sorter(sorting, settings.sort_order)
            conveyer.push_unit(sorter)

        packer = self.create_packer(factories, settings)
        control = PackingControl(packer, settings)
        conveyer.push_unit(control)
