# RPS Game :D

from random import choice

player1 = input('Choose: Rock, Paper, or Scissors: ')
cpu = choice(['Rock', 'Paper','Scissors'])

if player1 == cpu:
    # Tied Game
    print('Tied Game!')
else:
    # A non-tied game; therefore, there is a winner
    if player1 == 'Rock':
        if cpu == 'Paper':
            print('CPU wins!')
        else:
            print('Player 1 wins!')
    elif player1 == 'Paper':
        if cpu == 'Scissors':
            print('CPU wins!')
        else:
            print('Player 1 wins!')
    else:
        # it we are here ... player1 chose Scissors
        if cpu == 'Rock':
            print('CPU wins!')
        else:
            print('Player 1 wins!')