__author__ = 'human88998999877'

from Packing2D.BinPacker.BinSet import BinSet
from Packing2D import BorderMode,RotateMode
from Packing2D.Border import Border

class BinPackerError(BaseException):
    pass

class ManualAbort(object):
    def __init__(self):
        super(ManualAbort,self ).__init__()
        self.debugCount = 0
        pass

    def abortOnCount(self, limit):
        if self.debugCount >= limit:
            raise BaseException()
            pass

        self.debugCount+=1
        pass
    pass

class BinPacker(object):
    def __init__(self):
        super(BinPacker,self ).__init__()
        pass
    
    def initialise(self, factory, settings):
        self.settings = settings
        self.heuristic = factory.getInstance(settings.placeHeuristic)
        self._onInitialise( factory, settings )
        self.settings = settings

        self.maxWidth = self.settings.maxWidth
        self.maxHeight = self.settings.maxHeight

        if self.settings.borderMode == BorderMode.AUTO:
            self.maxHeight += self.settings.borderSize * 2
            self.maxWidth += self.settings.borderSize * 2
            pass

        self.binSet = BinSet(self.maxWidth, self.maxHeight)
        pass

    def _onInitialise(self, factory, settings):
        raise NotImplementedError()
        pass

    def packBin(self, bin):
        self.setBorder(bin)

        if self._onPackBin(bin) is False:
            return False
            pass
        
        if self.settings.isDebug is True:
            self.validate(bin)
            self.onDebug()
            pass

        self.binSet.add(bin)
        return True
        pass

    def validate(self, bin):
        for binCheck in self.binSet:
            if binCheck.isIntersect(bin) is True:
                raise BinPackerError( "Validate Error bins are intersected : %s with %s" % (binCheck,bin) )
                pass
            pass
        pass

    def onDebug(self):
        self._onDebug()
        pass

    def _onDebug(self):
        pass

    def _onPackBin(self, bin):
        raise NotImplementedError()
        pass

    def _createAutoBorder(self, bin):
        return None
        pass
    
    def setBorder(self, bin):
        if self.settings.borderMode == BorderMode.NONE:
            return
            pass
        elif self.settings.borderMode == BorderMode.STRICT:
            bin.setBorder(self.settings.border)
            pass
        elif self.settings.borderMode == BorderMode.AUTO:
            border = Border( borderSize = self.settings.borderSize, type = self.settings.borderType, color = self.settings.borderColor )
            bin.setBorder(border)
            pass
        pass

    def flush(self):
        result = self.binSet
        self.binSet = BinSet(self.maxWidth, self.maxHeight)
        self._onFlush()
        return result
        pass

    def _onFlush(self):
        raise NotImplementedError()
        pass
    pass