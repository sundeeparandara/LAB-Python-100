f=open('treasure.txt','r')
print(''.join([line for line in f]))


print("Welcome to Treasure Island.\nYour mission is to find the treasure.\n")
decision1 = input("You're at a cross road. Where do you want to go? Type 'left' or 'right'. ").lower()
if decision1 == "left":
  decision2 = input("You've come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across. ").lower()
  if decision2 == "wait":
    decision3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? ").lower()
    if decision3 == "yellow":
      print("YOU WIN.")
    elif decision3 == "red":
      print("Burned by fire.\nGAME OVER.")
    elif decision3 == "blue":
      print("Eaten by beasts.\nGAME OVER.")
    else:
      print("GAME OVER.")
  else:
    print("Attaced by trout.\nGAME OVER.")
else:
  print("Fall into a hole.\nGAME OVER.")



