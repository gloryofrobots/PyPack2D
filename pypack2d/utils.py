import glob
import os


def get_low_pow2(x):
    y = 2
    if y > x:
        return None
    while True:
        if y >= x:
            return y / 2

        y *= 2


def get_nearest_pow2(x):
    y = 1
    if y > x:
        return None
    while True:
        if y >= x:
            return y

        y *= 2


def max_sort(val1, val2, first, second):
    if val1 > val2:
        return first, second

    return second, first


def min_sort(val1, val2, first, second):
    if val1 < val2:
        return first, second

    return second, first


def rotate_image(img):
    return img.rotate(-90, expand=True)


def unrotate_image(img):
    return img.rotate(90, expand=True)


def extract_image_from_atlas(atlas, uv, rotated):
    width, height = atlas.size
    # if rotated:
    #     width,height = height, width
    uv_left, uv_top, uv_right, uv_bottom = uv
    left = width * uv_left
    top = height * uv_top
    right = width * uv_right
    bottom = height * uv_bottom
    image = atlas.crop((left, top, right, bottom))
    image.load()
    if rotated:
        image = unrotate_image(image)
    return image


def are_images_equal(im1, im2):
    from PIL import ImageChops
    # check image equality in many ways
    # it is redundant but I want to be sure
    check0 = im1.size == im2.size
    check1 = ImageChops.difference(im1, im2).getbbox() is None
    check2 = im1.tobytes() == im2.tobytes()
    return check0 is True and check1 is True and check2 is True


def clear_dir(dirname):
    for filename in glob.glob(dirname + "/*.*"):
        os.remove(filename)
