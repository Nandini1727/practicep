
name=input("Enter your name:")
age=input("enter your age:")
location=input("enter your location:")
print(name)
print(age)
print(location)



num1=int(input("enter the value of a:"))
num2=int(input("enter the value of b:"))
print(num1+num2)
print(num1*num2)
print(num1/num2)
print(num1//num2)
print(num1**num2)

name=input("enter your name:")
location=input("enter your location:")
print('My name is',name,'I am from',location)



location=input('enter your location:')
print(location[::-1])

str1=input("enter the first string:")
str2=input("enter the second string:")
print(str1[::-1],str2[::-1])

sub1 = int(input("enter the first sub marks:"))
sub2 = int(input("enter the second sub marks: "))
sub3 = int(input("enter the third sub marks:"))
sum =sub1+ sub2+sub3
average= sum/3
percentage=(sum/150)*100
print('The average of three sub is',average, 'the percentage is ',percentage)

x=[100,200,300,400]
print(x[-1])
print(x[1])
print(x[0:])
print(x[:10])
x[0]=x[-1]
print(x)


tuple=(10,20,30,40,50)
print(len(tuple))


r1=range(1,100,2)
r2=range(0,100,2)
li1=list(r1)
li2=list(r2)
print(li1)
print(li2)


r1=range(0,100,2)
r2=range(1,100,2)
s1=reversed(r1)
s2=reversed(r2)
li2=list(s2)
li1=list(s1)
print(li1,li2)


dictionary = {
    'name':'nandini',
    'age': 21,
    'location':'bng'
}
print(dictionary)



dictionary = {
    'eno': 345,
    'ename':'nandini',
    'esal': 30000,

}
dictionary['esal']=50000
print(dictionary['esal'])
dictionary["location"]='bangalore'
print(dictionary)