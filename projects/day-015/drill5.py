# correct order (data, functions, loop)

def check_move(m):
    print(f"You played {m}")

VALID_MOVES = ["rock", "paper", "scissors"]
playing = True

while playing:
    move = input("Your move: ")
    if move == "quit":
        playing = False
    elif move in VALID_MOVES:
        print(check_move(move))
