import string

def is_pangram(s):
    x = s.lower()
    for let in "abcdefghijklmnopqrstuvwxyz":
        if let not in x:
            return False
        
    return True
