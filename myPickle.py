import pickle
fruits = ['Apple','Banana','Orange']
num = [1,2,3,4,5,6,7,8,9,]
x = 3.14
y = 1
dataSet = [fruits,num,x,y]
with open('myData.pkl','wb') as f:
    pickle.dump(fruits,f)
    pickle.dump(num,f)
    pickle.dump(x,f)
    pickle.dump(y,f)
with open('myData.pkl','rb') as r:
    a = pickle.load(r)
    b = pickle.load(r)
    c = pickle.load(r)
    d = pickle.load(r)
print(a)
print(b)
print(c)
print(d)