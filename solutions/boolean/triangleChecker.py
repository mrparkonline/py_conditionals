# Given three side lengths of a triangle from the user, determine if it is a valid triangle.

# input
side_a = float(input('Enter side length A: '))
side_b = float(input('Enter side length A: '))
side_c = float(input('Enter side length A: '))

# processing
check1 = side_a + side_b > side_c
check2 = side_c + side_b > side_a
check3 = side_a + side_c > side_b
valid_triangle = check1 and check2 and check3

# output
print('Is it a valid triangle?:', valid_triangle)