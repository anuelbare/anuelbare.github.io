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
game = ["rock", "paper", "scissors"]
choice = input("What do you want to play? ")
side = random.choice(game)
print(side)

#choice rock
if (choice == "rock" or choice == "Rock" or choice == "ROCK") and side == "rock":
    print("Draw")
elif (choice == "rock" or choice == "Rock" or choice == "ROCK") and side == "scissors":
    print("You win")
elif (choice == "rock" or choice == "Rock" or choice == "ROCK") and side == "paper":
    print(paper)

#choice scissors
if (choice == "scissors" or choice == "Scissors" or choice == "SCISSORS") and side == "rock":
    print(rock)
elif (choice == "scissors" or choice == "Scissors" or choice == "SCISSORS") and side == "scissors":
    print("Draw")
elif (choice == "scissors" or choice == "Scissors" or choice == "SCISSORS") and side == "paper":
    print("You win")

#choice paper
if (choice == "paper" or choice == "Paper" or choice == "PAPER") and side == "rock":
    print("You win")
elif (choice == "paper" or choice == "Paper" or choice == "PAPER") and side == "scissors":
    print(scissors)
elif (choice == "paper" or choice == "Paper" or choice == "PAPER") and side == "paper":
    print("Draw")