class UnitError(BaseException):
    pass


def check_unit_forward_link_exist(fn):
    def wrap(self, *args, **kwargs):
        if self.next_unit is None:
            raise UnitError("Unit does not has forward link")

        return fn(self, *args, **kwargs)

    return wrap


def check_unit_forward_link_does_not_exist(fn):
    def wrap(self, *args, **kwargs):
        if self.next_unit is not None:
            raise UnitError("Unit has forward link. It must be None.")

        return fn(self, *args, **kwargs)

    return wrap


class Unit(object):
    def __init__(self, *params):
        super(Unit, self).__init__()
        self.next_unit = None
        self.slots = {}
        self._on_init(*params)

    def _on_init(self, *params):
        pass

    def connect(self, signal_type, slot):
        self.slots[signal_type] = slot

    def push_unit(self, unit):
        if self.next_unit is None:
            self.next_unit = unit

        else:
            self.next_unit.push_unit(unit)

    def get_slot(self, signal_type):
        if signal_type not in self.slots:
            return None

        return self.slots[signal_type]

    def process_signal(self, signal):
        slot = self.get_slot(signal.type)
        if slot is not None:
            is_need_to_continue = slot(signal.data)

            if is_need_to_continue is not True and is_need_to_continue is not False:
                raise BaseException("UNIT SLOT MUST RETURN BOOLEAN %s" % str(slot))

            if is_need_to_continue is False:
                return

        self._process_next(signal)

    def _process_next(self, signal):
        if self.next_unit is None:
            return

        self.next_unit.process_signal(signal)
