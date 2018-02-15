from pypack2d.pack2d.conveyer.unit import Unit,checkUnitForwardLinkExist
from pypack2d.pack2d.conveyer.signal import SignalType

class Rotator(Unit):
    def _onInit(self):
        self.connect(SignalType.PUSH_INPUT, self._onPushInput)
        pass

    @checkUnitForwardLinkExist
    def _onPushInput(self, input):
        for bin in input:
            self.rotate(bin)

        return True
        pass

    def rotate(self, bin):
        self._onRotate(bin)
        pass

    def _onRotate(self, bin):
        raise NotImplementedError()
        pass
    pass

class RotatorUpRight(Rotator):
    def _onRotate(self, bin):
        bin.rotateUpRight()
        pass
    pass

class RotatorSideWays(Rotator):
    def _onRotate(self, bin):
        bin.rotateSideWays()
        pass
    pass