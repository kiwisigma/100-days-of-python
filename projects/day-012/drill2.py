#Store an input, return based on it

def get_color():
    color = input(f"What is your favorite color?:\n")
    if color == "red" or color == "orange" or color == "yellow":
        return "warm"
    else:
        return "cool"

print(get_color()) 