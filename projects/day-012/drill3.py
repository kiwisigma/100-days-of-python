#Passing output of one function to another

def get_number():
    n = input(f"Enter a number: ")
    return int(n)

def double(n):
    d = n * 2
    return d

print(double(get_number()))
