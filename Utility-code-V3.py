import random
import math
import cmath

print("Welcome to the Utility Code V3!")
print("This utility includes various games and quizzes.")
def main_menu():
    while True:
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
            break
        else:
            print("Invalid choice. Please try again.")

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
        return

def quiz():
    print("\nPlease select a type of quize:")
    print("1. Basic Math Quiz")
    print("2. fruit Quiz")
    print("3. Advanced Math Quiz")
    choice = input("Enter the number of your choice (or 'q' to quit): ")
    
    if choice == '1':
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
    elif choice == '2':
        print("You have selected fruit quiz.")
        fruits = {
            "apple": "A round fruit that is typically red, green, or yellow.",
            "banana": "A long yellow fruit that is high in potassium.",
            "orange": "A round citrus fruit known for its vitamin C content.",
            "grape": "A small, round fruit that grows in bunches on vines.",
            "strawberry": "A red fruit with tiny seeds on its surface and a sweet flavor.",
            "Watermelon": "A large fruit with a green rind and sweet, juicy red or pink flesh."
        }
        score = 0
        print("Answer the following questions:")
        guessed_fruit = random.choice(list(fruits))
        user_input = input(f"Guess the fruit by its description: {fruits[guessed_fruit]}\nYour answer: ")
        if user_input.lower() == guessed_fruit.lower():
            print("You Got it Right!")
            score += 1
        else:
            print(f"Wrong Answer! The correct answer is {guessed_fruit}.")
        print(f"Your final score is {score}/1.")
    elif choice == '3':
        print("You Have Selected Advanced Math Quiz.")
        print("Answer the following questions:")
        score = 0
        question_number_a = random.randint(1,20)
        question_number_b = random.randint(1,20)
        op = random.choice(['*', '/', '%', 'square', 'cube'])
        if op == '*':
            answer = question_number_a * question_number_b
            user_answer = float(input(f"What is {question_number_a} {op} {question_number_b}? "))
        elif op == '/':
            answer = question_number_a / question_number_b
            user_answer = float(input(f"What is {question_number_a} {op} {question_number_b}? "))
        elif op == '%':
            answer = question_number_a % question_number_b
            user_answer = float(input(f"What is {question_number_a} {op} {question_number_b}? "))
        elif op == 'square':
            answer = question_number_a ** 2
            user_answer = float(input(f"What is the square of {question_number_a}? "))
        elif op == 'cube':
            answer = question_number_a ** 3
            user_answer = float(input(f"What is the cube of {question_number_a}? "))
        if user_answer == answer:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect! The correct answer is {answer}.")
        print(f"Your final score is {score}/1.")
    elif choice.lower() == 'q':
        return
    else:
        print("Invalid choice.")
        quiz()

def rock_paper_scissors():
    print("\n Welcome to Rock, Paper, Scissors Game!")
    choices = ['rock', 'paper', 'scissors']
    user_score = 0
    computer_score = 0
    while True:
        user_choice = input("Enter rock, paper, or scissors (or 'q' to exit):")
        if user_choice.lower() == 'q':
            break
        elif user_choice.lower() not in choices:
            print("Invalid choice. Please try again.")
            continue
        computer_choice = random.choice(choices)
        if user_choice == computer_choice:
            print(f"Both selected {user_choice}. It's a tie!")
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'paper' and computer_choice == 'rock') or \
             (user_choice == 'scissors' and computer_choice == 'paper'):
            print(f"You win! {user_choice} beats {computer_choice}.")
            user_score += 1
        else:
            print(f"You lose! {computer_choice} beats {user_choice}.")
            computer_score += 1
        print(f"Score: You {user_score} - Computer {computer_score}")

if __name__ == "__main__":
    main_menu()
