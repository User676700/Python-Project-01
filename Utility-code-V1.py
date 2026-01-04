import random
import math

name = input("Please enter your name: ")
print("Hello! ", name, ", lets begin.")
print("")
print("Please choose any option you want to do, else type quit")
print("")
print("1. Guesser")
print("2. Calculator")
print("3. Exit")

while True:
    Choice = int(input("Sir please enter your choice by a number [1, 2, 3,] : "))
    
    if Choice == 1:
        print("You have choosen ' Guesser' then continue...")
        print("")
        print("")
        print("Please choose a difficulty level: ")
        print("")
        print("1. Easy (1-10)")
        print("2. Medium (1-50)")
        print("3. Hard (1-100)")
        print("4. Immpossible (1-1000)")
        Diff_Lvl = int(input("Enter any four of number: "))
        while Diff_Lvl < 1 or Diff_Lvl > 4:
            print("Invalid choice, please select a valid difficulty level.")
            Diff_Lvl = int(input("Enter any four of number: "))
        if Diff_Lvl == 1:
            print("Easy level? start then.")
            easy_number = random.randint(1, 10)
            your_number = int(input("Please guess the number:"))
            if your_number == easy_number:
                print("congrats! you guessed it right.")
            elif your_number < easy_number:
                print("Sorry! your guess was lower then number. The number was ", easy_number)
            else:
                print("Sorry! your guess was higher then number. The number was ", easy_number)
        elif Diff_Lvl == 2:
            print("Medium level? start then.")
            medium_number = random.randint(1, 50)
            your_number = int(input("Please guess the number:"))
            if your_number == medium_number:
                print("congrats! you guessed it right.")
            elif your_number < medium_number:
                print("Sorry! your guess was lower then number. The number was ", medium_number)
            else:
                print("Sorry! your guess was higher then number. The number was ", medium_number)
        elif Diff_Lvl == 3:
            print("Hard level? start then.")
            hard_number = random.randint(1, 100)
            your_number = int(input("Please guess the number:"))
            if your_number == hard_number:
                print("congrats! you guessed it right.")
            elif your_number < hard_number:
                print("Sorry! your guess was lower then number. The number was ", hard_number)
            else:
                print("Sorry! your guess was higher then number. The number was ", hard_number)
        elif Diff_Lvl == 4:
            print("Impossible level? start then.")
            impossible_number = random.randint(1, 1000)
            your_number = int(input("Please guess the number:"))
            if your_number == impossible_number:
                print("congrats! you guessed it right.")
            elif your_number < impossible_number:
                print("Sorry! your guess was lower then number. The number was ", impossible_number)
            else:
                print("Sorry! your guess was higher then number. The number was ", impossible_number)   
        else:
            print("Invalid choice, please select a valid difficulty level.")
            print("")

    elif Choice == 2:
        print("You have choosen ' Calculator' then continue...")
        print("")
        print("Please choose any operation you want to do: ")
        print("")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Square Root")
        print("6. Power")
        print("7. Logarithm")
        print("8. Modulus (Remainder)")
        print("9. Sine")
        print("10. Cosine")
        print("11. Tangent")
        Operation = int(input("Enter any number from 1 to 11: "))
        while Operation < 1 or Operation > 11:
            print("Invalid choice, please select a valid operation.")
            Operation = int(input("Enter any number from 1 to 11: "))
        if Operation == 1:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            print("The sum is: ", a + b)
        elif Operation == 2:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            print("The difference is: ", a - b)
        elif Operation == 3:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            print("The product is: ", a * b)
        elif Operation == 4:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            if b != 0:
                print("The quotient is: ", a / b)
            else:
                print("Error! Division by zero.")
        elif Operation == 5:
            a = float(input("Enter the number: "))
            if a >= 0:
                print("The square root is: ", math.sqrt(a))
            else:
                print("Error! Cannot compute square root of negative number.")
        elif Operation == 6:
            a = float(input("Enter the base number: "))
            b = float(input("Enter the exponent number: "))
            print("The result is: ", math.pow(a, b))
        elif Operation == 7:
            a = float(input("Enter the number: "))
            if a > 0:
                print("The logarithm is: ", math.log(a))
            else:
                print("Error! Logarithm undefined for non-positive numbers.")
        elif Operation == 8:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            if b != 0:
                print("The remainder is: ", a % b)
            else:
                print("Error! Division by zero.")
        elif Operation == 9:
            a = float(input("Enter the angle in degrees: "))
            angle_rad = math.radians(a)
            print("The sine is: ", math.sin(angle_rad))
        elif Operation == 10:
            a = float(input("Enter the angle in degrees: "))
            angle_rad = math.radians(a)
            print("The cosine is: ", math.cos(angle_rad))
        elif Operation == 11:
            a = float(input("Enter the angle in degrees: "))
            angle_rad = math.radians(a)
            print("The tangent is: ", math.tan(angle_rad))

    elif Choice == 3:
        print("Exiting the program. Goodbye!")
        break
    
    else:
        print("Invalid choice, please select [1, 2, or 3].")
        continue