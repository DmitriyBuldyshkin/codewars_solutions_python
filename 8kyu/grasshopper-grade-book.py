def get_grade(s1, s2, s3):
    res = (s1 + s2 + s3) // 3
    if res >= 90:
        return "A"
    elif res >= 80:
        return "B"
    elif res >= 70:
        return "C"
    elif res >= 60:
        return "D"
    else:
        return "F"
