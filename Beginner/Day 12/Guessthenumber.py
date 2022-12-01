import random
import os
from art import logo

print("Welcome to the Number Guessing Game!")
print("I,m thinking of a number between 1 and 100.")
a = random.randint(1, 101)
lives = 0


def game():
    print(logo)
    should_stop = True
    global lives
    b = input("Choose a Difficulty type. 'Easy' or 'Hard'\n").lower()

    if b == 'easy':
        lives = 10
    elif b == 'hard':
        lives = 5
    else:
        should_stop = False
        print("Input Invalid.")
        s = input("Do you want to play again? Press 'Y' for yes and any key for 'no'.").lower()
        if s == 'y':
            game()
            os.system('cls')
        else:
            return 0

    while should_stop:
        print(f"You have {lives} attempts remaining to guess the number.")
        user_guess = int(input("Make a Guess: "))
        lives -= 1

        range = abs(a - user_guess)

        if a > user_guess:
            if range > 10:
                print("Try Higher.")
            else:
                print("Try a little higher. You are close.")
        elif a < user_guess:
            if range > 10:
                print("Try Lower.")
            else:
                print("Try little lower. You are close.")
        elif a == user_guess:
            print("You got the Number Right.")
            should_stop = False
            s = input("Do you want to play again? Press 'Y' for yes and any key for 'no'.").lower()
            if s == 'y':
                game()
                os.system('cls')
            else:
                return 0

        if lives == 0:
            should_stop = False
            s = input("Do you want to play again? Press 'Y' for yes and any key for 'no'.").lower()
            if s == 'y':
                os.system('cls')
                game()

            else:
                return 0


game()
