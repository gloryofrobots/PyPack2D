from pypack2d.pack2d.packer.packer import BinPacker

from pypack2d.pack2d.rectangle import Rectangle


class PackNode(Rectangle):
    def _on_init(self):
        self.firstChild = None
        self.secondChild = None
        pass

    def has_children(self):
        if self.secondChild is None \
                and self.firstChild is None:
            return False
            pass

        return True
        pass

    def get_free_branch(self, rect, placer):
        if self.has_children() is True:
            best, worth = placer.getPlace(self.firstChild, self.secondChild)
            leaf = best.get_free_branch(rect)
            if leaf is None:
                return worth.get_free_branch(rect)
                pass
            else:
                return leaf
                pass
            pass

        if rect.width > self.width or rect.height > self.height:
            return None
            pass

        return self
        pass

    def insert(self, rect, splitter, placer):
        if self.has_children() is True:
            best, worth = placer.choose(rect, self.firstChild, self.secondChild)
            leaf = best.insert(rect, splitter, placer)
            if leaf is None:
                return worth.insert(rect, splitter, placer)
                pass
            else:
                return leaf
                pass
            pass

        if rect.width > self.width or rect.height > self.height:
            return None
            pass

        rectangles = splitter.split(self, rect)

        self.firstChild = PackNode.from_rectangle(rectangles[0])
        self.secondChild = PackNode.from_rectangle(rectangles[1])

        leaf = PackNode.from_rectangle(Rectangle(self.left, self.top, self.left + rect.width, self.top + rect.height))
        return leaf
        pass

    pass


class BinPackerGuillotine(BinPacker):
    def _on_init(self, factory, settings):
        self.splitter = factory.create_instance(settings.splitRule)
        pass

    def _on_set_size(self):
        self.packNode = PackNode(0, 0, self.maxWidth, self.maxHeight)
        pass

    def _on_pack_bin(self, bin):
        leaf = self.packNode.insert(bin, self.splitter, self.heuristic)
        if leaf == None:
            return False
            pass

        bin.set_coord(leaf.left, leaf.top)
        return True
        pass

    def _on_flush(self):
        self.packNode = PackNode(0, 0, self.maxWidth, self.maxHeight)
        pass

    pass
