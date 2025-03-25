'''
#displaying even numbers from 0 to 100
li=[]
for i in range(0,101,2):
    li.append(i)
print(li)
'''


'''
li=[1,5,6,8,3]
y=[]
for i in range(len(li)):
    if i%2==1:
        y.append(li[i]**2)
print(y)

z=[]
for i in range(len(li)):
    if i%2==0:
        z.append(li[i]*5)
print(z)

a=[]
for i in range(5):
    a.append(li[i]*2)
print(a)
'''

'''
li=[11,3,6,10,13]
y=[]
for i in range(5):
    if li[i]%3==0:
        y.append(li[i]**2)
print(y)

z=[]
for i in range(5):
    z.append(li[i]+5)
print(z)

a=[]
for i in range(5):
    if li[i]%3!=0:
      a.append(li[i]**2)
print(a)

y=[li[i]**2 for i in range(5) if li[i]%3==0]
print(y)

z=[li[i]+5 for i in range(5)]
print(z)

a=[li[i]**2 for i in range(5) if li[i]%3!=0]
print(a)
'''

'''
x=['hi','python','we','write','python','we','say','hi','python']
di={}
for i in x:
    if i in di.keys():
        a=di[i]
        di[i]=a+1
    else:
        di[i]=1
print(di)
'''

'''
x=[('a',10),('b',20),('c',30),('d',40)]
for i in x:
    print(i[1] ,end=' ')
'''

'''
x = ['a', 'b', 'c', 'd']
y = [10, 20, 30, 40]
z={}
for i in range(len(x)):
    z[x[i]]=y[i]
print(z)
'''

'''
x = ['a', 'b', 'c', 'd']
y = [10, 20, 30, 40]
z = [(x[i], y[i])
     for i in range(len(x))]
print(z)
'''
'''
#globals()
#1
x=10
def fun():
    x=20
    print(x)
    print(globals() ['x'])
fun()
print(' ')

#2
x=10
y=20
def f1():
    y=30
    print(x)
    print(y)
    print(globals()['x'])
    print(globals()['y'])
f1()
print(' ')
'''
#modules