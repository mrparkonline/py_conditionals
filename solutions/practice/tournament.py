'''
Problem Description:
Each player in a tournament plays six games.  (There are no ties.)
-- The tournament director places the players in groups based on the results of games as follows: 
if a player wins 5 or 6 games, they are placed in Group 1; 
if a player wins 3 or 4 games, they are placed in Group 2; 
if a player wins 1 or 2 games, they are placed in Group 3; 
if a player does not win any games, they are eliminated from the tournament. 

Write a program to determine which group a player is placed in.

The program takes 6 inputs.Either W for Win or L for Loss.

The program should output the followings scenario
Output 1 for being in group 1
Output 2 for being in group 2
Output 3 for being in group 3
'''

# input
game1 = input('Input W for win, L for Loss: ')
game2 = input('Input W for win, L for Loss: ')
game3 = input('Input W for win, L for Loss: ')
game4 = input('Input W for win, L for Loss: ')
game5 = input('Input W for win, L for Loss: ')
game6 = input('Input W for win, L for Loss: ')

# processing & output
win_counter = 0

if game1 == 'W':
    win_counter += 1
# end of game1

if game2 == 'W':
    win_counter += 1
# end of game2

if game3 == 'W':
    win_counter += 1 # win_counter = win_counter + 1 # it is like incrementing
# end of game3

if game4 == 'W':
    win_counter += 1
# end of game4

if game5 == 'W':
    win_counter += 1
# end of game5

if game6 == 'W':
    win_counter += 1
# end of game6

if win_counter == 5 and win_counter == 6:
    print('Group 1')
elif win_counter >= 3:
    print('Group 2')
elif win_counter >= 1:
    print('Group 3')
else:
    print(-1)