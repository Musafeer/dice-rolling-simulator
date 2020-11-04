import random

try:
    min_value = 1
    max_value = 6
except:
    print('Input invalid program will revert to defaults.')

again = True

while again:
    print(random.randint(min_value, max_value))

    another_roll = input('Want to roll the dice again?')

    if another_roll == 'yes' or another_roll == 'y':
        again = True
    else:
        break