from itertools import groupby

def group(args):
    for _, g in groupby(enumerate(args), lambda i_x: i_x[0] - i_x[1]): # Creating a generator
        l = [x for _, x in g]
        # Yielding 
        if len(l) > 2:
            yield f"{l[0]}-{l[-1]}"
        else:
            yield from map(str, l)
            
            
def solution(args):
    return ",".join(group(args))
