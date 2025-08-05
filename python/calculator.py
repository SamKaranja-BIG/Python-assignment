import operator
# Dictionary mapping operation symbols to functions
operations = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv
}

# Get user input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
op = input("Enter the operation (+, -, *, /): ")

# Check if the operation is valid
if op in operations:
    if op == "/" and num2 == 0:
        print("Error: Division by zero is not allowed.")
    else:
        result = operations[op](num1, num2)
        print(f"{num1} {op} {num2} = {result}")
else:
    print("Invalid operation. Please enter one of +, -, *, /.")
