def solution(s):
    res = []
    l = [let for let in s]
    for el in l:
        if el.isupper():
            res.append(" ")
            res.append(el)
        else:
            res.append(el)
            
    return "".join(res)
