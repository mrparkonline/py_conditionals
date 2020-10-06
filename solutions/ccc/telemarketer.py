# Telemarketer Question
# Rules:
# the first of these four digits is an 8 or 9;
# the last digit is an 8 or 9;
# the second and third digits are the same.

# input
num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())

# processing & output
if num1 == 8 or num1 == 9:
    if num4 == 8 or num4 == 9:
        if num2 == num3:
            print('Ignore')
        else:
            print('Answer')
    else:
        print('Answer')
else:
    print('Answer') 

if (num1 == 8 or num1 == 9) and (num4 == 8 or num4 == 9) and (num2 == num3):
    print('Ignore')
else:
    print('Answer')