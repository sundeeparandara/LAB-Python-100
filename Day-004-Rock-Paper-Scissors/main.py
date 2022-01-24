from ascii_art import rock,paper,scissors
import random
import os

os.system("clear")

human_decision = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
# print(f"human_decision={human_decision}")
# print(type(human_decision))

computer_decision = random.randint(0,2)
# print(f"computer_decision={computer_decision}")
# print(type(computer_decision))

map = {"rock":0,"paper":1,"scissors":2}

victory = "unknown pokemon"

if (human_decision == map["rock"]) & (computer_decision == map["scissors"]):
  victory = "You win."
elif (human_decision == map["paper"]) & (computer_decision == map["rock"]):
  victory = "You win."
elif (human_decision == map["scissors"]) & (computer_decision == map["paper"]):
  victory = "You win."
elif (human_decision==computer_decision):
  victory = "Draw."
else:
  victory = "Computer wins."



ascii_art = [rock,paper,scissors]

print("\n")
print(ascii_art[human_decision])
print("\nComputer chose:\n")
print(ascii_art[computer_decision])
print("\n")
print(victory)
