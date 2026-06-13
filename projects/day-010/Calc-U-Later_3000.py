import art
print(art.logo)
print(f"Welcome to the Calc-U-Later 3000!")

def add(n1, n2):
    return n1 + n2
# Write out the other 3 functions - subtract, divide, multiply

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

# Operations
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

# Use the dictionary operations to perform the calculations,
# print(operations["*"](4, 8))
def calculator():
    should_accumulate = True
    num1 = float(input("What is the first number?: "))

    while should_accumulate:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What is the next number?: "))
        answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer}, or 'n' to start a new calculation: ")

        if choice == 'y':
            num1 = answer
        else:
            should_accumulate = False
            print("\n" * 20)
            calculator()


calculator()

