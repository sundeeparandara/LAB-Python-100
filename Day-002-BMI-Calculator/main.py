height = input("Enter your height in metres: ")
weight = input("Enter your weight in kilograms: ")

bmi = round(float(weight)/float(height)**2,1)

print(f"Your BMI is {bmi}")
