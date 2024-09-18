operator = input("Enter an operator (+, - , * /): ")
number1 = int(input("Enter the 1st number: "))
number2 = int(input("Enter the 2nd number: "))
result = int(0)

if operator == "+":
    result = number1 + number2
    print(result)
elif operator == "-":
    result = number1 - number2
    print(result)
elif operator == "*":
    result = number1 * number2
    print(result)
elif operator == "/":
    result = number1 / number2
    print(result)
else:
    print(f"{operator} is not valid operator !!!")