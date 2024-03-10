#---------------------------------------------
#single Inheritance

# class A:
#     def showA(self):
#         print("Class A")
# class B(A):
#     def showB(self):
#         print("Class B")

# obj=A()
# obj.showA()
# obj1=B()
# obj1.showA()
# obj1.showB()

#---------------------------------------------
#Multiple Inheritance
# class A:
#     def showA(self):
#         print("Class A")
# class B(A):
#     def showB(self):
#         print("Class B")
    
# class C(B):
#     def showC(self):
#         print("Class C")

# obj=A()
# obj.showA()
# obj1=B()
# obj1.showA()
# obj1.showB()
# obj2=C()
# obj2.showA()
# obj2.showB()
# obj2.showC()

#------------------------------------
#Hierarchical Inheritance
# class A:
#     def showA(self):
#         print("Class A")
# class B(A):
#     def showB(self):
#         print("Class B")
    
# class C(A):
#     def showC(self):
#         print("Class C")

# class D(A):
#     def showD(self):
#         print("Class D")

# obj3=D()
# obj3.showA()
# obj3.showD()

#-------------------------------------------
#Hybrid Inheritance

# class A:
#     def showA(self):
#         print("Class A")
# class B(A):
#     def showB(self):
#         print("Class B")
    
# class C(A):
#     def showC(self):
#         print("Class C")

# class D(B,C):
#     def showD(self):
#         print("Class D")

# obj=D()
# obj.showA()
# obj.showB()
# obj.showC()
# obj.showD()

#----- -------------------------------------
#super Function

# class parent1:
#     def show1(self):
#         print("parent1 Method")
# class parent2(parent1):
#     def show2(self):
#         super().show1()
#         print("parent2 Method")
# c=parent2()
# c.show2()

#-------------------------------------
#passing members of one class to another class
# class employee:
#     def __init__(self,no,name,sal):
#         self.eno=no
#         self.ename=name
#         self.esal=sal
#     def showdetails(self):
#         print("employee no : ",self.eno)
#         print("employee name : ",self.ename)
#         print("employee salary : ",self.esal)

# class test:
#     def updates(employee):
#         employee.esal=employee.esal+8000
#         employee.ename="vaibhav"
#         employee.showdetails()
# e=employee(101,"Yatish",20000)
# e.showdetails()
# test.updates(e)       

#------------------------------------------
#write a py program to create a class called employee with methodscalld work()and getsalary() (in getsalary()assign salary in HRmanager that overrides the work()methods and adds a new methods called addemployee()).


#==================================================================
# class BankAccount:
#     def __init__(self):
#         self.balance = 0

#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount
#             print("Amount deposited successfully.")
#         else:
#             print("Invalid amount.")

#     def withdraw(self, amount):
#         if amount > 0:
#             if self.balance - amount >= 1000:
#                 self.balance -= amount
#                 print("Amount withdrawn successfully.")
#             else:
#                 print("Insufficient balance.")
#         else:
#             print("Invalid amount.")

# class SavingsAccount(BankAccount):
#     def withdraw(self, amount):
#         if amount > 0:
#             if self.balance - amount >= 1000:
#                 self.balance -= amount
#                 print("Amount withdrawn successfully.")
#             else:
#                 print("Withdrawal not allowed")
#         else:
#             print("Invalid amount.")

# # Menu driven program
# account = SavingsAccount()

# while True:
#     print("------------------------------------------------------------")
#     print("1. Deposit")
#     print("2. Withdraw")
#     print("3. Check Balance")
#     print("4. Exit")

#     choice = int(input("Enter your choice: "))

#     if choice == 1:
#         amount = float(input("Enter the amount to deposit: "))
#         account.deposit(amount)
#     elif choice == 2:
#         amount = float(input("Enter the amount to withdraw: "))
#         account.withdraw(amount)
#     elif choice == 3:
#         print("Account balance:", account.balance)
#     elif choice == 4:
#         print("Exiting...")
#         break
#     else:
#         print("Invalid choice. Please try again.")


#=============================================================



