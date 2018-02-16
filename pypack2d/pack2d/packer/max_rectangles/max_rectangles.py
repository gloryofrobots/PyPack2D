from pypack2d.pack2d.packer.packer import BinPacker
from pypack2d.pack2d.rectangle import Rectangle as Area


class BinPackerMaxRectangles(BinPacker):
    def _on_init(self, factory, settings):
        self.waste = []
        pass

    def _on_set_size(self):
        self.areas = [Area.from_wh(self.maxWidth, self.maxHeight)]
        pass

    def _on_pack_bin(self, bin):
        bestRect = self.get_best_rectangle(bin, self.heuristic)

        if bestRect is None:
            return False
            pass

        destination = self.place_bin_to_rect(bestRect, bin)
        bin.set_coord(destination.left, destination.top)
        return True
        pass

    def place_bin_to_rect(self, rect, bin):
        destination = Area(rect.left, rect.top, bin.width, bin.height)
        self.split_on_max_rectangles(rect, destination, self.areas)
        self.areas.remove(rect)
        self.check_bin_intersections(destination)
        self.normalise_rectangles()
        return destination
        pass

    def check_bin_intersections(self, bin):
        newRects = []

        for rect in self.areas:
            intersection = rect.getIntersection(bin)
            if intersection is None:
                continue
                pass

            self.split_on_max_rectangles(rect, intersection, newRects)
            self.waste.append(rect)
            pass

        if len(newRects) is 0:
            return
            pass

        self.remove_bad()
        self.areas.extend(newRects)
        pass

    def normalise_rectangles(self):
        sortedAreas = sorted(self.areas, key=lambda rect: rect.area, reverse=False)

        for i in range(len(sortedAreas)):
            checked = sortedAreas[i]
            for rect in sortedAreas[i + 1: len(self.areas)]:
                if rect.isContain(checked):
                    self.waste.append(checked)
                    break
                    pass
                pass
            pass

        self.remove_bad()
        pass

    def remove_bad(self):
        for area in self.waste:
            self.areas.remove(area)
            pass

        self.waste = []
        pass

    def split_on_max_rectangles(self, bigRect, splitRect, destination):
        if splitRect.left != bigRect.left:
            rect = Area(bigRect.left, bigRect.top, splitRect.left - bigRect.left, bigRect.height)
            destination.append(rect)
            pass

        if splitRect.top != bigRect.top:
            rect = Area(bigRect.left, bigRect.top, bigRect.width, splitRect.top - bigRect.top)
            destination.append(rect)
            pass

        if splitRect.right != bigRect.right:
            rect = Area(splitRect.right, bigRect.top, bigRect.right - splitRect.right, bigRect.height)
            destination.append(rect)
            pass

        if splitRect.bottom != bigRect.bottom:
            rect = Area(bigRect.left, splitRect.bottom, bigRect.width, bigRect.bottom - splitRect.bottom)
            destination.append(rect)
            pass
        pass

    def get_best_rectangle(self, bin, heuristic):
        bestRect = None
        for rect in self.areas:
            if rect.isPossibleToFit(bin) is False:
                continue
                pass

            best, worth = heuristic.choose(bin, bestRect, rect)

            if best is not bestRect:
                bestRect = best
                pass
            pass

        return bestRect
        pass

    def _on_debug(self):
        return
        from PIL import Image, ImageDraw
        from random import choice, randrange

        COLORS = []
        for i in range(1000):
            r = randrange(0, 255)
            g = randrange(0, 255)
            b = randrange(0, 255)
            COLORS.append((r, g, b))
            pass

        canvas = Image.new("RGBA", (self.binSet.width, self.binSet.height), color=(128, 128, 128))
        draw = ImageDraw.Draw(canvas)

        for area in self.areas:
            draw.rectangle([area.left, area.top, area.right - 1, area.bottom - 1], outline=choice(COLORS))
            pass

        for bin in self.binSet:
            # img = Image.new("RGBA", (bin.width, bin.height), color = choice(COLORS))
            draw.rectangle([bin.left, bin.top, bin.right - 1, bin.bottom - 1], fill=choice(COLORS))
            # canvas.paste(img, (bin.left, bin.top))
            pass

        canvas.show()
        pass

    pass
