
def details(name,location):
    return f'{name},{location}'
res = details(name='nandini',location='bng')
print(res)



num1=int(input('enter the first number:'))
num2=int(input('enter the second number:'))
def arith(num1,num2):
    return f'sum of {num1},sum of{num2} is {num1+num2}'
sum=arith(num1,num2)
print(sum)



x=input('enter the string:')
def str_rev(x):
    print(x[::-1])
str_rev(x)



x=input('enter the string:')
def str_rev(x):
    return x
a=str_rev(x[::-1])
print(a)





num1=int(input('Enter the first number:'))
num2=int(input('Enter the second number:'))
def add(num1,num2):
    return f'the sum of {num1},{num2} is {num1+num2}'
addition=add(num1,num2)
print(addition)

def mul(num1,num2):
    return f'the product of {num1},{num2} is {num1*num2}'
multi=mul(num1,num2)
print(multi)

def div(num1,num2):
    return f'the divison of {num1},{num2} is {num1/num2}'
div=div(num1,num2)
print(div)

def sub(num1,num2):
    return f'the difference of {num1},{num2} is {num1-num2}'
subtraction=sub(num1,num2)
print(subtraction)

def rem(num1,num2):
    return f'the reminder of {num1},{num2} is {num1*num2}'
reminder=rem(num1,num2)
print(reminder)





num1=int(input('Enter the first number:'))
num2=int(input('Enter the second number:'))
def largest(num1,num2):
    if num1>num2:
        return num1
    else:
        return num2
fun=largest(num1,num2)
print('the bigger number is',fun)





num=int(input('Enter the number:'))
def evenodd(num):
     if num % 2 == 0:
         print("EVEN")
     else:
         print("ODD")

evenodd(num)




num1=int(input('Enter the first number:'))
num2=int(input('Enter the second number:'))
num3=int(input('Enter the third number:'))
def fun_largest(num1,num2,num3):
    if (num1 >= num2 and num1 >=num3):
        return num1
    elif (num2 >= num1 and num2>=num3):
        return num2
    else:
        return num3
largest=fun_largest(num1,num2, num3)
print("the bigger number is",largest)






