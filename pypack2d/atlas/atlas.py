from PIL import Image


class Atlas(object):
    def __init__(self):
        super(Atlas, self).__init__()
        self.width = 0
        self.height = 0
        self.dirPath = None
        self.fileName = None
        self.textureMode = None
        self.atlasType = None
        self.fillColor = None

        self.canvas = None
        self.images = []

    def initialise(self, width, height, dirPath, fileName, texMode, atlasType, fillColor):
        self.width = width
        self.height = height
        self.dirPath = dirPath
        self.fileName = fileName
        self.textureMode = texMode
        self.atlasType = atlasType
        self.fillColor = fillColor

    def add_image(self, image):
        self.images.append(image)
        return True

    def get_canvas(self):
        return self.canvas

    def save(self):
        path = self.dirPath + "\\" + self.fileName
        self.canvas.save(path, self.atlasType)

    def show(self):
        self.canvas.show()

    def pack(self):
        self.canvas = Image.new(self.textureMode, (self.width, self.height), self.fillColor)
        for img in self.images:
            img.pack(self)
