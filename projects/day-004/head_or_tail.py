import random

coin_flip = random.randint(0, 100)

if coin_flip <= 50:
    print('tails')
else:
    print('heads')

