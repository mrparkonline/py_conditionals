# Write a program to check if values a, b, and c are pythagorean triples such that 
# a^2 + b^2 = c^2

# input
side_a = float(input('Enter a side A: '))
side_b = float(input('Enter a side B: '))
side_c = float(input('Enter a side C: '))

# processing
if (side_a ** 2) + (side_b ** 2) == side_c ** 2:
    print(side_a, side_b, side_c, 'creates a pythagorean triple.')
else:
    print(side_a, side_b, side_c, 'does not create a pythagorean triple.')