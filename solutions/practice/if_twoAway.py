# Create a program such that when given a non-negative number input, output whether or not if the number is 2 away from a multiple of 10.

# input
num = int(input('Enter a positive number: '))

# processing & output
if (num + 2) % 10 == 0:
    print(num, 'is 2 away from a multiple of 10.')
elif (num - 2) % 10 == 0:
    print(num, 'is 2 away from a multiple of 10.')
else:
    print(num, 'is not 2 away from a multiple of 10.')