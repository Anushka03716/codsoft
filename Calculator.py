operator = input("Enter an operator:('+','-','/','*'): ")
number1 = float(input("Enter 1st number: "))
number2 = float(input("Enter 2nd number: "))

if operator == "+":
    result = number1 + number2
    print(result)
elif  operator == "-":
    result = number1 - number2  
    print(result)
elif  operator == "/":
    result = number1 / number2  
    print(result)
elif  operator == "*":
    result = number1 * number2 
    print(result)
else:
    print("Invalid Input")