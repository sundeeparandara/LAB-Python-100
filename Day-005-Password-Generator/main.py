import random

symbols = "#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
characters_lwr = "abcdefghijklmnopqrstuvwxyz"
characters_upr = characters_lwr.upper()
characters = characters_lwr+characters_upr
numbers = "1234567890"

print("Welcome to the PyPassword Generator!")
no_of_letters = int(input("How many letters would you like in your password? " ))
no_of_symbols = int(input("How many symbols would you like in your password? " ))
no_of_numbers = int(input("How many numbers would you like in your password? " ))

password = ""

for _ in range(no_of_letters):
  password += random.choice(characters)
for _ in range(no_of_symbols):
  password += random.choice(symbols)
for _ in range(no_of_numbers):
  password += random.choice(numbers)

password = list(password)
random.shuffle(password)
password = "".join(password)

print(f"Here is your password: {password}")