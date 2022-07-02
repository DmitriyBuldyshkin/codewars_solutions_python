def is_valid_walk(walk):
    i = 0
    j = 0
    if len(walk) != 10:
        return False
    else:
        n = walk.count('n')
        s = walk.count('s')
        w = walk.count('w')
        e = walk.count('e')
        if (n - s) == 0 and (w - e) == 0:
            return True
        else:
            return False
