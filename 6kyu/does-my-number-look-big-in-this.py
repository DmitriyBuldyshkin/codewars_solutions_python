def narcissistic( value ):
    x = str(value)
    digit = len(x)
    result = 0
    for num in x:
        result += int(num) ** digit
        if result == value:
            return True
    
    return False
