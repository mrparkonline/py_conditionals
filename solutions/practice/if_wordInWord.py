# Create a program that checks if the first word exists in the second word

# input
word1 = input('Enter your first word: ')
word2 = input('Enter your second word: ')

# processing & output
if word1 in word2:
    print(word1, 'exists inside', word2)
else:
    print(word1, 'does not exist inside', word2)