import pandas as pd
import numpy as np


def amortization(loan,rate,tenure,terminate):
    #loan = 200000
    #rate = 4.75
    #tenure = 40
    #terminate = 5

    per = np.arange(tenure*12) + 1
    per_terminate = np.arange(terminate*12) + 1
    ipmt = np.ipmt((rate/100)/12, per, tenure*12, loan)
    ppmt = np.ppmt((rate/100)/12, per, tenure*12, loan)

    pmt = np.pmt((rate/100)/12, tenure*12, loan)

    fmt = '{0:2d} {1:8.2f} {2:8.2f} {3:8.2f}'
    for payment in per_terminate:
        index = payment - 1
        loan = loan + ppmt[index]
        #print(fmt.format(payment, ppmt[index], ipmt[index], loan))

    return loan,pmt

# loan = 200000
# rate = 4.75
# tenure = 40
# terminate = 5

# loan,pmt = amortization(loan,rate,tenure,terminate)

# print(loan)
# print(pmt)