import random

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
computer_options = [scissors, rock, paper,]
images = [rock, scissors, paper]

print('Welcome to Rock Paper Scissors!')
print('what do you choose? Type 0 for Rock, 1 for paper or 2 for scissors.')




while True:
    computer_choice = random.choice(computer_options)
    choice = input('Type 0 for Rock, 1 for Paper, 2 for Scissors: ')
    if choice == '0':
        print(f'You chose rock!\n{rock}')
        print(f'The computer chose:\n{computer_choice}')
        if computer_choice == paper:
            print(f'The computer wins!')
            break
        elif computer_choice == scissors:
            print(f'You win!')
            break
        elif computer_choice == rock:
            print(f"It's a draw!")
    if choice == '1':
        print(f'You chose paper!\n{paper}')
        print(f'The computer chose:\n{computer_choice}')
        if computer_choice == scissors:
            print(f'The computer wins!')
            break
        elif computer_choice == rock:
            print(f'You win!')
            break
        elif computer_choice == paper:
            print(f"It's a draw!")
    if choice == '2':
        print(f'You chose scissors!\n{scissors}')
        print(f'The computer chose:\n{computer_choice}')
        if computer_choice == rock:
            print(f'The computer wins!')
            break
        elif computer_choice == paper:
            print(f'You win!')
            break
        elif computer_choice == scissors:
            print(f"It's a draw!")
