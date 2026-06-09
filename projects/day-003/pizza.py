print("Welcome to Python Pizza Deliveries!")
input()
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

# workout how much they need to pay based on their size choice
bill = 0
if size == "S":
    b =+ 15
elif size == "M":
    b =+ 20
elif size == "L":
    b =+ 25
else:
    print("Please enter a valid size")

if pepperoni == "Y":
    if size == "S":
        bill =+ 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Your bill is {bill}")
