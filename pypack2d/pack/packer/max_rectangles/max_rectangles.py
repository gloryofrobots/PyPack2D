from pypack2d.pack.packer.packer import BinPacker
from pypack2d.pack.rectangle import Rectangle as Area


class BinPackerMaxRectangles(BinPacker):
    def _on_init(self, factories, settings):
        self.waste = []

    def _on_set_size(self):
        self.areas = [Area.from_wh(self.max_width, self.max_height)]

    def _on_pack_bin(self, bin):
        best_rect = self.get_best_rectangle(bin, self.heuristic)

        if best_rect is None:
            return False

        destination = self.place_bin_to_rect(best_rect, bin)
        bin.set_coord(destination.left, destination.top)
        return True

    def place_bin_to_rect(self, rect, bin):
        destination = Area(rect.left, rect.top, bin.width, bin.height)
        self.split_on_max_rectangles(rect, destination, self.areas)
        self.areas.remove(rect)
        self.check_bin_intersections(destination)
        self.normalise_rectangles()
        return destination

    def check_bin_intersections(self, bin):
        new_rects = []

        for rect in self.areas:
            intersection = rect.get_intersection(bin)
            if intersection is None:
                continue

            self.split_on_max_rectangles(rect, intersection, new_rects)
            self.waste.append(rect)

        if len(new_rects) is 0:
            return

        self.remove_bad()
        self.areas.extend(new_rects)

    def normalise_rectangles(self):
        sorted_areas = sorted(self.areas, key=lambda rect: rect.area, reverse=False)

        for i in range(len(sorted_areas)):
            checked = sorted_areas[i]
            for rect in sorted_areas[i + 1: len(self.areas)]:
                if rect.is_contain(checked):
                    self.waste.append(checked)
                    break

        self.remove_bad()

    def remove_bad(self):
        for area in self.waste:
            self.areas.remove(area)

        self.waste = []

    def split_on_max_rectangles(self, big_rect, split_rect, destination):
        if split_rect.left != big_rect.left:
            rect = Area(big_rect.left, big_rect.top, split_rect.left - big_rect.left, big_rect.height)
            destination.append(rect)

        if split_rect.top != big_rect.top:
            rect = Area(big_rect.left, big_rect.top, big_rect.width, split_rect.top - big_rect.top)
            destination.append(rect)

        if split_rect.right != big_rect.right:
            rect = Area(split_rect.right, big_rect.top, big_rect.right - split_rect.right, big_rect.height)
            destination.append(rect)

        if split_rect.bottom != big_rect.bottom:
            rect = Area(big_rect.left, split_rect.bottom, big_rect.width, big_rect.bottom - split_rect.bottom)
            destination.append(rect)

    def get_best_rectangle(self, bin, heuristic):
        best_rect = None
        for rect in self.areas:
            if rect.is_possible_to_fit(bin) is False:
                continue

            best, worth = heuristic.choose(bin, best_rect, rect)

            if best is not best_rect:
                best_rect = best

        return best_rect
