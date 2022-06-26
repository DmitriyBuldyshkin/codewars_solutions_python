def count(string):
    res = {}
    for let in string:
        if let in res:
            res[let] += 1
        else:
            res[let] = 1
    return res
