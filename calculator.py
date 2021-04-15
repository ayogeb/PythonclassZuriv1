def operation(first,second,operator):
    if(operator == 1):
        return first + second
    if(operator == 2):
        return first - second
    if(operator == 3):
        return first / second
    if(operator == 4):
        return first * second
    return "Invalid selection or input"

print("Welcome to calculator.py, please enter 2 values to perform an operation")
firstValue = float(input("What is the first value? \n"))
secondValue = float(input("What is the second value? \n"))

print("Available Operations")
print("1. add- Add two numbers")
print("2. sub- Subtract two numbers")
print("3. div- Divide Add two numbers")
print("4. mul- Multiply two numbers")

operator = int(input("What operation would you like to perform? \n"))

print(operation(firstValue, secondValue, operator))