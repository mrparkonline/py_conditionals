'''
8. Movie Going Program

Create a program that determines what ratings of movies you can watch based on your age.
Ages in 18, +infinity can watch all ratings of movies
Ages in 13 to 17 can watch all movies except a rating of R
Ages in 0 to 12 will require parental guidance for PG-13 while watching the rest
All ages can enjoy G rated movies
'''

# input
age = int(input('Enter your age: '))

# processing & output
if age >= 18:
    print('You can watch any movies.')
elif age >= 13:
    print('You can watch any movies that are not rated-R.')
else:
    print('You can only watch PG-13 and PG rated movies with parental guidance.')

print('Humans of all ages can enjoy G rated movies.')