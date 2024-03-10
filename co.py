#class and object

# class p:
#     def __init__(self):
#         self.pid=7
#         self.name="vaibhav"

#     def q(self):
#         print("PID =",self.pid)
#         print("Name = ", self.name)
# obj=p()
# obj.q()

#---------------------

#first Q:

# class p:
#     def __init__(self):
#         self.time= "10"

#     def q(self):
#         print("Time=",self.time)

# obj = p()
# obj.q()

#--------------------

#Second Q

# class p:
#     def __init__(self):
#         self.date= "10-10-2023"

#     def q(self):
#         print("Time=",self.date)

# obj = p()
# obj.q()

#---------------------

#Third Q

# class Team():
#     def __init__(self):
#         self.Country_name="India  Australia  India"
#         self.Player_name = "Sachin  Ricky    Saurav"
#         self.Matches=295  ,160  ,230
#         self.Age=30  ,28  ,31
#         self.BattingAvg=45.51  ,41.00  ,40.95
#         self.BallingAvg=53.00  ,67.00  ,30.00

#     def q(self):
#         print("Country_name \t",self.Country_name)
#         print("Player_name \t",self.Player_name)
#         print("Matches \t",self.Matches)
#         print("Age \t",self.Age)
#         print("Batting_Avg \t",self.BattingAvg)
#         print("Balling_Avg \t",self.BallingAvg)

# obj = Team()
# obj.q()

#4 Q
#------------------------

# class ElectricityBill:
#     def _init_(self, name, units_consumed):
#         self.name = name
#         self.units_consumed = units_consumed

#     def calculate_charge(self):
#         if self.units_consumed <= 30:
#             return self.units_consumed * 1.50
#         elif self.units_consumed <= 230:
#             return 30 * 1.50 + (self.units_consumed - 30) * 3.00
#         else:
#             return 30 * 1.50 + 200 * 3.00 + (self.units_consumed - 230) * 4.25

#     def calculate_total_charge(self):
#         charge = self.calculate_charge()
#         if charge > 500.00:
#             return charge + (charge * 0.15)
#         return charge

# # Create instances for at least 5 users
# users = [
#     ElectricityBill("User1", 25),
#     ElectricityBill("User2", 150),
#     ElectricityBill("User3", 300),
#     ElectricityBill("User4", 400),
#     ElectricityBill("User5", 600)
# ]

# # Print charges with names
# for user in users:
#     total_charge = user.calculate_total_charge()
#     print(f"{user.name}: Rs. {total_charge:.2f}")

#5 Q
#-----------------------------

# import math

# class Sphere:
#     def _init_(self, radius):
#         self.radius = radius

#     def calculate_surface_area(self):
#         surface_area = 4 * math.pi * self.radius ** 2
#         return surface_area

#     def calculate_volume(self):
#         volume = (4/3) * math.pi * self.radius ** 3
#         return volume

# # Input radius of the sphere
# radius = float(input("Enter the radius of the sphere: "))

# # Create a Sphere object
# sphere = Sphere(radius)

# # Calculate and print surface area and volume
# surface_area = sphere.calculate_surface_area()
# volume = sphere.calculate_volume()

# print(f"Surface Area of the Sphere: {surface_area:.2f}")
# print(f"Volume of the Sphere: {volume:.2f}")       
        
#6 Q

#------------------------

# class TelephoneBill:
#     def _init_(self, name, address, tel_no, num_calls):
#         self.name = name
#         self.address = address
#         self.tel_no = tel_no
#         self.num_calls = num_calls

#     def calculate_amount(self, charge_per_call=2):
#         amount = self.num_calls * charge_per_call
#         return amount

# # Input customer details
# name = input("Enter customer name: ")
# address = input("Enter customer address: ")
# tel_no = input("Enter customer telephone number: ")
# num_calls = int(input("Enter the number of calls: "))

# # Create a TelephoneBill object
# customer_bill = TelephoneBill(name, address, tel_no, num_calls)

# # Calculate and print the amount to be paid
# amount_to_be_paid = customer_bill.calculate_amount()
# print(f"Amount to be paid: Rs. {amount_to_be_paid:.2f}")

#7 Q
#---------------------------------
        
# def remove_character(s, x):
#     # Initialize an empty string to store the result
#     result = ""
    
#     # Iterate through the characters in the input string 's'
#     for char in s:
#         # If the character is not 'x', add it to the result string
#         if char != x:
#             result += char
    
#     return result

# # Example usage:
# input_string = "Fanny's Occurences"
# character_to_remove = 'x'
# result_string = remove_character(input_string, character_to_remove)
# print(result_string)

