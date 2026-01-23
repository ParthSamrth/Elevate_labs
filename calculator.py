def add(a, b=0):
    """Returns the sum of two numbers."""
    return a + b


def subtract(a, b=0):
    """Returns the difference of two numbers."""
    return a - b


def multiply(a, b=1):
    """Returns the product of two numbers."""
    return a * b


def divide(a, b=1):
    """Returns the division of two numbers. Handles division by zero."""
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b


def calculator():
    """Main calculator function"""

    print("----- Simple Modular Calculator -----")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter your choice (1-4): ")

    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if choice == "1":
        print("Result:", add(a, b))
    elif choice == "2":
        print("Result:", subtract(a, b))
    elif choice == "3":
        print("Result:", multiply(a, b))
    elif choice == "4":
        print("Result:", divide(a, b))
    else:
        print("Invalid choice")


if __name__ == "__main__":
    calculator()
