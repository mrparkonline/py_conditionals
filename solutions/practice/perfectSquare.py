# Create a program to check if an integer is a perfect square.

# 4, 9, 25 any ideas? Use Square Root

# input
num = int(input('Enter a value: '))

# processing & output
if (num ** 0.5) % 1 != 0:
    print(num, 'is not a perfect square.')
else:
    print(num, 'is a perfect square.')