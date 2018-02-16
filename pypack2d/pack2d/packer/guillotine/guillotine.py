from pypack2d.pack2d.packer.packer import BinPacker

from pypack2d.pack2d.rectangle import Rectangle


class PackNode(Rectangle):
    def _on_init(self):
        self.firstChild = None
        self.secondChild = None

    def has_children(self):
        if self.secondChild is None \
                and self.firstChild is None:
            return False

        return True

    def get_free_branch(self, rect, placer):
        if self.has_children() is True:
            best, worth = placer.getPlace(self.firstChild, self.secondChild)
            leaf = best.get_free_branch(rect)
            if leaf is None:
                return worth.get_free_branch(rect)

            else:
                return leaf

        if rect.width > self.width or rect.height > self.height:
            return None

        return self

    def insert(self, rect, splitter, placer):
        if self.has_children() is True:
            best, worth = placer.choose(rect, self.firstChild, self.secondChild)
            leaf = best.insert(rect, splitter, placer)
            if leaf is None:
                return worth.insert(rect, splitter, placer)

            else:
                return leaf

        if rect.width > self.width or rect.height > self.height:
            return None

        rectangles = splitter.split(self, rect)

        self.firstChild = PackNode.from_rectangle(rectangles[0])
        self.secondChild = PackNode.from_rectangle(rectangles[1])

        leaf = PackNode.from_rectangle(Rectangle(self.left, self.top, self.left + rect.width, self.top + rect.height))
        return leaf


class BinPackerGuillotine(BinPacker):
    def _on_init(self, factory, settings):
        self.splitter = factory.create_instance(settings.split_rule)

    def _on_set_size(self):
        self.packNode = PackNode(0, 0, self.max_width, self.max_height)

    def _on_pack_bin(self, bin):
        leaf = self.packNode.insert(bin, self.splitter, self.heuristic)
        if leaf == None:
            return False

        bin.set_coord(leaf.left, leaf.top)
        return True

    def _on_flush(self):
        self.packNode = PackNode(0, 0, self.max_width, self.max_height)
