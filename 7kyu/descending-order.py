def descending_order(num):
    l = sorted([n for n in str(num)], reverse = True)
    return int("".join(l))
