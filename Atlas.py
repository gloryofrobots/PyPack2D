__author__ = 'human88998999877'
from PyBuilder.Atlas.AtlasGenerator.TexturePackerSkyLine.TexturePacker import TexturePacker

from PIL import Image

class Atlas(object):
    def __init__(self, maxWidth, maxHeight):
        super(Atlas,self).__init__()
        self.maxWidth = maxWidth
        self.maxHeight = maxHeight
        self.width = 0
        self.height = 0

        self.path = None
        
        self.packer = TexturePacker(self.maxWidth,self.maxHeight)
        self.images = []
        pass

    def initialise(self, dirPath, fileName, texMode, atlasType, fillColor):
        self.dirPath = dirPath
        self.fileName = fileName
        self.textureMode = texMode
        self.atlasType = atlasType
        self.fillColor = fillColor
        pass

    def getFileName(self):
        return self.fileName
        pass
    
    def isEmpty(self):
        if len(self.images) is 0:
            return True
            pass

        return False
        pass

    def addImage(self, image):
        if self.packer.addTexture(image.getPath(), image.getWidth(), image.getHeight(), image.getBorderSize()) is False:
            print("ADD IMAGE FALSE")
            return False
            pass

        self.images.append(image)
        return True
        pass

    def getWidth(self):
        return self.width
        pass

    def getHeight(self):
        return self.height
        pass
    
    def pack(self):
        self.packer.packTextures()
        self.width = self.packer.getWidth()
        self.height = self.packer.getHeight()
        pass
    
    def save(self):
        canvas = Image.new(self.textureMode, (self.width, self.height), self.fillColor)
        for img in self.images:
            texture = self.packer.getTextureByName(img.path)

            #print("---",img.path,texture.getX(), texture.getY())
            img.setTexture(texture)
            img.onPackToAtlas(self)
            
            pilImage = img.getImagePIL()
            canvas.paste(pilImage, (texture.getX(), texture.getY()))
            pass

        path = self.dirPath + "\\" + self.fileName
        dir = FileSystem.getDirname(path)
        #TODO CHANGE THIS
        #FileSystem.makeDirsRecursiveIfNotExist(dir)
        canvas.save(path, self.atlasType)
        #canvas.show()
        pass
    pass