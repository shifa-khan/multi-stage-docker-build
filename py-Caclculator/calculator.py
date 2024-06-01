def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."

def calculator():
    print("Simple Python Calculator")
    print("Operations:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    while True:
        try:
            num1 = float(input("Enter first number: "))
            operation = input("Enter operation (+, -, *, /): ")
            num2 = float(input("Enter second number: "))

            if operation == '+':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif operation == '-':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif operation == '*':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif operation == '/':
                result = divide(num1, num2)
                if result == "Error! Division by zero.":
                    print(result)
                else:
                    print(f"{num1} / {num2} = {result}")
            else:
                print("Invalid operation. Please enter one of +, -, *, /.")
        except ValueError:
            print("Invalid input. Please enter numerical values.")

        next_calculation = input("Do you want to perform another calculation? (yes/no): ")
        if next_calculation.lower() != 'yes':
            print("Exiting the calculator. Goodbye!")
            break

if __name__ == "__main__":
    calculator()
