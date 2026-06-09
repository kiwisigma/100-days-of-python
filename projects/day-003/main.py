print("Hello! welcome to number checker!")

print("What is the number you want to check?")

number_check = int(input())

if number_check % 2 == 0:
    print(f"{number_check} is even")
else:
    print(f"{number_check} is odd")
