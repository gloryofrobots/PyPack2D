__author__ = 'human88998999877'

from PyBuilder.Atlas.AtlasGenerator.Field2D import Field2D
from PIL import Image

class AtlasImage(object):
    def __init__(self, path, onPackCallback, borderSize):
        super(AtlasImage, self).__init__()
        self.img = Image.open(path)
        self.path = path
        self.onPackCallback = onPackCallback
        self._initialise()
        self.borderSize = borderSize
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

        newWidth = self.width + border.left + border.right
        newHeight = self.height + border.top + border.bottom
        
        newImage = Image.new("RGBA",(newWidth, newHeight),(128,128,128,255) )

        newImage.paste(self.img,(border.left, border.top))
        data = list(newImage.getdata())
        field2D = Field2D(data, newWidth, newHeight)
        #print(self.height,newHeight)
        #Copying data to box around
        if border.top is not 0:
            #print("copy top")
            #top Lines
            sourceLine = border.top
            lineNumbers = range(0, sourceLine)
            self.copyLines(field2D, sourceLine, lineNumbers)
            pass

        if border.bottom is not 0:
            #print("copy bottom")
            #bottom lines
            sourceLine = self.height + border.top - 1
            lineNumbers = range(sourceLine + 1, newHeight)

            self.copyLines(field2D, sourceLine, lineNumbers)
            pass

        if border.left is not 0:
            #print("copy left")
            #left columns
            sourceColumn = border.left
            columnNumbers = range(0, sourceColumn)
            self.copyColumns(field2D, sourceColumn, columnNumbers)
            pass
        
        if border.right is not 0:
            #print("copy right")
            #right columns
            sourceColumn = self.width + border.left - 1 
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

    def getBorderSize(self):
        return self.borderSize
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

    def getLowestSide(self):
        if self.height < self.width:
            return self.height
            pass

        return self.width
        pass

    def getBiggestSide(self):
        if self.height > self.width:
            return self.height
            pass

        return self.width
        pass

    def getRatio(self):
        return self.width / self.height
        pass

    def getDiff(self):
        return self.width - self.height
        pass

    def getPerimeter(self):
        return self.width + self.height
        pass

    def getArea(self):
        return self.width * self.height
        pass

    def setTexture(self, texture):
        self.texture = texture

        if self.texture.isRotate():
            self.img = self.img.rotate(-90)
            self._initialise()
            pass

        border = self.texture.getBorder()

        if border.isZero() is True:
            return
            pass
        
        #print("self._createBorderFromMyBody",texture.name)
        self._createBorderFromMyBody(border)
        #from PyBuilder.FileSystem import FileSystem
        #path = "D:\\Projects\\PyBuilderConsole\\atlases\\textures\\" + FileSystem.getBasename(texture.name)

        #self.img.save(path)
        pass

    def getUV(self):
        return self.texture.getUV()
        pass
    
    def isRotate(self):
        return self.texture.isRotate()
        pass
    
    def onPackToAtlas(self, atlas):
        self.onPackCallback(self, atlas)
        pass
    pass

"""
from PIL import Image
path = "D:\\Projects\\PyBuilderConsole\\atlases\\textures\\test\\100x100(border).png"
resultPath = "D:\\Projects\\PyBuilderConsole\\atlases\\textures\\test\\100x100(border)2.png"
image = AtlasImage(path,None,(1,1))
image.img.save("D:\\Projects\\PyBuilderConsole\\atlases\\textures\\test\\100x100(border)2.png")

x = [0,0,0,0,0,0,0]
y = [1,1,1,1]"""