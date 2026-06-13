def make_loud(text):
    text = text.upper()
    return text

def add_exclamation(text):
    return f"{text}!!!"

print(add_exclamation(make_loud("hello")))