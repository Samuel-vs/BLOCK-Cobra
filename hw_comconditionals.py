num = int(input('Enter yourn number: '))
rem = num % 2
if(num > 0 and rem == 0):
    print('Your number is positive and even')
if(num > 0 and rem != 0):
    print('Your number is positive and odd.')
if(num < 0 and rem != 0):
    print('Your number is negative and odd.')
if(num < 0 and rem == 0):
    print('Your number is negative and even.')
if(num == 0)
    print('Your number is zero.')