from Compound import compound
from Amortization_Schedule import amortization
from Calculator import calculate
import matplotlib.pyplot as plt

principal = int(input("Loan amount (ex : 200,000) = "))
asb_return = float(input("Asb return (ex : 8%) = "))
loan_interest = float(input("Loan interest (ex : 4.5%) = "))
loan_tenure = int(input("Loan tenure (ex : 30 years) = "))
year_terminate = int(input("Termination year (ex : 10 years) = "))

maturity,payment,ppmt,ipmt=calculate(principal,asb_return,loan_interest,loan_tenure,year_terminate)

print("Monthly instalment :  RM %.2f" % -payment)
print("Maturity value : RM %.2f" % maturity)

plt.style.use('dark_background')
fig_size = plt.rcParams["figure.figsize"]
# Set figure width to 12 and height to 9
fig_size[0] = 18
fig_size[1] = 8
plt.plot(-ppmt, 'r', label = "Principal")
plt.plot(-ipmt, 'g', label = "Interest")
plt.xlabel('Period (Month)')
plt.ylabel('Payment (RM)')
plt.legend()
plt.title('Principal vs Interest')
plt.grid()
plt.show() 
