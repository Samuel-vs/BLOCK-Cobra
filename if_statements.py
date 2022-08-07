myNum = float(input('Enter your number: '))
if (myNum > 0 and myNum < 9):
    print('Your number has a single digit.')
if (myNum > 9 and myNum < 100):
    print('Your number has two digits.')
if (myNum > 99 and myNum < 1000):
    print('Your number has three digits.')