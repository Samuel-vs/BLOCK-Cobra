class students:
    def __init__(self,first,last):
        self.first = first
        self.last = last
    def gInput(self,ng):
        self.ng = ng
        self.grades = []
        for i in range(0,ng,1):
            grd = float(input('Enter grades: '))
            self.grades.append(grd)
        return self.grades
    def PrintGrades(self):
        print(self.first,self.last,"'s Grade: ")
        for i in range(0,self.ng,1):
            print(self.grades[i])
        print('')
    def AvGrades(self):
        bucket = 0
        for i in range(0,self.ng,1):
            bucket = bucket + self.grades[i]
        avg = bucket / self.ng
        return avg
    def highlow(self):
        high_grade = 0
        low_grade = 100
        for i in range(0,self.ng,1):
            if (self.grades[i] > high_grade):
                high_grade = self.grades[i]
            if (self.grades[i] < low_grade):
                low_grade = self.grades[i]
        return low_grade, high_grade
           
student1 = students('Joe','Evans')
student2 = students('Samuel','VS')
num = int(input('Enter number of tests: '))
print(student1.first,student1.last)
test1 = student1.gInput(num)
print('\n',student2.first,student2.last)
test2 = student2.gInput(num)
print('\nStudent Report for: ',student1.first,student1.last)
student1.PrintGrades()
print('Average score: ',student1.AvGrades())
print('Lowest and Highest = = ',student2.highlow())
print('\nStudent Report for: ',student2.first,student2.last)
student2.PrintGrades()
print('Average score: ',student2.AvGrades())
print('Lowest and Highest = ',student2.highlow())