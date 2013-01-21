from AtlasGenerator.Atlas import Atlas

class AtlasGenerator(object):
    def __init__(self):
        super(AtlasGenerator,self).__init__()
        self.sorter = None
        pass

    def setSorting(self, sortKey, sortOrder):
        
        pass

    def initialise(self, dirPath, relativeFileName, maxWidth, maxHeight, texMode, atlasType, fillColor):
        self.dirPath = dirPath
        self.relativeFileName = relativeFileName
        self.maxWidth = maxWidth
        self.maxHeight = maxHeight

        self.texMode = texMode
        self.atlasType = atlasType
        self.fillColor = fillColor

        self.images = []

        self.atlases = []
        pass

    def getNewAtlas(self):
        index = len(self.atlases)
        counter = ""
        if index > 0:
            counter = "%i" % index
            pass

        atlas = Atlas(self.maxWidth, self.maxHeight)
        atlasFileName = self.relativeFileName + counter + "." + self.atlasType
        atlas.initialise(self.dirPath, atlasFileName, self.texMode, self.atlasType, self.fillColor)
        return atlas
        pass

    def addImages(self, images):
        self.images.extend(images)
        pass

    def addImage(self, image):
        self.images.append(image)
        pass

    def prepare(self):
        #self.images = sorted(self.images , key = lambda image: image.getBiggestSide(), reverse=False)
        self.images = sorted(self.images , key = lambda image: image.getLowestSide(), reverse=False)
        pass
    
    def generate(self):
        self.prepare()

        if len(self.images) is 0:
            #print ("file list empty")
            return False
            pass

        isAdded = False

        atlas = self.getNewAtlas()

        while True:
            if len(self.images) is 0:
                break
                pass

            image = self.images.pop()

            if image.getWidth() > self.maxWidth or image.getHeight() > self.maxHeight:
                print ("ERROR atlas size %i,%i to small for rect %i %i" % (self.maxWidth, self.maxHeight, image.getWidth(), image.getHeight()))
                continue
                pass

            isAdded = atlas.addImage(image)

            if isAdded is True:
                continue
                pass

            self.atlases.append(atlas)

            atlas = self.getNewAtlas()
            self.images.insert(0, image)
            pass

        if isAdded is True:
            self.atlases.append(atlas)
            pass

        for atlas in self.atlases:
            atlas.pack()
            atlas.save()
            pass
        
        print ("It all fit into " + str(len(self.atlases) ) + " images!")
        pass
    pass


