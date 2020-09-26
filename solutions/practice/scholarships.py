# Average Checker with scholarships

# input
mark1 = int(input('Enter mark 1: '))
mark2 = int(input('Enter mark 2: '))
mark3 = int(input('Enter mark 3: '))
mark4 = int(input('Enter mark 4: '))

# processing and output
average = (mark1 + mark2 + mark3 + mark4) / 4

if average >= 80:
    print('Your average is greater or equal to: 80%.')

    if average >= 90 and average < 95:
        print('Your scholarship is: $2000.')
    elif average >= 95:
        print('Your scholarship is: $4000.')
else:
    print(':(')