# Constructor overloading with variable number of arguments
# class test:
#     def __init__(self,*n):
#         print("Constructor with variable number of arguments")

# t=test()
# t=test(10)
# t=test(10,22)
# t=test(10,22,33)

# constructor overloading

# class test:
#     def __init__(self):
#         print("no arguments method:")

#     def __init_(self,a):
#         print("one argument method:",a)

#     def __init__(self,a,b):
#         print("Two argument method :",(a*b))
# t=test()
# t=test(10)
# t=test(10,22)
    
# class MyPython:
#     def __init__(self):
#         print("Constructor is called")

#     def func(self):
#         print("func code execution")

# m1=MyPython()
# m1.func()

# class student:
#     def __init__(self,name,age,percentage):
#         self.name=name
#         self.age=age
#         self.percentage=percentage

#     def showinfo(self):
#         print("name:",self.name)
#         print("age:",self.age)
#         print("percentage :",self.percentage)

# name=input("Enter name \t:")
# age=int(input("Enter age \t:"))
# percentage =float(input("Enter percentage"))
# s=student(name,age,percentage)
# s1=student(name,age,percentage)
# s.showinfo()
# s1.showinfo()


# Q-1

# class BankAccount:
#     def _init_(self):
#         self.name = ""
#         self.account_number = 0
#         self.account_type = ""
#         self.balance = 0.0

#     def input_data(self):
#         self.name = input("Enter the name of the depositor: ")
#         self.account_number = int(input("Enter the account number: "))
#         self.account_type = input("Enter the type of account: ")
#         self.balance = float(input("Enter the initial balance: "))

#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount
#             print(f"Deposited {amount} successfully. New balance: {self.balance}")
#         else:
#             print("Invalid deposit amount. Please enter a positive amount.")

#     def withdraw(self, amount):
#         if amount > 0:
#             if amount <= self.balance:
#                 self.balance -= amount
#                 print(f"Withdrew {amount} successfully. New balance: {self.balance}")
#             else:
#                 print("Insufficient balance. Cannot withdraw.")
#         else:
#             print("Invalid withdrawal amount. Please enter a positive amount.")

#     def display(self):
#         print(f"Name: {self.name}")
#         print(f"Account Number: {self.account_number}")
#         print(f"Account Type: {self.account_type}")
#         print(f"Balance: {self.balance}")

# # Menu-driven program
# account = BankAccount()
# while True:
#     print("\nMenu:")
#     print("1. Input Data")
#     print("2. Deposit")

# class student:


#     def _init_(self):
#         self.name = ""
#         self.roll_number = 0
#         self.address = ""
#         self.percentage = 0.0

#     def input_data(self):
#         self.name = input("Enter the name of the Student: ")
#         self.roll_number = int(input("Enter the roll number: "))
#         self.address = input("Enter the address: ")
#         self.percentage = float(input("Percentage: "))

#     def rank(self):
#         if self.percentage>= 70 :
#             print("You got distinction")
#         elif self.percentage <70 and self.percentage>= 60:
#             print("First class")
#         elif self.percentage < 60 and self.percentage>=40:
#             print("Second class") 
#         else :
#             print("you are fail")   
    
#     def display(self):
#         print(f"Name: {self.name}")
#         print(f"Roll Number: {self.roll_number}")
#         print(f"address: {self.address}")
#         print(f"percentage: {self.percentage}")

# s=student()






    








































