class BinSet(object):
    def __init__(self, width, height):
        super(BinSet, self).__init__()
        self.bins = []
        self.width = width
        self.height = height
        pass

    def set_size(self, width, height):
        self.width = width
        self.height = height
        pass

    def add(self, bin):
        self.bins.append(bin)
        pass

    def getBins(self):
        return self.bins
        pass

    def __iter__(self):
        return self.bins.__iter__()
        pass

    def get_efficiency(self):
        area =  self.width * self.height
        binsArea = self.get_bins_area()
        efficiency = (binsArea * 100) / area
        return efficiency
        pass

    def get_free_space(self):
        area =  self.width * self.height
        binsArea = self.get_bins_area()
        return area - binsArea
        pass

    def get_bins_area(self):
        binsArea = 0
        for bin in self.bins:
            binsArea += bin.area
            pass

        return binsArea
        pass
    pass