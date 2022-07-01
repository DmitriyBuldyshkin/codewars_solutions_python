def driver(data):
    
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    
    firstn = data[0]
    middlen = data[1]
    surname = data[2]
    birth = data[3]
    gender = data[4]
        
    if len(surname) >= 5:
        surname = surname[0:5]
    else:
        surname = surname + "9" * (5 - len(surname)) 
        
    decade = birth[-2:-1]
    
    for i in range(12):
        if birth[3:6] == months[i]:
            if gender == "F":
                mon = str(i + 51)
            elif i >= 9:
                mon = str(i + 1)
            else:
                mon = '0' + str(i + 1)
    
    date = birth[0:2]
    year = birth[-1]
    
    if middlen == "":
        initials = firstn[0:1] + "9"
    else:
        initials = firstn[0:1] + middlen[0:1]
        
    plate = surname + decade + mon + date + year + initials + "9" + "AA"
    return plate.upper()
