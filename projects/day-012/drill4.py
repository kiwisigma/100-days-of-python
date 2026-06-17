#looping inside a counter
guess_count = 0

while True:
    v = input(f"guess a number:\n")
    guess_count += 1
    if int(v) == 42:
        print(guess_count)
        break
    else:
        print(f"Try again")