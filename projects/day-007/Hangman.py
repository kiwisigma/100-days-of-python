import random
word_list = ["avalanche"]
guessed_letters = []
print(r"""
   _   _    _    _   _  ___  __  __    _    _   _
  | | | |  / \  | \ | |/ _ \|  \/  |  / \  | \ | |
  | |_| | / _ \ |  \| | | | | |\/| | / _ \ |  \| |
  |  _  |/ ___ \| |\  | |_| | |  | |/ ___ \| |\  |
  |_| |_/_/   \_\_| \_|\___/|_|  |_/_/   \_\_| \_|
""")

lives = 6
chosen_word = random.choice(word_list)
display = ["_" for letter in chosen_word]
print(" ".join(display))

print(f"Hello! welcome to Hangman!")
input(f'please press enter to continue')
placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)
print(f"Guessed letters: {guessed_letters}")


while "_" in display and lives > 0:
  guess = (input("Please choose a letter!\n".lower()))

  if guess in guessed_letters:
    print(f"you already guessed {guess}!")
  elif guess in chosen_word:
    print("Right")
    guessed_letters.append(guess)
  else:
    print("Wrong")
    lives -= 1
    print(f"Lives remaining: {lives}")
    guessed_letters.append(guess)

  guessed_letters.append(guess)
  print(f"Guessed letters: {guessed_letters}")

  for position, letter in enumerate(chosen_word):
      if letter == guess:
        display[position] = guess
  print(" ".join(display))

if lives == 0:
  print(f"You lost! The word was: {chosen_word}")
else:
  print(f"You won! The word was: {chosen_word}")
