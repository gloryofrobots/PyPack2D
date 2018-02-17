from pypack2d.pack.conveyer.unit import Unit, check_unit_forward_link_exist
from pypack2d.pack.conveyer.signal import SignalType
from pypack2d.pack.conveyer.collector import Collector


class Conveyer(Unit):
    def _on_init(self):
        self.connect(SignalType.PREPARE_TO_PACK, self._on_prepare_to_pack)
        self.collector = Collector()
        self.waste = []

    @check_unit_forward_link_exist
    def _on_prepare_to_pack(self, dummy):
        self.push_unit(self.collector)
        return True

    def get_result(self):
        return self.collector.get_result()

    def get_waste(self):
        return self.collector.get_waste()
