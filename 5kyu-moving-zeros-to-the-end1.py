def move_zeros(array):
    res = [el for el in array if el > 0]
    zeros = [el for el in array if el == 0]
    return res + zeros
