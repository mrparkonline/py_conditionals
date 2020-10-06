# Let's Make a Deal
# 1 Million or Goat?

# import statement
from random import randint # randint helps us generate random values

# input
print('Welcome to Let us make a deal!')
user_input = int(input('Choose a door, 1/2/3: '))

# processing & output
winning_door = randint(1,3) # randint includes the last value

if winning_door == 1:
    if user_input == 1:
        print('There is a goat in door 2.')
        change = input('Would you like to stay on Door 1 or switch to Door 3? (Stay/Switch): ')
        if change != 'Stay':
            user_input = 3
    
    elif user_input == 2:
        print('There is a goat in door 3.')
        change = input('Would you like to stay on Door 2 or switch to Door 1? (Stay/Switch): ')
        if change != 'Stay':
            user_input = 1
    
    else:
        # user chose door 3
        print('There is a goat in door 2.')
        change = input('Would you like to stay on Door 3 or switch to Door 1? (Stay/Switch): ')
        if change != 'Stay':
            user_input = 1


elif winning_door == 2:
    if user_input == 1:
        print('There is a goat in door 3.')
        change = input('Would you like to stay on Door 1 or switch to Door 2? (Stay/Switch): ')
        if change != 'Stay':
            user_input = 2
    
    elif user_input == 2:
        print('There is a goat in door 1.')
        change = input('Would you like to stay on Door 2 or switch to Door 3? (Stay/Switch): ')
        if change != 'Stay':
            user_input = 3
    
    else:
        # user chose door 3
        print('There is a goat in door 1.')
        change = input('Would you like to stay on Door 3 or switch to Door 2? (Stay/Switch): ')
        if change != 'Stay':
            user_input = 2

else:
    # winning door is 3
    if user_input == 1:
        print('There is a goat in door 2.')
        change = input('Would you like to stay on Door 1 or switch to Door 3? (Stay/Switch): ')
        if change != 'Stay':
            user_input = 3
    
    elif user_input == 2:
        print('There is a goat in door 1.')
        change = input('Would you like to stay on Door 2 or switch to Door 3? (Stay/Switch): ')
        if change != 'Stay':
            user_input = 3
    
    else:
        # user chose door 3
        print('There is a goat in door 1.')
        change = input('Would you like to stay on Door 3 or switch to Door 2? (Stay/Switch): ')
        if change != 'Stay':
            user_input = 2
# out of door switching

if user_input == winning_door:
    print('The million dollars were in door', winning_door)
    print('You guessed correctly, Congratulations.')
else:
    print('You picked a goat, you lose!')
