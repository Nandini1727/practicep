
li=[10,20,30,40]
li.extend([50,70,80])
print(li)

li=[10,20,30,50]
li.append([10,20])
print(li)

li=[10,20,30,50]
li.pop(2)
print(li)

li=[10,20,30,40,50]
li.insert(70,80)
print(li)

li=[10,20,30,40,50]
li.reverse()
print(li)



li=[]
print('enter a elements:')
for i in range(10):
    element = int(input())
    li.append(element)
print(li)


li=[10,20,30,40,50]
pos=int(input('enter a position:'))
new=int(input('enter a elements:'))
li.insert(pos,new)
print(li)

delete=int(input('enter a elements to be deleted:'))
li.remove(delete)
print(li)

num=int(input('enter the index to be deleted:'))
li.pop(num)
print(li)

li1 = [1,2,3,4,5]
num1= int(input("enter an element: "))
if num1 in li1:
    print(li1.index(num1))
else:
    print(-1)

tu=(1,2,3,4,5)
ele=int(input('enter a element whose index is determined: '))
if ele in tu:
    print('the index of',ele,'is',tu.index(ele))
else:
    print(ele,'is not present in tuple')

se=set()
print('enter a elements:')
for i in range(5):
    element = int(input())
    se.add(element)
print(se)

s={1,2,3,4,5,6}
de= int(input('enter a element to be deleted:'))
if de in s:
    s.remove(de)
    print(s)
else:
    print(s,'is not present in set')


di = {}
name = input("Enter your name: ")
email = input("Enter your email: ")
mobile = int(input("Enter your mobile: "))
city = input("Enter your city: ")
pin = int(input("Enter your pin: "))

di['name'] = name
di['email'] = email
di['mobile'] = mobile
di['city'] = city
di['pin'] = pin
print(' ')
for i, j in di.items():
    print(i,'=',j)
print(' ')

new= input('Enter a new name: ')
di['name'] = new
for i,j in di.items():
    print(i,'=',j)
print(' ')

remove = input('Enter a key to remove:')
if remove in di:
    di.pop(remove)
    print(f'{remove} removed from dictionary.')
else:
    print('Key not found')
print(' ')

check = input('Enter a value to check: ')
if check in di.values():
    print('Value exists in dictionary')
else:
    print('Value not found.')
print(' ')

state = input('Enter a state:')
di['state'] = state
print('State added to dictionary')
print(' ')
for i, j in di.items():
    print(i,'=',j)




