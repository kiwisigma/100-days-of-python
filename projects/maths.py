import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
  'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print(f'Welcome to the PyPassword Generator!')
nr_letters = int(input(f"How many letters would you like in your password?\n"))


for letter in range(nr_letters):
    random_letter = random.choice(letters)
    print(f"Your password is: {random_letter}")



