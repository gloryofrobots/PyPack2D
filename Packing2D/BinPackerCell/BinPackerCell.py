__author__ = 'human88998999877'

from Packing2D.BinPacker.BinPacker import BinPacker,BinPackerValidateSettingsError
from Packing2D import PlaceHeuristic


from Packing2D.BinPackerCell.Cell import Cell


class BinPackerCell(BinPacker):
    def _onInitialise(self, factory, settings):
        self.heuristic = None
        self._initHeuristic(settings)
        self.cells = [Cell( 0, 0, settings.maxWidth, settings.maxHeight )]
        pass

    def _initHeuristic(self, settings):
#        if settings.placeHeuristic == PlaceHeuristic.WORST_AREA_FIT:
#            self.heuristic = PlaceHeuristicWorstAreaFit()
#            pass
#        else:
#            raise BinPackerValidateSettingsError( "Place heuristic incorrect %s" % str(settings.placeHeuristic) )
#            pass
        pass

    def _onPackBin(self, bin):
        bestCell = self.getBestCell(bin)

        if bestCell is None:
            return False
            pass

        destinationRect = bestCell.place(bin)

        newLine = Cell( destinationRect.left, destinationRect.bottom, destinationRect.width, bestCell.height - bin.height )

        if bestCell.isOver() is True:
            self.cells.remove(bestCell)
            pass

        self.cells.append(newLine)

        self.normalise(destinationRect)

        bin.setCoord(destinationRect.left, destinationRect.top)
        return True
        pass

    def _onFlush(self):
        self.cells = [Cell( 0, 0, self.settings.maxWidth, self.settings.maxHeight )]
        pass

    def canPlace(self, cell, rect):
        if cell.height < rect.height:
            return False
            pass

        if cell.width >= rect.width:
            return True
            pass

        rightEdge = cell.left + rect.width

        if rightEdge > self.settings.maxWidth:
            return False
            pass

        for bin in self.binSet:
            if bin.left < rightEdge and bin.bottom > cell.top:
                return False
                pass
            pass

        return True
        pass
    pass

    def getBestCell(self, bin):
        bestCell = None
        minTopLeft = self.settings.maxHeight * 2
        for cell in self.cells:
            if self.canPlace( cell, bin ) is False:
                continue
                pass

            topLeft =  cell.top + bin.height

            if minTopLeft < topLeft:
                continue
                pass

            bestCell = cell
            minTopLeft = topLeft
            pass

        return bestCell
        pass

    def normalise(self, destinationRect):
        newCells = []
        for cell in self.cells:
            if cell.left < destinationRect.right \
               and cell.top < destinationRect.top :

                if cell.right < destinationRect.right:
                    cell.setBB( cell.left, cell.top, cell.right, destinationRect.top )
                    pass
                else:
                    newCell = Cell( cell.left, cell.top, destinationRect.right, destinationRect.top )
                    cell.cut( newCell.getWidth() )
                    newCells.append(newCell)
                    pass

                pass

        if len(newCells) is not 0:
            self.cells.extend(newCells)
            pass
        pass
    pass


