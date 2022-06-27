def dirReduc(arr):
    opposite = {"NORTH": "SOUTH", "SOUTH": "NORTH", "EAST": "WEST", "WEST": "EAST"}
    res = []
    for el in arr:
        if res and opposite[el] == res[-1]:
            res.pop()
        else:
            res.append(el)
            
    return res
