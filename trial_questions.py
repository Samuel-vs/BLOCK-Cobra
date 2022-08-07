import time
from datetime import date
import os

def interest(ren, com, principal, rate):
    t = 1 / com ; j = 0 ; i = 0 
    while (j < ren):
        i = principal * rate * t
        ir = i / 100
        principal = principal + ir
        j += 1
    principal = round(principal,2)  
    return principal
def taxation(principal, tax):
    z = 0 ; y = 0
    if (tax > 0):
        z = principal * (tax / 100)
        y = principal - z
        y = round(y,2)
    if (tax == 0):
        y = 0
    return y
def difference(pa, pl, y):
    d = 0
    if (y > 0):
        d = pa - pl
        dt = y - pl
        d = round(d, 2) ; dt = round(dt, 2)  
        return d, dt
    if (y == 0):
        d = pa - pl
        d = round(d, 2)
        return d
        
name = str(input('Enter your name: '))
principle = float(input('Principal(p): '))
roi = float(input('Rate(r): '))
time_interwal = int(input('Years(t): '))
compounding = int(input('Compounding(n): '))
tax = float(input('Enter tax %: '))

renewal = compounding * time_interwal

#pauses the execution for 1sec
time.sleep(1)

test = interest(renewal,compounding, principle, roi)
tax_out = taxation(test, tax)
pol = difference(test, principle, tax_out)

window = str(input('Do you want to show on screen(Yes/No): '))

if (window == 'YES' or window == 'yes' or window == 'Yes'):
    print('Revenue before tax: ',test)
    print('Revenue after tax: ',tax_out)
    print('Profit/Loss before and after taxation: ',pol)
elif (window == 'NO' or window == 'no' or window == 'No'):
    print("Uploading to document...")
else:
    print('Invaid Input!!!\nPlease execute the program again.')
    exit()

btest = str(test) ; b_tax_out = str(tax_out) ; bpol = str(pol)

#Prints to .txt file
# writing new content to the file
t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
today = date.today()
d2 = today.strftime("%B %d, %Y")

file_name = str(input('\nEnter file name or dir:(.txt) '))
fp = open(file_name, 'w')

fp.write('REPORT:\n\n\n')

fp.write('Revenue before tax:\t')
fp.write(btest + '\n')

fp.write('Revenue after tax:\t')
fp.write(b_tax_out + '\n')

fp.write('Profit/Loss before and after taxation: \t')
fp.write(bpol + '\n\n\n')

fp.write('Last Updated by: ')
fp.write('\n' + name + '\n' + d2 + '\n' + current_time)

print('Done Writing')
fp.close()

#Launches file_name in Notepad
os.system(file_name)