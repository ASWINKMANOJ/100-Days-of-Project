from game_data import data
import random
from art import logo
from art import vs
import os


def format_data(account):
    """Takes the account data and returns the printable format."""
    name = account["name"]
    country = account["country"]
    des = account["description"]
    return f"{name}, a {des} from {country}"


def check_answer(guess, f_followers, s_follower):
    """Take the user guess and follower counts and returns if they got it right"""
    if f_followers > s_follower:
        return guess == "a"
    else:
        return guess == "b"


def game():
    score = 0

    game_should_continue = True
    s = random.choice(data)

    while game_should_continue:
        print(logo)
        f = s

        while f == s:
            s = random.choice(data)
        print(f"Compare A: {format_data(f)}")
        print(vs)
        print(f"Against B: {format_data(s)}")

        guess = input("Who has more follower? Type 'A' or 'B': ").lower()

        f_count = f["follower_count"]
        s_count = s["follower_count"]

        is_correct = check_answer(guess, f_count, s_count)

        os.system('cls')

        if is_correct:
            score += 1
            print(f'You got it right. Your score is {score}')

        else:
            print(f"Sorry that's wrong. Your score is {score}")
            game_should_continue = False

    gamer = input("Do you want to play again? 'Y' for yes 'N' for no.").lower()
    if gamer == 'y':
        os.system('cls')
        game()
    else:
        input("Thank you for playing. Press Enter to exit")


game()
