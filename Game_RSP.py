import sys
import random
from enum import Enum


# Game of Rock, Scissors & Paper.
class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

# Input number in the terminal //  Rock = 1, Scissors = 2 & Paper = 3
playerchoice = input("Enter...\n1 for Rock, \n2 for Paper, or \n3 for Scissors:\n\n")

player = int(playerchoice)

if player < 1 | player > 3:
    print("You must enter 1, 2, or 3.")

# Random module.
computerchoice = random.choice("123")

computer = int(computerchoice)

print("")
print("You chose " + str(RPS(player)).replace("RPS.", "") + ".")
print("Python chose " + str(RPS(computer)).replace("RPS.", "") + ".")
print("")

if player == 1 and computer == 3:
    print("You Win!")
elif player == 2 and computer == 1:
    print("You Win!")
elif player == 3 and computer == 2:
    print("You Win!")
elif player == computer:
    print("Tie game!")
else:
    print("Python Wins!")