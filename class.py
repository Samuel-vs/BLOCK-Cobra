class Rectangle:
    def __init__(self,c,l,w):
        self.color = c
        self.length = l
        self.width = w
    def area(self):
        self.area = self.length * self.width
        return self.area
    def peri(self):
        self.peri = (self.length + self.width) * 2
        return self.peri
    def dia(self):
        self.dia = (self.length**2 + self.width**2)**(1/2)
        return self.dia
    def vol(self,h):
        self.height = h
        self.vol = self.length * self.width * self.height
        return self.vol

myRect1 = Rectangle('red',2,1)
myRect2 = Rectangle('blue',4,3)
print(myRect1.color,myRect1.length,myRect1.width)
print(myRect2.color,myRect2.length,myRect2.width)
print('AREA1 = ', myRect1.area())
print('AREA2 = ', myRect2.area())
print('PERIMETER1 = ', myRect1.peri())
print('PERIMETER2 = ', myRect2.peri())
print('DIAGONAL1 = ', myRect1.dia())
print('DIAGONAL2 = ', myRect2.dia())
myVol1 = myRect1.vol(5)
myVol2 = myRect2.vol(5)
print('Volume of Rect1: ',myVol1)
print('Volume of : ',myVol2)