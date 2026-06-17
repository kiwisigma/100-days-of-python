import art
import random
print(art.logo)
print(f"Welcome to the Number Guessing Game!")
print(f"I'm thinking of a number between 1 and 100")

def play_game():
    secret = random.randint(1, 100)
    attempts = get_difficulty()
    guess_count = 0
    while guess_count < attempts:
        guess = int(input("Make a guess: "))
        result = check_guess(guess, secret)
        guess_count += 1
        if result == "correct":
            break

def get_difficulty():
    easy_attempts = 10
    hard_attempts = 5
    choice = input("choose a difficulty. Type 'easy' or 'hard':\n")
    if choice == "easy":
        return easy_attempts
    elif choice == "hard":
        return hard_attempts

def check_guess(guess, secret):
    if guess < secret:
        print(f"Too low\n Guess again.")
        return "too_low"
    elif guess > secret:
        print(f"Too high\n Guess again.")
        return "too_high"
    elif guess == secret:
        print(f"Correct!")
        return "correct"

play_game()