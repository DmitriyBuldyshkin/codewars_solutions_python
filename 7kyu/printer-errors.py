def printer_error(s):
    res = 0
    for let in s:
        if let not in "abcdefghijklm":
            res += 1
            
    return f"{res}/{len(s)}"
