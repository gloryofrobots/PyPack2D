from pypack2d.pack2d.conveyer.unit import Unit,check_unit_forward_link_exist
from pypack2d.pack2d.conveyer.signal import SignalType

class Sorter(Unit):
    def _on_init(self, sorting, order):
        self.order = order
        self.sorting = sorting
        self.connect(SignalType.PUSH_INPUT, self._on_push_input)
        pass

    @check_unit_forward_link_exist
    def _on_push_input(self, input):
        self.sorting.sort(input, self.order)
        return True
        pass
    pass
