import random
import math
import cmath

print("Welcome to the Utility Code V3!")
print("This utility includes various games and quizzes.")
def main_menu():
    print("Please select an option: \n")
    print("1. Number Guessing Game")
    print("2. Quiz")
    print("3. Rock, Paper, Scissors Game")

    choice = input("Enter the number of your choice (or 'q' to quit): ")
    if choice == '1':
        number_guessing_game()
    elif choice == '2':
        quiz()
    elif choice == '3':
        rock_paper_scissors()
    elif choice.lower() == 'q':
        print("Thank you for using the Utility Code V3. Goodbye!")
    else:
        print("Invalid choice. Please try again.")
        main_menu()

def number_guessing_game():
    print("\nWelcome to the Number Guessing Game!")
    print("Here you have to choose a difficulty level: \n")
    print("1. very easy (1-5)")
    print("2. easy (1-10)")
    print("3. medium (1-20)")
    print("4. hard (1-50)")
    print("5. very hard (1-100)")

    try:
        diff_lvl = int(input("Enter the number of your choice: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        number_guessing_game()
        return
    if diff_lvl == 1:
        max_num = 5
    elif diff_lvl == 2:
        max_num = 10
    elif diff_lvl == 3:
        max_num = 20
    elif diff_lvl == 4:
        max_num = 50
    elif diff_lvl == 5:
        max_num = 100
    else:
        print("Invalid choice. Please try again.")
        number_guessing_game()
        return
    secret_number = random.randint(1, max_num)
    attempts = 0
    while True:
        try:
            guess = int(input(f"Guess a number between 1 and {max_num}: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        attempts += 1
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number {secret_number} in {attempts} attempts.")
            break
    if input("Do you want to play again? (y/n): ").lower() == 'y':
        number_guessing_game()
    else:
        main_menu()

def quiz():
    print("\nPlease select a type of quize:")
    print("1. Basic Math Quiz")
    print("2. fruit Quiz")
    choice = input("Enter the number of your choice (or 'q' to quit): ")
    
    while True:
        if choice == 1:
            print("You have selected Basic Math Quiz.")
            print("Answer the following questions:")
            score = 0
            question_number_a = random.randint(1,20)
            question_number_b = random.randint(1,20)
            op = random.choice(['+', '-', '*', '/'])
            if op == '+':
                answer = question_number_a + question_number_b
            elif op == '-':
                answer = question_number_a - question_number_b
            elif op == '*':
                answer = question_number_a * question_number_b
            elif op == '/':
                answer = question_number_a / question_number_b
            user_answer = float(input(f"What is {question_number_a} {op} {question_number_b}? "))
            if user_answer == answer:
                print("Correct!")
                score += 1
            else:
                print(f"Incorrect! The correct answer is {answer}.")
            print(f"Your final score is {score}/1.")
            break
        if choice == 2:
            print("You have sel")