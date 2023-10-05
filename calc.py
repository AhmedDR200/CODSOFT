# addition
def add(x, y):
    return x + y

# subtraction
def subtract(x, y):
    return x - y

# multiplication
def multiply(x, y):
    return x * y

# division
def divide(x, y):
    if y == 0:
        return "Cannot divide by zero."
    return x / y

# Main program
print("Simple Calculator")
print("Available operations:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

# Get user input
choice = input("Enter the operation (1/2/3/4): ")

# Check if the choice is valid
if choice in ('1', '2', '3', '4'):
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if choice == '1':
        result = add(num1, num2)
        operator = '+'
    elif choice == '2':
        result = subtract(num1, num2)
        operator = '-'
    elif choice == '3':
        result = multiply(num1, num2)
        operator = '*'
    else:
        result = divide(num1, num2)
        operator = '/'

    print(f"{num1} {operator} {num2} = {result}")
else:
    print("Invalid input. Please select a valid operation (1/2/3/4).")
