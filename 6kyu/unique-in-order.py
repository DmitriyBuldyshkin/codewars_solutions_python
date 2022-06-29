def unique_in_order(iterable):
    l = []
    for i, el in enumerate(iterable):
        if el not in l:
            l.append(el)
        elif el in l and iterable[i-1] == iterable[i]:
            pass
        else:
            l.append(el)
    return l
