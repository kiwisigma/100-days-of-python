# Understanding where to declare variables relative to loops

tries = 0
while True:
    guess = int(input(f"Guess a number between 1-10."))
    if guess == 7:
        print(f"It took you {tries} to guess correctly")
        break
    elif guess != 7:
        tries += 1
