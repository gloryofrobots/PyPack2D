from pypack2d.pack2d.conveyer.filter import Filter
from pypack2d.pack2d.conveyer.control.control import PackingControl
from pypack2d.pack2d.conveyer.builder.builder import PackingConveyerBuilder


class PackingConveyerBuilderOnline(PackingConveyerBuilder):
    def _on_build(self, conveyer, factories, settings):
        _filter = Filter(1)
        conveyer.push_unit(_filter)
        packer = self.create_packer(factories, settings)
        control = PackingControl(packer, settings)
        conveyer.push_unit(control)
