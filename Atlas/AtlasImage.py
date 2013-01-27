__author__ = 'human88998999877'

from Atlas.Field2D import Field2D
from PIL import Image

class AtlasImage(object):
    def __init__(self, path):
        super(AtlasImage, self).__init__()
        self.img = Image.open(path)
        self.path = path
        self._initialise()
        self.bin = None
        pass

    def __repr__(self):
        return "<%s %s (%i,%i)>" %( self.__class__.__name__, self.path, self.width, self.height)
        pass
    
    def getBin(self):
        return self.bin
        pass

    def _initialise(self):
        self.width = self.img.size[0]
        self.height = self.img.size[1]
        pass

    def copyLines(self, field2D, sourceLineNumber, lineNumbers):
        for lineNumber in lineNumbers:
            #print("copyLine",sourceLineNumber,lineNumber)
            field2D.copyLine(field2D,sourceLineNumber,lineNumber)
            pass
        pass

    def copyColumns(self, field2D, sourceColumnNumber, columnNumbers):
        for columnNumber in columnNumbers:
            #print("copyColumn",sourceColumnNumber,columnNumber)
            field2D.copyColumn(field2D, sourceColumnNumber, columnNumber)
            pass
        pass

    def _createBorderFromMyBody(self, border):
        newWidth = self.width + border[0] + border[2]
        newHeight = self.height + border[1] + border[3]

        #TODO CHECK IS COLOR NOT SEEN
        newImage = Image.new("RGBA",(newWidth, newHeight),(128,128,128,255) )

        newImage.paste(self.img,(border[0], border[1]))
        data = list(newImage.getdata())
        field2D = Field2D(data, newWidth, newHeight)
        #print(self.height,newHeight)
        #Copying data to box around
        if border[1] is not 0:
            #print("copy top")
            #top Lines
            sourceLine = border[1]
            lineNumbers = range(0, sourceLine)
            self.copyLines(field2D, sourceLine, lineNumbers)
            pass

        if border[3] is not 0:
            #print("copy bottom")
            #bottom lines+
            sourceLine = self.height + border[1] - 1
            lineNumbers = range(sourceLine + 1, newHeight)

            self.copyLines(field2D, sourceLine, lineNumbers)
            pass

        if border[0] is not 0:
            #print("copy left")
            #left columns
            sourceColumn = border[0]
            columnNumbers = range(0, sourceColumn)
            self.copyColumns(field2D, sourceColumn, columnNumbers)
            pass
        
        if border[2] is not 0:
            #print("copy right")
            #right columns
            sourceColumn = self.width + border[0] - 1 
            columnNumbers = range(sourceColumn + 1, newWidth)

            self.copyColumns(field2D, sourceColumn, columnNumbers)
            pass
      
        newImage.putdata(data)
        self.img = newImage

        self._initialise()
        pass

    def getImagePIL(self):
        return self.img
        pass
    
    def getPath(self):
        return  self.path
        pass

    def getWidth(self):
        return self.width
        pass

    def getHeight(self):
        return self.height
        pass

    def setBin(self, bin):
        self.bin = bin

        if self.bin.isRotate():
            self.img = self.img.rotate(-90)
            self._initialise()
            pass

        border = self.bin.getBorder()

        if border[0] == 0 and border[1] == 0 and border[2] == 0 and border[3] == 0:
            return
            pass
        
        self._createBorderFromMyBody(border)
        pass

    def getUV(self):
        #TODO
        #return self.bin.getUV()
        pass
    
    def isRotate(self):
        return self.bin.isRotate()
        pass
    
    def pack(self, atlas):
        canvas = atlas.getCanvas()

        if self.bin is None:
            raise BaseException("Atlas Image pack error. Bin not determined")
            pass

        canvas.paste(self.img, box = (self.bin.left, self.bin.top))
        self._onPack(atlas)
        pass

    def _onPack(self,atlas):
        pass
    pass

class AtlasImagePyBuilder(AtlasImage):
    def __init__(self, path, onPackCallback = None):
        super(AtlasImagePyBuilder, self).__init__(path)
        self.onPackCallback = onPackCallback
        pass

    def _onPack(self,atlas):
        self.onPackCallback(self, atlas)
        pass
    pass