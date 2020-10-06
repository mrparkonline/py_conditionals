# Triangle Times

# input
angle1 = int(input())
angle2 = int(input())
angle3 = int(input())

# processing & output
total_sum = angle1 + angle2 + angle3

if total_sum != 180:
    print('Error')
else:
    # our total_sum is 180; therefore, we have a valid triangle

    if angle1 == angle2 and angle2 == angle3:
        print('Equilateral')
    elif angle1 != angle2 and angle2 != angle3 and angle1 != angle3:
        print('Scalene')
    else:
        print('Isosceles')
