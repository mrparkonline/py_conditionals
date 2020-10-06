# RPS game with random numbers

# import
from random import randint

# input
print('Welcome to RPS game!!')
player_choice = int(input('Enter your choice (0 - Rock | 1 - Scissors | 2 - Paper): '))

# processing & output
cpu_choice = randint(0,2)
if cpu_choice == 0:
    print('CPU chose Rock')
elif cpu_choice == 1:
    print('CPU chose Scissors')
else:
    print('CPU chose Paper')

if player_choice == cpu_choice:
    print('Tie Game!')
else:
    if player_choice == 0:
        if cpu_choice == 1:
            print('Player 1 Wins!')
        else:
            print('CPU Wins!')
    elif player_choice == 1:
        if cpu_choice == 2:
            print('Player 1 Wins!')
        else:
            print('CPU Wins!')
    else:
        if cpu_choice == 0:
            print('Player 1 Wins!')
        else:
            print('CPU Wins!')