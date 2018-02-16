from pypack2d.pack2d.packer.bin_set import BinSet
from pypack2d.pack2d.settings import BorderMode, RotateMode, BorderType
from pypack2d.pack2d.border import Border


class BinPackerError(Exception):
    pass

class AbortError(Exception):
    pass

class ManualAbort(object):
    def __init__(self):
        super(ManualAbort, self).__init__()
        self.debugCount = 0

    def abort_on_count(self, limit):
        if self.debugCount >= limit:
            raise AbortError("Abort on count")

        self.debugCount += 1


class BinPacker(object):
    def __init__(self):
        super(BinPacker, self).__init__()

    def initialise(self, factory, settings):
        self.settings = settings
        self.heuristic = factory.create_instance(settings.place_heuristic)

        self.settings = settings
        self._on_init(factory, settings)

    def set_size(self, width, height):
        self.max_width = width
        self.max_height = height

        if self.settings.border_mode == BorderMode.AUTO:
            self.max_height += self.settings.border_size * 2
            self.max_width += self.settings.border_size * 2

        self.binSet = BinSet(self.max_width, self.max_height)
        self._on_set_size()

    def _on_set_size(self):
        raise NotImplementedError()

    def _on_init(self, factory, settings):
        pass

    def pack_bin(self, bin):
        self.set_border(bin)

        if self._on_pack_bin(bin) is False:
            return False

        if self.settings.debug is True:
            self.validate(bin)
            self.on_debug()

        self.binSet.add(bin)
        return True

    def validate(self, bin):
        for binCheck in self.binSet:
            if binCheck.is_intersect(bin) is True:
                raise BinPackerError("Validate Error bins are intersected : %s with %s" % (binCheck, bin))

    def on_debug(self):
        self._on_debug()

    def _on_debug(self):
        pass

    def _on_pack_bin(self, bin):
        raise NotImplementedError()

    def set_border(self, bin):
        border = self.settings.border
        border_mode = self.settings.border_mode
        if border is None or border_mode == BorderMode.NONE:
            return
        border_type = border.get("type", BorderType.SOLID)
        border_color = border.get("color", "#000")

        if "rect" in border:
            bin_border = Border.from_rect(border_type, border_color, border["rect"])
            if border_mode != BorderMode.STRICT:
                raise BinPackerError("Border rect can be specified only for STRICT border mode")
        elif "size" in border:
            bin_border = Border.from_size(border_type, border_color, border["size"])
        else:
            raise BinPackerError("border settings must have either rect or size attribute")
            # border=Border(self.settings.type, self.settings.color, bbox=self.settings.border.bbox)

        if border_mode != BorderMode.AUTO and "size" not in border:
            raise BinPackerError("Border mode AUTO expects size attribute")

        bin.set_border(bin_border)

    def normalise_border(self):
        realWidth = self.max_width - self.settings.border_size * 2
        realHeight = self.max_height - self.settings.border_size * 2
        for bin in self.binSet:
            border = bin.border
            if bin.top is 0:
                border.top = 0

            else:
                bin.set_coord(bin.left, bin.top - self.settings.border_size)

            if bin.left is 0:
                border.left = 0

            else:
                bin.set_coord(bin.left - self.settings.border_size, bin.top)

            if bin.right > realWidth:
                border.right = 0

            if bin.bottom > realHeight:
                border.bottom = 0

            self.binSet.set_size(realWidth, realHeight)

    def flush(self):
        if self.settings.border_mode == BorderMode.AUTO:
            self.normalise_border()

        result = self.binSet
        self.binSet = BinSet(self.max_width, self.max_height)
        self._on_flush()
        self._on_set_size()
        return result

    def _on_flush(self):
        pass
