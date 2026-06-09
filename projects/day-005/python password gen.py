import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
  'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print(f'Welcome to the PyPassword Generator!')
nr_letters = int(input(f"How many letters would you like in your password?\n"))
nr_numbers = int(input(f"How many numbers would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like in your password?\n"))

password = ""
for letter in range(nr_letters):
    random_letter = random.choice(letters)
    password += random_letter

for number in range(nr_numbers):
    random_number = random.choice(numbers)
    password += random_number

for symbol in range(nr_symbols):
    random_symbols = random.choice(symbols)
    password += random_symbols

password_list = list(password)
random.shuffle(password_list)
password = "".join(password_list)
print(f"Your new password is: {password}")