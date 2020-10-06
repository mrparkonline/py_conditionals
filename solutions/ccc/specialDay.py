# Special Day
# 02/18 is a special day

# input
month = int(input())
day = int(input())

# processing & output
if month < 2:
    print('Before')
elif month > 2:
    print('After')
else:
    # month is 2 ... yay
    if day == 18:
        print('Special')
    elif day < 18:
        print('Before')
    else:
        print('After')