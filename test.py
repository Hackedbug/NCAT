import math

def calc(num1, op, num2=None): # Created a function for basic calculator
    operators = ['+', '-', '*', '/', '%', 'sqrt', 'square root'] # List of the known operators used in maths on the calculator

    if op in operators:
        if op == "+":  # Addition
            return num1 + num2
        elif op == "-":  # Subtraction
            return num1 - num2
        elif op == "*":  # Multiplication
            return num1 * num2
        elif op == "/":  # Division
            return num1 / num2
        elif op == "%":  # Modulus
            return num1 % num2
        elif op == "sqrt" or op == "square root":
            return math.sqrt(num1)
    else:  # For if the "operator" provided by the user is not among the list
        return "Error occurred in the calculation. " + op + " is an Invalid Operator"

num1 = float(input("Enter the first number: "))  # For the user to input the first number
op = input("Enter the operator: ")  # For the user to input the operator

# Only ask for the second number if the operation is not square root
if op not in ["sqrt", "square root"]:
    num2 = float(input("Enter the second number: "))  # For the user to input the second number
    print(calc(num1, op, num2))
else:
    print(calc(num1, op))
