import pickle
with open('studentdata.pkl','rb') as readF:
    num = pickle.load(readF)
    names = pickle.load(readF)
    grades = pickle.load(readF)
while (1 == 1):
    name = input('WHich student do you want to check? ')
    for i in range(0,num,1):
        if (names[i] == name):
            print(name,"'s grade is ",grades[i],'.')
