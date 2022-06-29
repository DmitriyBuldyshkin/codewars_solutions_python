def open_or_senior(data):
    res = []
    for pers in data:
        if pers[0] > 54 and pers[1] > 7:
            res.append('Senior')
        else:
            res.append('Open')
            
    return res
