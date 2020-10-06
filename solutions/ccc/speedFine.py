# Speed Fine Problem

# input
limit = int(input('Enter the speed limit: '))
speed = int(input('Enter the recorded speed of the car: '))

# processing & output
if speed <= limit:
    print('Congratulations, you are within the speed limit!')
else:
    difference = speed - limit
    if difference > 30:
        print('You are speeding and your fine is $500.')
    elif difference > 20:
        print('You are speeding and your fine is $270.')
    else:
        print('You are speeding and your fine is $100.')