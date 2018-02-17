from PIL import Image, ImageDraw
import random
import os

"""
you can use this script to generate test images for atlas packer
also it will create necessary folders
"""
COLORS = []
for i in range(1000):
    r = random.randrange(0, 255)
    g = random.randrange(0, 255)
    b = random.randrange(0, 255)
    COLORS.append((r, g, b))

SIZES = [100, 60, 30, 180, 200, 10, 2, 140, 70, 50]

# PRESETS = [(510, 10), (10, 510), (100, 100), (2, 10), (10,2), (10, 10)]
PRESETS = [(x * 10, y * 10) for x, y in [(2, 10), (10, 2), (10, 10), (5, 5)]]


# PRESETS = [(x*10, y*10) for x,y in [(2, 5)]]


def make_path(dirname, index):
    return os.path.join(dirname, "%d.png" % index)


def generate_image(filename, size):
    color = random.choice(COLORS)
    canvas = Image.new("RGBA", size, color=color)
    canvas.save(filename)
    return canvas


def generate(dirname, max_count):
    def randsize():
        size = lambda x: random.choice(SIZES) + random.randrange(1, x)
        return size(10), size(10)

    images = [randsize() for _ in range(max_count)]
    images = PRESETS + images

    for index, size in enumerate(images):
        if index >= max_count:
            return
        name = make_path(dirname, index)
        generate_image(name, size)


if __name__ == "__main__":
    dirs = ["img/unpacked", "img/test", "img/atlas"]
    for path in dirs:
        try:
            os.makedirs(path)
        except os.error as e:
            # dir already exists
            pass

    generate("img/test", len(PRESETS))
