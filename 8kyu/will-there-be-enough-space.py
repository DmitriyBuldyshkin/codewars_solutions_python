def enough(cap, on, wait):
    res = cap - (on + wait)
    if res >= 0:
        return 0
    else:
        return -res
