# Given four values from the user, determine if they have an average of 80% or Higher. 

# input
mark1 = int(input('Enter mark 1: '))
mark2 = int(input('Enter mark 2: '))
mark3 = int(input('Enter mark 3: '))
mark4 = int(input('Enter mark 4: '))

# processing
average = (mark1 + mark2 + mark3 + mark4) / 4
boolean_result = average >= 80

# output
print('Is our average greater or equal to 80%?', boolean_result)