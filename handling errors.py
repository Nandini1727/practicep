# from logging import exception
#
# li=[10,20,30,40,50]
# x=10
# try:
#     print(x/2)
#     print(li[3])
#     print(10/0)
# except Exception as e:
#     print(e)
# except:
#     print('An error occurred')
# print('Hello')
from dataclasses import replace

# x=int(input('Please enter a number:'))
# y=[10,20,30]
# try:
#     print(x)
#     print(y[0])
#     print(y[1])
#     print(y[2])
#     print(y[3])
# except Exception as e:
#     print(e)


# x=[10,20,30,40,50]
# y=10
# try:
#     print(x[0])
#     print(y/0)
# except IndexError:
#     print('Trying to access a non-existent index')
# except ZeroDivisionError:
#     print('trying to divide by 0')
# except:
#     print('An error occurred')


# f=open('sample.txt','w')
# f.write('This is file operation')
# f.close()
# f=open('sample.txt','a')
# f.write('\nhello')
# f.write('\nGood morning')
# f.close()
# f=open('sample.txt','r')
# res=f.read()
# print(res)
# res1=f.readline()
# print(res1)
# res2=f.readlines()
# print(res2)
# f.close()


# f=open('info.txt','w')
# f.write('Hello')
# f.write('\nEveryone')
# f.close()
# f=open('info.txt','a')
# f.write('\nGood morning')
# f.write('\nwelcome to python')
# f.close()
# f=open('info.txt','r')
# res=f.read()
# res=res.replace('Hello','We have made a changes')
# print(res)
# f.close()
# f=open('info.txt','w')
# f.write(res)
# f.close()


f=open('example.txt','w')
f.write('This is file operation')
f.write('\n we are creating a file')
f.close()
f=open('example.txt','r')
res=f.read()
res=res.replace('This is file operation','This is file I/O operation')
print(res)
f.close()
f=open('example.txt','w')
f.write(res)
f.close()
