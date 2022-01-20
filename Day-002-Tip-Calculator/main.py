print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? $"))
no_of_people = int(input("How many people to split the bill? "))
pct_tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))

total_bill = total_bill*(1+(pct_tip/100))
cost_per_person = round(total_bill/no_of_people,2)

print(f"Each person should pay ${cost_per_person}")