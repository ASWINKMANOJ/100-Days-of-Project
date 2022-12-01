import random
from art import logo
import os

print(logo)


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(list):
    if sum(list) == 21 and len(list) == 2:
        return 0

    if 11 in list and sum(list) > 21:
        list.remove(11)
        list.append(1)

    return sum(list)


def game():
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"    Your cards: {user_cards}, current score: {user_score}")
        print(f"    Computer's first card: {computer_cards[0]}")

    while not is_game_over:
        stop = input("Type 'y' for another card 'n' to pass.\n")
        if stop == 'y':
            user_cards.append(deal_card())
            computer_cards.append(deal_card())
            user_score = calculate_score(user_cards)
            computer_score = calculate_score(computer_cards)
            print(f"    Your cards: {user_cards}, current score: {user_score}")
            new_comp = []
            for i in range(0, 2):
                new_comp.append(computer_cards[i])
            print(f"    Computer's cards: {new_comp}")
        elif stop == 'n':
            is_game_over = True
            print(f"    Your cards: {user_cards}, current score: {user_score}")
            print(f"    Computer's cards: {computer_cards}, computer's score: {computer_score}")
            if computer_score < user_score <= 21:
                print("You Win.")
            elif user_score < computer_score <= 21:
                print("You lose.")
            elif user_score < computer_score and computer_score > 21:
                print("You Win.")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
            if computer_score == 0:
                print("You Win.")
            else:
                print("You lose.")

    cont = input("Do you want to play again? Type 'y' for yes 'n' for no.\n")

    if cont == 'y':

        os.system('cls')
        print(logo)
        game()

    else:
        print("Thank You For Playing This Game.")


game()


