def tower_builder(n_floors):
    count = 1
    amount = 1
    spaces = n_floors - 1
    res = []
    while count <= n_floors:
        res.append(' ' * spaces + '*' * amount + ' ' * spaces)
        count += 1
        amount += 2
        spaces -= 1
            
    return res
