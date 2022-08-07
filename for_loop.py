num = int(input('Please enter number of tests: '))
score = []
for digits in range(0,num,1):
    marks = int(input('Enter score: '))
    score.append(marks)
for o in score:
    print(o)