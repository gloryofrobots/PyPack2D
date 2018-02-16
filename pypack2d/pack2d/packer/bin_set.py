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

    def getBins(self):
        return self.bins

    def __iter__(self):
        return self.bins.__iter__()

    def get_efficiency(self):
        area = self.width * self.height
        binsArea = self.get_bins_area()
        efficiency = (binsArea * 100) / area
        return efficiency

    def get_free_space(self):
        area = self.width * self.height
        binsArea = self.get_bins_area()
        return area - binsArea

    def get_bins_area(self):
        binsArea = 0
        for bin in self.bins:
            binsArea += bin.area

        return binsArea
