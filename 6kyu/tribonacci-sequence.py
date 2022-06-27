def tribonacci(signature, n):
    if n == 0:
        return []
    if n < 3:
        return signature[:n]
    else:
        table = [0] * n 
        table[0], table[1], table[2] = signature
        for i in range(3, n):
            table[i] = table[i - 1] + table[i - 2] + table[i - 3]

        return table
