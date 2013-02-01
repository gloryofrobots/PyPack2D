__author__ = 'human88998999877'

from Packing2D.BinPacker.BinSet import BinSet
from Packing2D import BorderMode,RotateMode

class BinPackerError(BaseException):
    pass

class BinPackerValidateSettingsError(BaseException):
    pass

class BinPacker(object):
    def __init__(self):
        super(BinPacker,self ).__init__()
        self.debugCount = 0
        pass

    def abortOnCount(self, limit):
        if self.debugCount >= limit:
            raise BaseException()
            pass
        
        self.debugCount+=1
        pass
    
    def initialise(self, factory, settings):
        self.settings = settings
        self.heuristic = factory.getInstance(settings.placeHeuristic)
        self._onInitialise( factory, settings )
        self.settings = settings

        self.binSet = BinSet(self.settings.maxWidth, self.settings.maxHeight)
        pass

    def isValidSettings(self, settings):
        return self._isValidSettings(settings)
        pass

    def _isValidSettings(self, settings):
        raise NotImplementedError()
        pass
    
    def _onInitialise(self, factory, settings):
        raise NotImplementedError()
        pass

    def packBin(self, bin):
        self.setBorder(bin)
        self.rotateBin(bin)
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
                raise BaseException( "Validate Error bins are intersected : %s with %s" % (binCheck,bin) )
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
        return (0,0,0,0)
        pass

    def rotateBin(self, rect):
        self._onRotateBin(rect)
        pass

    def _onRotateBin(self, rect):
        if self.settings.rotateMode == RotateMode.NONE:
            return
            pass
        elif self.settings.rotateMode == RotateMode.UP_RIGHT:
            rect.rotateUpRight()
            pass
        elif self.settings.rotateMode == RotateMode.SIDE_WAYS:
            rect.rotateSideWays()
            pass
        pass
    
    def setBorder(self, bin):
        if self.settings.borderMode == BorderMode.NONE:
            return
            pass

        elif self.settings.borderMode == BorderMode.STRICT:
            bin.setBorder(self.settings.border)
            pass
        elif self.settings.borderMode == BorderMode.AUTO:
            border = self._createAutoBorder(bin)
            bin.setBorder(border)
            pass
        pass

    def flush(self):
        result = self.binSet
        self.binSet = BinSet(self.settings.maxWidth, self.settings.maxHeight)
        self._onFlush()
        return result
        pass

    def _onFlush(self):
        raise NotImplementedError()
        pass
    pass