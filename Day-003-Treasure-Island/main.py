f=open('treasure.txt','r')
print(''.join([line for line in f]))


print("Welcome to Treasure Island.\nYour mission is to find the treasure.\n")
decision1 = input("left or right? ").lower()
if decision1 == "left":
  decision2 = input("swim or wait? ").lower()
  if decision2 == "wait":
    decision3 = input("which door (red, blue or yellow)? ")
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



