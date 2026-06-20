# dicts + nested access

toppings = {
    "cheese": 2,
    "pepperoni": 3,
    "sausage": 2,
}

pizza = {
    "size": "Large",
    "price": 12.99,
    "toppings": toppings,
}

print(pizza["price"])   #prints price
print(pizza["toppings"]["pepperoni"])   #pepperoni count
pizza["toppings"]["cheese"] -= 1