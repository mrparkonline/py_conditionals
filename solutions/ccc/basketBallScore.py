# Basketball Scores
# apple vs banana

# input - apples
apple_three = int(input())
apple_two = int(input())
apple_free = int(input())

# input - bananas
banana_three = int(input())
banana_two = int(input())
banana_free = int(input())

apple_total = (apple_three * 3) + (apple_two * 2) + apple_free
banana_total = (banana_three * 3) + (banana_two * 2) + banana_free

if apple_total == banana_total:
    print('T')
elif apple_total > banana_total:
    print('A')
else:
    print('B')