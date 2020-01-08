from Compound import compound
from Amortization import amortization

principal = int(input("Loan amount (ex : 200,000) = "))
asb_return = float(input("Asb return (ex : 8%) = "))
loan_interest = float(input("Loan interest (ex : 4.5%) = "))
loan_tenure = int(input("Loan tenure (ex : 30 years) = "))
year_terminate = int(input("Termination year (ex : 10 years) = "))

compounded_interest = compound(principal,year_terminate,asb_return)
loan,payment = amortization(principal,loan_interest,loan_tenure,year_terminate)

maturity = compounded_interest - loan

print("Monthly instalment :  RM %.2f" % -payment)
print("Maturity value : RM %.2f" % maturity)
