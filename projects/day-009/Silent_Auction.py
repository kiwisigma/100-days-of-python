bids = {}
highest_bid = 0
winner = ""

while True:
    name = input("What is your name?")
    price = int(input("What is your bid?"))
    bids[name] = price
    should_continue = input("Are there other bidders? yes/no: ")
    if should_continue == "yes":
        print("\n"*20)
    else:
        break

for name, bid in bids.items():
    if bid > highest_bid:
        highest_bid = bid
        winner = name
    else


