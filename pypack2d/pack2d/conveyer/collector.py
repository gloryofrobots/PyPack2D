from pypack2d.pack2d.conveyer.unit import Unit,check_unit_forward_link_does_not_exist
from pypack2d.pack2d.conveyer.signal import SignalType

class Collector(Unit):
    def _on_init(self):
        self.connect(SignalType.END_PACK, self._on_end_to_pack)
        self.connect(SignalType.WASTE_INPUT, self._on_waste_input)
        self.result = None
        self.waste = []
        pass

    @check_unit_forward_link_does_not_exist
    def _on_end_to_pack(self, result):
        self.result = result
        return True
        pass

    def _on_waste_input(self, waste):
        self.waste.extend(waste)
        return True
        pass

    def get_result(self):
        return self.result
        pass

    def get_waste(self):
        return self.waste
        pass
    pass