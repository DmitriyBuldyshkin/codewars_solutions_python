def wave(people):
    if len(people) == 0:
        return []
    else:
        people = people.lower()
        list = []
        for e,i in enumerate(people):
            if i == " ":
                continue
            else:
                wave = people[:e] + people[e].swapcase() + people[e+1:]
                list.append(wave)
            
        return list
