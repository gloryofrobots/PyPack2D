__author__ = 'human88998999877'

class UnitError(BaseException):
    pass

def checkUnitForwardLinkExist(fn):
    def wrap(self, *args, **kwargs):
        if self.nextUnit is None:
            raise UnitError("Unit doesn`t has forward link")
            pass
        fn(*args, **kwargs)
        pass

    return wrap
    pass

def checkUnitForwardLinkDoesNotExist(fn):
    def wrap(self, *args, **kwargs):
        if self.nextUnit is not None:
            raise UnitError("Unit has forward link. It must be None.")
            pass
        fn(*args, **kwargs)
        pass

    return wrap
    pass


class Unit(object):
    def __init__(self, *params):
        super(Unit, self).__init__()
        self.nextUnit = None
        self.slots = {}
        self._onInit(*params)
        pass

    def _onInit(self, *params):
        pass

    def connect(self, signalType, slot):
        self.slots[signalType] = slot
        pass

    def pushUnit(self, unit):
        if self.nextUnit is None:
            self.nextUnit = unit
            pass
        else:
            self.nextUnit.pushUnit(unit)
            pass
        pass

    def processSignal(self, signal):
        slot = self.getSlot(signal.type)
        if slot is not None:
            isNeedToContinue = slot(signal.data)
            if isNeedToContinue is False:
                return
                pass
            pass

        self._processNext(signal)
        pass

    def _processNext(self, signal):
        if self.nextUnit is None:
            return
            pass

        self.nextUnit.processSignal( signal )
        pass
    pass