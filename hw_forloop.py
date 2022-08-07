# Homework form Tutorial 9
# Copied last loop from Tutorial 10
# Included max and min in Tutorial 11
num = int(input('How many tests so you have? '))
grades = []
bucket = 0
lowGrade = 100
highGrade = 0
for i in range(0,num,1):
    grade = int(input('Please enter your grades: '))
    grades.append(grade)
print('Your grades are: ')
for i in range(0,num,1):
    print(grades[i])
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
