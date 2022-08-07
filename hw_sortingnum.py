# Homework form Tutorial 11
num = int(input('How many tests so you have? '))
grades = []
swp = 0
bucket = 0
lowGrade = 100
highGrade = 0
for i in range(0,num,1):
    grade = int(input('Please enter your grades: '))
    grades.append(grade)
for i in range(0,num,1):
    bucket = bucket + grades[i]
Avg = bucket/num
print('Your Average score: ',Avg)
for i in range(0,num,1):
    if grades[i] < lowGrade:
        lowGrade = grades[i]
print('Your low grade is: ',lowGrade)
for i in range(0,num,1):
    if grades[i] > highGrade:
        highGrade = grades[i]
print('Your high Grade is: ',highGrade)
for i in range(0,num - 1,1):
    for i in range(0,num - 1,1):
        if grades[i] < grades[i + 1]:
            swp = grades[i]
            grades[i] = grades[i + 1]
            grades[i + 1] = swp
print('Your sorted grades are: ')
for i in range(0,num,1):
    print(grades[i])