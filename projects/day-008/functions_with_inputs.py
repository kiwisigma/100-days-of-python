#
# def greet():
#     print(f'Hello! Welcome to the greet function!')
#     print(f'hello')
#     print(f'how are you?')
#
# greet()
#
# Functions that allows for inputs

# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How are you {name}?")
#
# greet_with_name("Billie")
# Functions with more than 1 input

def greet_with(name, location):
    print(f"Hello {name}!")
    print(f"What is it like in {location}?")
#
# greet_with("Jack Bauer", "Nowhere")
# # Positional argument
# greet_with("Nowhere", "Jack Bauer")
# Assigned keywords
greet_with(name="Angela", location="London")