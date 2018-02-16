from pypack2d.pack2d.conveyer.unit import Unit,check_unit_forward_link_exist
from pypack2d.pack2d.conveyer.signal import SignalType

class Rotator(Unit):
    def _on_init(self):
        self.connect(SignalType.PUSH_INPUT, self._on_push_input)
        pass

    @check_unit_forward_link_exist
    def _on_push_input(self, input):
        for bin in input:
            self.rotate(bin)

        return True
        pass

    def rotate(self, bin):
        self._on_rotate(bin)
        pass

    def _on_rotate(self, bin):
        raise NotImplementedError()
        pass
    pass

class RotatorUpRight(Rotator):
    def _on_rotate(self, bin):
        bin.rotate_up_right()
        pass
    pass

class RotatorSideWays(Rotator):
    def _on_rotate(self, bin):
        bin.rotate_side_ways()
        pass
    pass