# Task 5: Modular Calculator Program

def add(a, b=0):
    """Returns the sum of two numbers. Default b is 0."""
    return a + b

def subtract(a, b=0):
    """Returns the difference of two numbers."""
    return a - b

def multiply(a, b=1):
    """Returns the product of two numbers. Default b is 1."""
    return a * b

def divide(a, b):
    """Returns the division result. Handles division by zero error."""
    if b == 0:
        return "Error: Cannot divide by zero!"
    return a / b

def show_menu():
    """Displays the options to the user."""
    print("\n--- Modular Calculator ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

def get_user_input():
    """Separated logic for getting and validating user numbers."""
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        return num1, num2
    except ValueError:
        print("Invalid input! Please enter numeric values.")
        return None, None

def main():
    """Main function to control the program flow."""
    while True:
        show_menu()
        choice = input("Select an option (1-5): ")

        if choice == '5':
            print("Exiting... Goodbye!")
            break

        if choice in ['1', '2', '3', '4']:
            n1, n2 = get_user_input()
            
            if n1 is None: continue # Skip if input was invalid

            if choice == '1':
                print(f"Result: {add(n1, n2)}")
            elif choice == '2':
                print(f"Result: {subtract(n1, n2)}")
            elif choice == '3':
                print(f"Result: {multiply(n1, n2)}")
            elif choice == '4':
                result = divide(n1, n2)
                print(f"Result: {result}")
        else:
            print("Invalid choice. Please pick 1 to 5.")

# Independent Testing
if __name__ == "__main__":
    main()