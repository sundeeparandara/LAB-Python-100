age = input("What is your current age? ")

max_years = 90

remaining_years = 90 - int(age)

remaining_months = remaining_years*12

remaining_weeks = remaining_years*52

remaining_days = remaining_years*365

print(f"You have:\n {remaining_years} years or \n {remaining_months} months or \n {remaining_weeks} weeks or\n {remaining_days} days \nremaining, based on a max age of 90 years.")