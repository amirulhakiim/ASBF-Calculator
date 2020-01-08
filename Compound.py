def compound(principal,period,rate):
    # Calculates compound interest  
    CI = principal * (pow((1 + rate / 100), period)) 
    #print("Compound interest is", CI) 
    return CI

