from pypack2d.pack2d.packer.bin_set import BinSet
from pypack2d.pack2d.settings import BorderMode, RotateMode
from pypack2d.pack2d.border import Border


class BinPackerError(BaseException):
    pass


class ManualAbort(object):
    def __init__(self):
        super(ManualAbort, self).__init__()
        self.debugCount = 0
        pass

    def abort_on_count(self, limit):
        if self.debugCount >= limit:
            raise BaseException()
            pass

        self.debugCount += 1
        pass

    pass


class BinPacker(object):
    def __init__(self):
        super(BinPacker, self).__init__()
        pass

    def initialise(self, factory, settings):
        self.settings = settings
        self.heuristic = factory.create_instance(settings.place_heuristic)

        self.settings = settings
        self._on_init(factory, settings)
        pass

    def set_size(self, width, height):
        self.max_width = width
        self.max_height = height

        if self.settings.border_mode == BorderMode.AUTO:
            self.max_height += self.settings.border_size * 2
            self.max_width += self.settings.border_size * 2
            pass

        self.binSet = BinSet(self.max_width, self.max_height)
        self._on_set_size()
        pass

    def _on_set_size(self):
        raise NotImplementedError()
        pass

    def _on_init(self, factory, settings):
        pass

    def pack_bin(self, bin):
        self.set_border(bin)

        if self._on_pack_bin(bin) is False:
            return False
            pass

        if self.settings.debug is True:
            self.validate(bin)
            self.on_debug()
            pass

        self.binSet.add(bin)
        return True
        pass

    def validate(self, bin):
        for binCheck in self.binSet:
            if binCheck.is_intersect(bin) is True:
                raise BinPackerError("Validate Error bins are intersected : %s with %s" % (binCheck, bin))
                pass
            pass
        pass

    def on_debug(self):
        self._on_debug()
        pass

    def _on_debug(self):
        pass

    def _on_pack_bin(self, bin):
        raise NotImplementedError()
        pass

    def set_border(self, bin):
        if self.settings.border_mode == BorderMode.NONE:
            return
            pass
        elif self.settings.border_mode == BorderMode.STRICT:
            border = Border(border=self.settings.border)
            bin.set_border(border)
            pass
        elif self.settings.border_mode == BorderMode.AUTO:
            border = Border(border_size=self.settings.border_size, type=self.settings.border.type,
                            color=self.settings.border.color)
            bin.set_border(border)
            pass
        pass

    def normalise_border(self):

        realWidth = self.max_width - self.settings.border_size * 2
        realHeight = self.max_height - self.settings.border_size * 2
        for bin in self.binSet:
            border = bin.getBorder()
            if bin.top is 0:
                border.top = 0
                pass
            else:
                bin.set_coord(bin.left, bin.top - self.settings.border_size)
                pass
            if bin.left is 0:
                border.left = 0
                pass
            else:
                bin.set_coord(bin.left - self.settings.border_size, bin.top)
                pass
            if bin.right > realWidth:
                border.right = 0
                pass
            if bin.bottom > realHeight:
                border.bottom = 0
                pass
            pass

            self.binSet.set_size(realWidth, realHeight)
            pass
        pass

    def flush(self):
        if self.settings.border_mode == BorderMode.AUTO:
            self.normalise_border()
            pass

        result = self.binSet
        self.binSet = BinSet(self.max_width, self.max_height)
        self._on_flush()
        self._on_set_size()
        return result
        pass

    def _on_flush(self):
        pass

    pass
