def high_and_low(numbers):
    l = numbers.split()
    l1 = [int(el) for el in l]
    res = max(l1)
    res1 = min(l1)
    return f"{res} {res1}"
