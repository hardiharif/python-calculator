import art

print(art.logo)

#Subtract multiply, add divide
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operation_symbols = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculate():
    calculating = True

    first_number = float(input("Enter your first number: "))

    while calculating:
        for symbol in operation_symbols:
            print(symbol)

        users_operator = input("Choose an operator: ")

        while users_operator not in operation_symbols:
            print('You typed the wrong operator')
            users_operator = input("Choose an operator: ")

        second_number = float(input("enter your second number: "))

        while users_operator == '/' and second_number == 0:
            print("cannot divide by zero")
            second_number = float(input("enter your second number: "))

        result = operation_symbols[users_operator](first_number, second_number)

        print(f"{first_number} {users_operator} {second_number} = {result}")

        approval_for_continuation = input(f"Type y to continue your calculations with {result}  (Type n for no): ")

        if approval_for_continuation == "y":
            first_number = result
        else:
            calculating = False
            print('\n' * 20)

            calculate()

calculate()