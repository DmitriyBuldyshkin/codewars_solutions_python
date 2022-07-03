def square_digits(num):
    num1 = ""
    for n in str(num):
        num1 += str(int(n) ** 2)
    return int(num1)
