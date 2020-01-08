def do_calculation(num1,num2):
    return num1+num2

number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))
solution = do_calculation(number1,number2)

print("The solution is {}".format(solution))