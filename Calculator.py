def add(op, num1, num2):
    if op == "+":
        print(f"The sum of {num1} and {num2} is {num1+num2}")
    elif op == "-":
        print(f"The difference between {num1} and {num2} is {num1-num2}")
    elif op == "*":
        print(f"The product when {num1} is multiplied by {num2} is {num1*num2}")
    elif op == "**":
        print(f"The result when the power of {num1} is {num2} is {num1**num2}")
    elif op == "/":
        print(f"The quotient when {num1} is divided by {num2} is {num1/num2}")
    elif op == "%":
        print(f"The remainder when {num1} is divided by {num2} is {num1%num2}")
    elif op == "//":
        print(f"The nearest number which cuts {num1} by {num2} excatly is {num1//num2}")
    else:
        print("Please select one from these given operators: +, -, *, **, /, %, //\n")

operator = input("Enter the operator here to choose what you want to do. The options are +, -, *, **, /, %, //. \n")
a = int(input("Enter the number here\n"))
b = int(input("Enter another number here\n"))
add(operator, a, b)