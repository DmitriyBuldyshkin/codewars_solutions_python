def fake_bin(x):
    l = list(x)
    res = []
    for el in l:
        if int(el) < 5:
            res.append("0")
        else:
            res.append("1")
            
    return "".join(res)
