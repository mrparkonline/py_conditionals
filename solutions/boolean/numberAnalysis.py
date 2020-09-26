# Number Analysis
# Greater than zero
# Less than 100
# Not Even

# input
num = int(input('Enter an integer: '))

# processing
check1 = num > 0
check2 = num < 100
check3 = num % 2 != 0 # num % 2 == 1
valid_number = check1 and check2 and check3

# output
print('Is', num, 'valid?', valid_number)