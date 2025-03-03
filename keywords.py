def fun(pname,blood_group,*diseases,email='abcd01@gmail.com'):
    print('pname=',pname)
    print('blood_group=',blood_group)
    for i in diseases:
        print(i,end=',')
    print('')
    print('email=',email)
fun('Krishna','AB+','cancer','fewer','diabetes','cold','corona' ,email='xyz@gmail.com')
print(' ')
fun('Ram','A+','cold','cough')
print(' ')

def fun(s_name,*email,**address):
    print('s_name=',s_name)
    for i in email:
        print(i,end=',')
    print('')
    for i,j in address.items():
        print(i,'=',j)
    print('')
fun('abcd','abc11@gmail.com','xyz@gmailcom',House_no=121,Street='JP Nagar',City='Bangalore',State='Karnataka')
