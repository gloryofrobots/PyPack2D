class UnitError(BaseException):
    pass


def checkUnitForwardLinkExist(fn):
    def wrap(self, *args, **kwargs):
        if self.nextUnit is None:
            raise UnitError("Unit doesn`t has forward link")
            pass

        return fn(self, *args, **kwargs)
        pass

    return wrap
    pass


def checkUnitForwardLinkDoesNotExist(fn):
    def wrap(self, *args, **kwargs):
        if self.nextUnit is not None:
            raise UnitError("Unit has forward link. It must be None.")
            pass

        return fn(self, *args, **kwargs)
        pass

    return wrap
    pass


class Unit(object):
    def __init__(self, *params):
        super(Unit, self).__init__()
        self.nextUnit = None
        self.slots = {}
        self._on_init(*params)
        pass

    def _on_init(self, *params):
        pass

    def connect(self, signalType, slot):
        self.slots[signalType] = slot
        pass

    def push_unit(self, unit):
        if self.nextUnit is None:
            self.nextUnit = unit
            pass
        else:
            self.nextUnit.push_unit(unit)
            pass
        pass

    def get_slot(self, signalType):
        if signalType not in self.slots:
            return None
            pass

        return self.slots[signalType]
        pass

    def process_signal(self, signal):
        slot = self.get_slot(signal.type)
        if slot is not None:
            isNeedToContinue = slot(signal.data)

            if isNeedToContinue is not True and isNeedToContinue is not False:
                raise BaseException("UNIT SLOT MUST RETURN BOOLEAN %s" % str(slot))
                pass

            if isNeedToContinue is False:
                return
                pass
            pass

        self._process_next(signal)
        pass

    def _process_next(self, signal):
        if self.nextUnit is None:
            return
            pass

        self.nextUnit.process_signal(signal)
        pass

    pass
