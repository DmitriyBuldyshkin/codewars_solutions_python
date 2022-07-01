from math import isqrt

def find_next_square(sq):
    res = isqrt(sq)
    if res ** 2 == sq:
        res += 1
        return res ** 2
    else:
        return -1
