import numpy as np

def amortization(loan,rate,tenure,terminate):

    per = np.arange(tenure*12) + 1
    per_terminate = np.arange(terminate*12) + 1
    ipmt = np.ipmt((rate/100)/12, per, tenure*12, loan)
    ppmt = np.ppmt((rate/100)/12, per, tenure*12, loan)

    pmt = np.pmt((rate/100)/12, tenure*12, loan)

    balance = []
    fmt = '{0:2d} {1:8.2f} {2:8.2f} {3:8.2f}'
    for payment in per_terminate:
        index = payment - 1
        loan = loan + ppmt[index]
        balance.append(loan) 
        #print(fmt.format(payment, ppmt[index], ipmt[index], balance[index]))

    return balance,pmt,ppmt,ipmt











