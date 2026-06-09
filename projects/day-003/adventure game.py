import sys

print(r"""
                     _.--.
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           \'.  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.'\U||
            
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.-\U/.-'    o |'||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
                 '-._'-.|| |' `_.-'
                    '-.||_/.-'
""")
print("Welcome to Teasure Island!")
print("You are a pirate. A storm is appraching amd it might destroy the ship")
input("__***press enter to continue***__")

while True:
 choice1 = input(f"you can either go down into the cellar to seek shelter"
                 f"\nor jump overboard and swim to a nearby island?"
                 f"\nType 'down' or 'jump' to continue\n")
 if choice1 == "down":
     print("You have taken shelter and survived the storm!")
     break
 elif choice1 == "jump":
     print("You have decided to jump off the ship and you where killed by the tide")
     sys.exit(0)
 else:
     print("invalid choice please try again")
print('Now you come across 3 doors, which one do you enter in the cellar?\n')


while True:
    choice2 = input(f'the red door.\n'
                     f'the blue door.\n'
                     f'the green door.\n'
                     f'type "red" "blue" or "green" to continue\n')
    if choice2 == "red":
     print('You have opened the red door.\nYou have been ingulfed in an inferno and die')
     sys.exit(0)
    elif choice2 == 'blue':
        print(f'You have opened the blue door.\n'
              f'You set into the walkway and the wooden floor gives in\n'
              f'You fall into the ocean.')
        sys.exit(1)
    elif choice2 == 'green':
        print(f'You have opened the green door.\n'
              f'You find a treasure chest full of immense wealth')
        sys.exit(1)
