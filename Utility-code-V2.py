import random
import math

def greet_user():
    name = input("Enter your name: ")
    print(f"Hello, {name}! Welcome to the utility program.\n")
    print("Chose any of the following options: \n")
    print("1. Number Guessing Game")
    print("2. Calculator")
    print("3. Exit\n")

    try:
        choice = int(input("Enter your choice (1-3): "))
    except:
        print("Invalid input. Please enter a number between 1 and 3.")
        return
    
    if choice == 1:
        number_guessing_game()
    elif choice == 2:
        calculator()
    elif choice == 3:
        print("Thank you for using the utility program. Goodbye!")
        return
    else:
        print("Invalid choice. Please enter a number between 1 and 3.")

def number_guessing_game():
    print("\nWelcome to the Number Guessing Game!\n")
    print("Choose a difficulty level:\n")
    print("1. Very Easy (1-10, 5 attempts)")
    print("2. Easy (1-50, 7 attempts)")
    print("3. Medium (1-100, 10 attempts)")
    print("4. Hard (1-500, 15 attempts)")
    print("5. Very Hard (1-1000, 20 attempts)\n")
    try:
        level = int(input("Enter your choice (1-5): "))
    except:
        print("Invalid input. Please enter a number between 1 and 5.")
        return
    
    if level == 1:
        max_number = 10
        attempts = 5
    elif level == 2:
        max_number = 50
        attempts = 7
    elif level == 3:
        max_number = 100
        attempts = 10
    elif level == 4:
        max_number = 500
        attempts = 15
    elif level == 5:
        max_number = 1000
        attempts = 20
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
        return
    secret_number = random.randint(1, max_number)
    print(f"\nI have selected a number between 1 and {max_number}. You have {attempts} attempts to guess it.\n")
    for attempt in range(1, attempts + 1):
        try:
            guess = int(input(f"Attempt {attempt}: Enter your guess: "))
        except:
            print("Invalid input. Please enter a valid number.")
            continue
        if guess < 1 or guess > max_number:
            print(f"Please guess a number between 1 and {max_number}.")
            continue
        if guess < secret_number:
            print("Too low!\n")
        elif guess > secret_number:
            print("Too high!\n")
        else:
            print(f"Congratulations! You've guessed the number {secret_number} correctly in {attempt} attempts!\n")
            return
        print(f"Sorry, you've used all your attempts. The correct number was {secret_number}.\n")
def calculator():
    print("\nWelcome to the Calculator!\n")
    print("Choose an operation:\n")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exponentiation (^)")
    print("6. Square Root (√)\n")
    try:
        operation = int(input("Enter your choice (1-6): "))
    except:
        print("Invalid input. Please enter a number between 1 and 6.")
        return
    
    if operation in [1, 2, 3, 4, 5]:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except:
            print("Invalid input. Please enter valid numbers.")
            return
        
        if operation == 1:
            result = num1 + num2
            op_symbol = "+"
        elif operation == 2:
            result = num1 - num2
            op_symbol = "-"
        elif operation == 3:
            result = num1 * num2
            op_symbol = "*"
        elif operation == 4:
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
                return
            result = num1 / num2
            op_symbol = "/"
        elif operation == 5:
            result = num1 ** num2
            op_symbol = "^"
        
        print(f"\nResult: {num1} {op_symbol} {num2} = {result}\n")
    
    elif operation == 6:
        try:
            num = float(input("Enter the number to find the square root of: "))
        except:
            print("Invalid input. Please enter a valid number.")
            return
        
        if num < 0:
            print("Error: Cannot compute the square root of a negative number.")
            return
        
        result = math.sqrt(num)
        print(f"\nResult: √{num} = {result}\n")
    
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")

greet_user()