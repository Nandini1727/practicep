# class A:
#     def __init__(self):
#         print('Hi')
# class B(A):
#     def __init__(self):
#         super().__init__()
#         print('Bye')
# b=B()
from traceback import print_tb


#Implement a student Grading System
class Student:
    def __init__(self,name,roll_no,marks1,marks2,marks3):
        self.name=name
        self.roll_no=roll_no
        self.marks1=marks1
        self.marks2=marks2
        self.marks3=marks3
    def calculate_average(self):
        sum=self.marks1+self.marks2+self.marks3
        avg=sum/3
        return avg
    def display_grade(self):
        avg=self.calculate_average()
        if avg>=90:
            print('Grade A')
        elif (avg>=75) and (avg<90):
            print('Grade B')
        elif (avg>=50) and (avg<75):
            print('Grade C')
        else:
            print('Grade D')
s=Student('Nandini',91,61,93,81)
s.display_grade()

#Implement a Banking system
class BankAccount:
    def __init__(self,Holder_name,Account_no,balance=0):
        self.Holder_name=Holder_name
        self.Account_no=Account_no
        self.balance=balance
    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
            print(f'Deposited:{amount},new balance:{self.balance}')
        else:
            print('Invalid amount')
    def withdraw(self,amount):
        if 0<amount<=self.balance:
            self.balance-=amount
            print(f'withdrawn:{amount},new balance:{self.balance}')
        else:
            print('Negative')
    def display_balance(self):
        print(f'Holder_name:{self.Holder_name},Account_no:{self.Account_no},balance:{self.balance}')
a1=BankAccount('Bob',1234,500)
a1.deposit(2000)
a1.withdraw(100)
a1.display_balance()