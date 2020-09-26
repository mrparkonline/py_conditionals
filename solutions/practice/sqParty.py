# When squirrels get together for a party, they like to have acorns. A squirrel party is successful when the number of acorns is between 40 and 60, inclusively. During the weekends, there is no need for acorns. The party is always fun. 

# input
num_acorns = int(input('Enter the number of acorns: '))
is_weekend = input('Is it the weekend? (Y/N): ')

# processing & output
if is_weekend == 'Y':
    print('The party was a success.')
else:
    if num_acorns >= 40 and num_acorns <= 60:
        print('The party was a success.')
    else:
        print(':(')