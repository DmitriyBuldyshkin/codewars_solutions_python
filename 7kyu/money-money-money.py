def calculate_years(principal, interest, tax, desired):
    count = 0
    while principal < desired:
        count += 1
        get_interest = principal * interest
        pay_tax = get_interest * tax
        principal = principal + (get_interest - pay_tax)
        
    return count
