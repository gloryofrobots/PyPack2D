from pypack2d.pack2d.conveyer.unit import Unit,check_unit_forward_link_exist
from pypack2d.pack2d.conveyer.signal import SignalType
from pypack2d.pack2d.conveyer.collector import Collector


class Conveyer(Unit):
    def _on_init(self):
        self.connect(SignalType.PREPARE_TO_PACK, self._onPrepareToPack)
        self.collector = Collector()
        self.waste = []
        pass

    @check_unit_forward_link_exist
    def _onPrepareToPack(self, dummy):
        self.push_unit(self.collector)
        return True
        pass

    def getResult(self):
        return self.collector.get_result()
        pass

    def getWaste(self):
        return self.collector.get_waste()
        pass
    pass