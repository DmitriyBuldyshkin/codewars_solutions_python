from itertools import product

def get_pins(observed):
    keypad = {
        '0': ['8'],
        '1': ['2', '4'],
        '2': ['1', '3', '5'],
        '3': ['2', '6'],
        '4': ['1', '5', '7'],
        '5': ['2', '4', '6', '8'],
        '6': ['3', '5', '9'],
        '7': ['4', '8'],
        '8': ['0', '5', '7', '9'],
        '9': ['6', '8'],
    }
    l = [[num] + keypad[num] for num in observed]
    res = ["".join(el) for el in product(*l)]
    return res
