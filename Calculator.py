from Compound import compound
from Amortization_Schedule import amortization

def calculate(principal,asb_return,loan_interest,loan_tenure,year_terminate):
    compounded_interest = compound(principal,year_terminate,asb_return)
    balance,payment,ppmt,ipmt = amortization(principal,loan_interest,loan_tenure,year_terminate)

    maturity = compounded_interest - balance[year_terminate*12 - 1]
    return maturity,payment,ppmt,ipmt
