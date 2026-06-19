import art
import random
print(art.logo)

data = [
    {"name": "Cristiano Ronaldo", "follower_count": 620, "description": "Footballer", "country": "Portugal"},
    {"name": "Lionel Messi", "follower_count": 500, "description": "Footballer", "country": "Argentina"},
    {"name": "Selena Gomez", "follower_count": 420, "description": "Musician and actress", "country": "United States"},
    {"name": "Kylie Jenner", "follower_count": 395, "description": "Media personality and businesswoman", "country": "United States"},
    {"name": "Dwayne Johnson", "follower_count": 385, "description": "Actor and former wrestler", "country": "United States"},
    {"name": "Ariana Grande", "follower_count": 375, "description": "Musician", "country": "United States"},
    {"name": "Kim Kardashian", "follower_count": 360, "description": "Media personality", "country": "United States"},
    {"name": "Beyonce", "follower_count": 310, "description": "Musician", "country": "United States"},
    {"name": "Justin Bieber", "follower_count": 290, "description": "Musician", "country": "Canada"},
    {"name": "Taylor Swift", "follower_count": 280, "description": "Musician", "country": "United States"},
    {"name": "Khloé Kardashian", "follower_count": 305, "description": "Media personality", "country": "United States"},
    {"name": "Zendaya", "follower_count": 175, "description": "Actress and musician", "country": "United States"},
    {"name": "Kevin Hart", "follower_count": 170, "description": "Comedian and actor", "country": "United States"},
    {"name": "Nicki Minaj", "follower_count": 215, "description": "Musician", "country": "Trinidad and Tobago"},
    {"name": "LeBron James", "follower_count": 155, "description": "Basketball player", "country": "United States"},
    {"name": "Cardi B", "follower_count": 155, "description": "Musician", "country": "United States"},
    {"name": "Rihanna", "follower_count": 145, "description": "Musician and entrepreneur", "country": "Barbados"},
    {"name": "Drake", "follower_count": 145, "description": "Musician", "country": "Canada"},
    {"name": "Billie Eilish", "follower_count": 110, "description": "Musician", "country": "United States"},
    {"name": "Demi Lovato", "follower_count": 85, "description": "Musician and actress", "country": "United States"},
]
"""{} - f-string placeholder
    name = "Drake"
    print(f"Hello {name}") #Hello Drake
    curly braces inside an f-string say "put the value of this variable here.
    """
"""[] - dictionary/list lookup
    person = {"name": "Drake", "country": "Canada"}
    print(person["name"])   #Drake
    print(person["country"])    #Canada
    Square brackets grab a vlue out of a dict or list by its key/index.
    """
"""Combined - f-string + dict lookup
    print(f"Hello {person['name']}")    #Hello Drake
    This structure evaluates both at once - the {} tells Python "evaluate this", and inside it
    person['name'] looks up the value.
    """
def format_person(person):
    return f"{person['name']}, a {person['description']}, from {person['country']}"

points = 0
option_a = random.choice(data)

while True:     #main game loop
    option_b = random.choice(data)
    while option_b == option_a:     # Inner loop, ensures no duplicate conflicting questions
            option_b = random.choice(data)
    print(f"Compare A: {format_person(option_a)}")
    print(art.vs)
    print(f"Compare B: {format_person(option_b)}")
    choice = input(f"Who has more followers? Type 'a' or 'b'\n")

    if choice == 'a' and option_a['follower_count'] > option_b['follower_count']:
        points += 1
        print(f"correct!")
        option_a = option_b
    elif choice == 'b' and option_b['follower_count'] > option_a['follower_count']:
        points += 1
        print(f"correct!")
        option_a = option_b
    elif choice == 'a' and option_a['follower_count'] < option_b['follower_count']:
        print(f"incorrect!")
        print(f"Your final score was:{points}")
        break
    elif choice == 'b' and option_b['follower_count'] < option_a['follower_count']:
        print(f"incorrect!")
        print(f"Your final score was:{points}")
        break