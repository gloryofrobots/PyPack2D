from pypack2d.pack2d.settings import BorderMode, BorderType
from pypack2d.pack2d.border import Border


class BinPackerError(Exception):
    pass


class AbortError(Exception):
    pass


class ManualAbort(object):
    def __init__(self):
        super(ManualAbort, self).__init__()
        self.debug_count = 0

    def abort_on_count(self, limit):
        if self.debug_count >= limit:
            raise AbortError("Abort on count")

        self.debug_count += 1


class BinSet(object):
    def __init__(self, width, height):
        super(BinSet, self).__init__()
        self.bins = []
        self.width = width
        self.height = height

    def set_size(self, width, height):
        self.width = width
        self.height = height

    def add(self, bin):
        self.bins.append(bin)

    def get_bins(self):
        return self.bins

    def __iter__(self):
        return self.bins.__iter__()

    def get_efficiency(self):
        area = self.width * self.height
        bins_area = self.get_bins_area()
        efficiency = (bins_area * 100) / area
        return efficiency

    def get_free_space(self):
        area = self.width * self.height
        bins_area = self.get_bins_area()
        return area - bins_area

    def get_bins_area(self):
        bins_area = 0
        for bin in self.bins:
            bins_area += bin.area

        return bins_area


class BinPacker(object):
    def __init__(self):
        super(BinPacker, self).__init__()
        self.bin_set = None
        self.heuristic = None
        self.settings = None
        self.max_width = 0
        self.max_height = 0

    def initialise(self, factory, settings):
        self.heuristic = factory.create_instance(settings.place_heuristic)
        self.settings = settings
        self._on_init(factory, settings)

    def set_size(self, width, height):
        self.max_width = width
        self.max_height = height

        if self.settings.border_mode == BorderMode.AUTO:
            self.max_height += self.settings.border_size * 2
            self.max_width += self.settings.border_size * 2

        self.bin_set = BinSet(self.max_width, self.max_height)
        self._on_set_size()

    def _on_set_size(self):
        raise NotImplementedError()

    def _on_init(self, factory, settings):
        pass

    def pack_bin(self, bin):
        self.set_border(bin)

        if self._on_pack_bin(bin) is False:
            return False

        self.validate(bin)

        self.bin_set.add(bin)
        return True

    def validate(self, bin):
        for binCheck in self.bin_set:
            if binCheck.is_intersect(bin) is True:
                raise BinPackerError("Validate Error bins are intersected : %s with %s" % (binCheck, bin))

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
            rect = border["rect"]
            if isinstance(rect, dict):
                try:
                    rect = (rect["left"], rect["top"], rect["right"], rect["bottom"])
                except KeyError:
                    raise BinPackerError("Border rect can be tuple (left, top, right, bottom) "
                                         "or dict {left=, top=, right=, bottom=}")

            bin_border = Border.from_rect(border_type, border_color, rect)
            if border_mode != BorderMode.STRICT:
                raise BinPackerError("Border rect can be specified only for STRICT border mode")
        elif "size" in border:
            size = int(border["size"])
            if size <= 0:
                raise BinPackerError("Border size must be > 0")

            bin_border = Border.from_size(border_type, border_color, border["size"])
        else:
            raise BinPackerError("border settings must have either rect or size attribute")

        if border_mode == BorderMode.AUTO and "size" not in border:
            raise BinPackerError("Border mode AUTO expects size attribute")

        bin.set_border(bin_border)

    def normalise_border(self):
        real_width = self.max_width - self.settings.border_size * 2
        real_height = self.max_height - self.settings.border_size * 2
        for bin in self.bin_set:
            border = bin.border
            if bin.top is 0:
                border.top = 0

            else:
                bin.set_coord(bin.left, bin.top - self.settings.border_size)

            if bin.left is 0:
                border.left = 0

            else:
                bin.set_coord(bin.left - self.settings.border_size, bin.top)

            if bin.right > real_width:
                border.right = 0

            if bin.bottom > real_height:
                border.bottom = 0

            self.bin_set.set_size(real_width, real_height)

    def flush(self):
        if self.settings.border_mode == BorderMode.AUTO:
            self.normalise_border()

        result = self.bin_set
        self.bin_set = BinSet(self.max_width, self.max_height)
        self._on_flush()
        self._on_set_size()
        return result

    def _on_flush(self):
        pass
