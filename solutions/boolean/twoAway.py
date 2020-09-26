# Given a non-negative number input, output whether or not if the number is exactly 2 away from a multiple of 10. 

# 8 12 18 22

# input
num = int(input())

# processing
two_away = num % 10 == 2 or num % 10 == 8
two_away2 = (num + 2) % 10 == 0 or (num - 2) % 10 == 0

# output
print('Is', num, 'two values away from a multiple of 10?', two_away)
print('Is', num, 'two values away from a multiple of 10?', two_away2)