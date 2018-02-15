from pypack2d.pack2d.conveyer.unit import Unit,checkUnitForwardLinkExist
from pypack2d.pack2d.conveyer.signal import SignalType

class Sorter(Unit):
    def _onInit(self, sorting, order):
        self.order = order
        self.sorting = sorting
        self.connect(SignalType.PUSH_INPUT, self._onPushInput)
        pass

    @checkUnitForwardLinkExist
    def _onPushInput(self, input):
        self.sorting.sort(input, self.order)
        return True
        pass
    pass
