'''
import calendar
year=int(input('enter a year:'))
month=int(input('enter a month:'))
display=calendar.month(year,month)
print(display)
'''

'''
import datetime
print(datetime.datetime.now())
'''

'''
import math
print(math.factorial(5))
'''

'''
num=int(input('enter a number:'))
fact = num
for i in range(1, num):
    fact *= i
print('factorial of', num ,'is',fact)
'''
'''
base=float(input('enter a base of triangle:'))
height=float(input('enter a height of triangle:'))
area=0.5*base*height
print('Area of triangle is',area)
'''

'''
miles=float(input('enter the mile:'))
km=miles*1.6
print('miles',miles,'km',km)
'''

'''
a=int(input('enter the first number:'))
b=int(input('enter the second number:'))
print(f'original number:a= {a},b = {b}')
temp=a
a=b
b=temp
print(f'a={a},b={b}')
'''

'''
celsius=float(input('enter a celsius:'))
f=(celsius*9/5)+32
print('fahrenheit of',celsius,'is',f)
'''

'''
num=int(input('enter the number:'))
if num>0:
    print('number is positive')
elif num<0:
    print('number is negative')
else:
    print('zero')
'''

'''
num=int(input('enter a multiplication table:'))
for i in range(1,11):
    print(f'{num}*{i}={num*i}')
'''
num1=int(input('enter the first number:'))
num2=int(input('enter the  second number:'))
total=0
for i in range(num1,num2+1):
    total+=i
print(f'sum of numbers from {num1},{num2} is {total}')