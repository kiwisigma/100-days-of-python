
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,    #milliliters
            "milk": 0,      #milliliters
            "coffee": 18,   #grams
        },
        "cost": 1.50,   #dollars
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.50,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.00,
    },
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}


def is_resource_sufficent(order_ingredients):
    """Return True if the machine can make the drink."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def process_coins():
    """Ask for coins, return total dollar value, showing a running total."""
    print("Please insert coins.")
    total = 0
    for coin, value in [("quarters", 0.25), ("dimes", 0.10), ("nickels", 0.05), ("pennies", 0.01)]:
        total += int(input(f"How many {coin}?: ")) * value
        print(f"Total so far: ${total:.2f}")
    return total

def transaction_successful(money_received, drink_cost):
    """Return True if paid enough; handle change + bank profit."""
    if money_received < drink_cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    change = round(money_received - drink_cost, 2)
    if change > 0:
        print(f"Here is ${change:.2f} dollars in change.")
    resources["money"] += drink_cost
    return True

def make_coffee(drink_name, order_ingredients):
    """Deduct ingredients and serve."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}. Enjoy! ☕")

is_on = True
while is_on:
    choice = input("What type of coffee would you like?\nespresso?\nlatte?\ncappuccino?\n")

    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${resources['money']:.2f}")
    elif choice in MENU:
        drink = MENU[choice]
        if is_resource_sufficent(drink["ingredients"]):
            print(f"{choice.title()} costs ${drink['cost']:.2f}.")
            payment = process_coins()
            if transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
