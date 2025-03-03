char=input('Enter a character:').lower()
if char == 'a' or char== 'e' or char=='i' or char=='o' or char=='u':
    print(char,'is a vowel')
else:
    print(char,'is a consonent')



year=int(input('Enter a year:'))

if (year%400==0) or (year%4==0 and year%100!=0):
    print('is a leap year')
else:
    print('not a leap year')



st=input('Enter a string:').lower()
if st==st[::-1]:                        #if st[::-1].lower()== st.lower():
    print('is a palindrome')
else:
    print('is not a palindrome')




a=int(input('Enter the length:'))
b=int(input('enter the breadth:'))
if a==b:
    print('is a square')
else:
    print('is a rectangle')



name=input('enter your name:')
gender=input('enter your gender:').lower()
if gender=='male':
    height=int(input('enter your height:'))
    if height>=188:
        print(name,'is eligible')
    else:
        print(name,'not eligible')
elif gender=='female':
    height=int(input('enter your height:'))
    if height>=175:
        print(name,'is eligible')
    else:
        print(name,'not eligible')
else:
    print(name,'not eligible')



x=2
while x<=100:
    print(x,end=' ')
    x=x+2
print('end')
x=1
while x<=100:
    print(x,end=' ')
    x=x+2
print('end')




#2,4 16,256,65526
x=2
while x<=65526:
    print(x,end=' ')
    x=x*2



x=3125
while x>=5:
    print(x,end=' ')
    x=x//5



x=1
while x<=10:
    print (f'1*{x}={1*x}')
    x=x+1



x=1
while x<=10:
    print(f'{2} * {x}= {2*x}, {3}* {x}= {3*x} , {4} * {x}= {4*x} , {5} * {x}= {5*x} , {6} * {x}= {6*x} , {7} * {x}= {7*x}, {8} * {x}= {8* x}, {9} * {x}= {9*x}, {10} * {x}= {10 * x}')
    x=x+1


x=0
letters=('A','C','E','G','I')
while x<=4:
        print(letters[x],end=' ')
        x=x+1












