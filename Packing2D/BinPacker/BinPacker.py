__author__ = 'human88998999877'

from Packing2D.BinPacker.BinSet import BinSet

class BinPackerError(BaseException):
    pass

class BinPackerValidateSettingsError(BaseException):
    pass

class BinPacker(object):
    def __init__(self):
        super(self, BinPacker).__init__()
        pass

    def initialise(self, factory, settings):
        self.binSet = BinSet()
        #self.isValidSettings( settings )
        self.settings = settings
        self._onInitialise( factory, settings )
        self.settings = settings
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
        self._onPackBin(bin)
        pass

    def _onPackBin(self, bin):
        raise NotImplementedError()
        pass

    def _createAutoBorder(self, bin):
        return (0,0,0,0)
        pass

    def rotateBin(self, bin):
        if self.settings.isRotate is False:
            return
            pass

        if bin.getWidth() < bin.getHeight():
            bin.rotate()
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
        #self._onFlush()
        result = self.binSet
        self.binSet = BinSet()
        return result
        pass

#    def _onFlush(self):
#        raise NotImplementedError()
#        pass
    pass