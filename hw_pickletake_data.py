import pickle
names = []
grades = []
num = int(input('Enter number of students: '))
for j in range(0,num,1):
    name = input("Enter student's name: ")
    names.append(name)
    prompt = 'Please enter '+name+"'s grade: "
    grade = float(input(prompt))
    grades.append(grade)
with open('studentdata.pkl','wb') as dataF:
    pickle.dump(num,dataF)
    pickle.dump(names,dataF)
    pickle.dump(grades,dataF)
     