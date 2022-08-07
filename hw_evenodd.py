# Homework in Tutorial-6
# num = number entered by the user ; r = reminder
num = int(input('Enter a number: '))
r = num % 2
if(r == 0):
    print('Your number is even.')
if(r != 0):
    print('Your number is odd.')