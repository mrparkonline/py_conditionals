# Determine the type of the triangle given its side length, you may assume that it is a valid triangle.

# Types of Triangles
# Equilateral --> equal on all sides
# Isosceles --> equal on only two sides
# Scalene --> no sides are equal

# input
side1 = float(input('Enter side length 1: '))
side2 = float(input('Enter side length 2: '))
side3 = float(input('Enter side length 3: '))

# processing & output
equilateral = side1 == side2 and side2 == side3 # checking if it is an equilateral
scalene = side1 != side2 and side2 != side3 and side1 != side3
isosceles = (not equilateral) and (not scalene)

if equilateral:
    print('The 3 side lengths create a equilateral triangle.')
elif scalene:
    print('The 3 side lengths create a scalene triangle.')
else:
    print('The 3 side lengths create a isosceles triangle.')