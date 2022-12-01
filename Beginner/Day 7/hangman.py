import random

from hangman_list import word_list

from hangman_art import stages

from hangman_art import logo

import os



print(logo)

chosen_word = random.choice(word_list)

word_length = int(len(chosen_word))


display = []

display += "_"*word_length

lives = len(stages)

end_of_game = False

while not end_of_game:
    guess = input("Guess the word: ").lower()

    os.system('cls')

    if guess in display:
        print(f"You already guessed {guess}.")

    for position in range(word_length):
        letter = chosen_word[position]

        if guess == letter:
            display[position] = letter

    if guess not in chosen_word:
        print(f"Your guess {guess} is not in the word")
        lives -= 1

        if lives == 0 :
            print("You lose.")
            end_of_game = True

    print(f"{''.join(display)}")

    if "_" not in display:
        print("You win.")
        end_of_game = True
        print(display)


    print(stages[lives])

if end_of_game:
    input("Type Enter to Close the Game.")






