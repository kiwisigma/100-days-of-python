import random
from art import logo

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

number = random.randint(1, 100)

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
attempts = 10 if difficulty == "easy" else 5

while attempts > 0:
    print(f"\nYou have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))

    if guess == number:
        print(f"You got it! The answer was {number}.")
        break
    elif guess < number:
        print("Too low.")
    else:
        print("Too high.")

    attempts -= 1
    if attempts > 0:
        print("Guess again.")
else:
    print(f"\nYou've run out of guesses. The answer was {number}.")
