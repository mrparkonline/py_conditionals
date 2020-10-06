# Program the following minimum credit card payment protocol. The minimum payment is equal to either $10 or 2.1% of the customer's balance, whichever is GREATER; but if this exceeds the balance, then the minimum payment is the balance.

# input
balance = float(input('Enter your balance: '))

# processing & output
percentile = balance * 0.021 # this 2.1% of customer balance

if percentile > 10:
    print('The minimum payment is:', percentile)
else:
    # scenario 1: percentile and 10 are equal
    # scenario 2: percentile is less than 10

    if balance < 10:
        print('The minimum payment is:', balance)
    else:
        print('The minumum payment is: 10')