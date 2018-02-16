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
