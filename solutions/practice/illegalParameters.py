# Create a program that adds two integer values of the user's input. The sum cannot be within the range of 10 to 20 excluding 20; therefore, the program should output “illegal parameters” for such operands.

# input
num1 = int(input('Enter a value: '))
num2 = int(input('Enter a value: '))

# processing & output
total = num1 + num2

if total >= 10 and total < 20:
    print('Illegal Parameters!')
else:
    print(total)