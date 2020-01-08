def compound(principal,period,rate):
    CI = principal * (pow((1 + rate / 100), period)) 
    return CI

