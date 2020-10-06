# Creating a program that uses the min() without using the min() function. Without knowing the user inputted values of num1 and num2, create a program that outputs the lower value without using the min()

num1 = int(input('Enter a value: '))
num2 = int(input('Enter a value: '))

if num1 <= num2:
    print(num1)
else:
    print(num2)
