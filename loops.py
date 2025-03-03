
'''
li=[10,20,30,40,50]
for i in li:
    print(i,end=' ')
print(' ')


li=[10,20,30,40,50]
for i in range(0,len(li),2):
    print(li[i],end=' ')
print(' ')

li=[10,20,30,40,50]
for i in range(len(li)-2,0,-2):
    print(li[i],end=' ')
print(' ')
'''
from forloop import smallest

'''
li=[10,20,13,61,50]
print('elements at even indices are:')
for i in range(0,5,2):
    print(li[i], end=' ')
print(' ')
print('elements at odd indices are:')
for i in range(1,5,3):
    print(li[i], end=' ')
print(' ')


#even & odd elements

for i in li:
    if(i%2==0):
        print(i,'is an even number')
    else:
        print(i,'is an odd number')
print(' ')
'''

'''
#sum of elements
li=[10,20,13,61,50]
sum=0
for i in li:
    sum = sum + i
print('sum of elements is', sum)
'''

'''
li=[10,20,13,61,50]
sum1= 0
sum2=0
for i in li:
    if i%2==0:
        sum1 = sum1 +i 
    else:
        sum2= sum2 + i
print('sum of odd indices is',sum2)
print('sum of even indices is',sum1)

'''

'''
li=[10,20,13,61,50]
sum1= 0
sum2=0
for i in range(0,5,2):
        sum1 = sum1 +li[i]
for i in range(1,5,2):
        sum2= sum2 + li[i]
print('sum of odd indices is',sum2)
print('sum of even indices is',sum1)
'''

'''
st=input('enter a string:')
word_count=1
space_count=0
for char in st:
    if char==' ':
        space_count+= 1
word_count+= 1
print(f'number of words,{word_count}')
print(f'number of space,{space_count}')
'''

'''
words = input("Enter a list of words: ").split()
char = input("Enter a character: ")
vowels = "aeiouAEIOU"

for v in vowels:
    if char == v:
        print(f'{char}, is a vowel.')
        break
else:
    print(f'{char}, is not vowel.')
print(' ')
'''









