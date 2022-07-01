from math import isqrt

def is_square(n): 
    if n >= 0 and isqrt(n) ** 2 == n:
        return True
    else:
        return False
