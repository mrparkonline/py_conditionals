'''
Head or Tail Game
'''

# import statements
from random import choice

# input
print('Welcome to Head or Tail Game!')
user_input = input('Take a guess: H for Head, T for Tail: ')

# processing & output
cpu = choice(['H', 'T'])
if cpu == 'H':
    print('The coin landed on Head')
else:
    print('The coin landed on Tail')

if cpu == user_input:
    print('You have guessed correctly.')
else:
    print('You did not guess correctly.')