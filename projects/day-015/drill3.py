# nested dictionary

car = {
    "make": "Toyota",
    "year": 2020,
    "engine": {
        "cylinders": 4,
        "horsepower": 200,
    },
}

print(car["engine"]["horsepower"])
car["engine"]["horsepower"] += 50
print(car["engine"]["horsepower"])