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
        pass

    def initialise(self, factory, settings):
        self.settings = settings
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
        
        self.binSet.add(bin)
        return True
        pass

    def _onPackBin(self, bin):
        raise NotImplementedError()
        pass

    def _createAutoBorder(self, bin):
        return (0,0,0,0)
        pass

    def rotateBin(self, rect):
        if self.settings.rotateMode == RotateMode.NONE:
            return
            pass
        elif self.settings.rotateMode == RotateMode.HEIGHT_LONGER:
            if rect.getWidth() < rect.getHeight():
                rect.setRotate(True)
                pass
            pass
        elif self.settings.rotateMode == RotateMode.WIDTH_LONGER:
            if rect.getWidth() > rect.getHeight():
                rect.setRotate(True)
                pass
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