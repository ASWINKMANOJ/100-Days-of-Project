import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choices = [rock, paper, scissors]

user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors."))

computer = random.randint(0, 2)

print("Computer chose: \n" + choices[computer])

if user_input <= 2:
    print("You chose \n" + choices[user_input])
else:
    x = 2

if user_input == 0 and computer == 1:
    print("You Lost.")
elif user_input == 0 and computer == 2:
    print("You Won.")
elif user_input == 1 and computer == 0:
    print("You Won.")
elif user_input == 1 and computer == 2:
    print("You Lost.")
elif user_input == 2 and computer == 0:
    print("You Lost.")
elif user_input == 2 and computer == 1:
    print("You Won.")
elif user_input >= 3 or user_input < 0:
    print("You typed an invalid Number.You Lost.")
else:
    print("It's a Tie.")

input("Type Enter to Close.")