# class rcpit:
#     def __init__ (self):
#         print("rcpit default constructor is called...")
#     class cse:
#         def __init__ (self):
#             print("cse default constructor is called...")

#         def techfest(self):
#             print("rcpit - cse branch techfest execution")
        
# r=rcpit()
# r1=r.cse()
# r1.techfest()
# obj=rcpit().cse()
# obj.techfest()
#rcpit().cse().techfest()


# class Student:
#     def __init__(self, student_id, name, password):
#         self.student_id = student_id
#         self.name = name
#         self.password = password
#         self.has_voted = False

#     def update_details(self, name, password):
#         self.name = name
#         self.password = password

#     def vote(self):
#         if not self.has_voted:
#             self.has_voted = True
#             return True
#         else:
#             return False

# class Admin:
#     def __init__(self, admin_username, admin_password):
#         self.admin_username = admin_username
#         self.admin_password = admin_password

# class Election:
#     def __init__(self):
#         self.nominees = {}
#         self.votes = {}

#     def add_nominee(self, nominee_name):
#         self.nominees[nominee_name] = 0

#     def update_nominee(self, nominee_name, new_name):
#         if nominee_name in self.nominees:
#             self.nominees[new_name] = self.nominees.pop(nominee_name)

#     def remove_nominee(self, nominee_name):
#         if nominee_name in self.nominees:
#             del self.nominees[nominee_name]

#     def view_voting_details(self):
#         for nominee, votes in self.nominees.items():
#             print(f"{nominee}: {votes} votes")

# def student_registration():
#     # Implement student registration logic here
#     pass

# def student_login(students):
#     # Implement student login logic here
#     pass

# def admin_login(admin):
#     # Implement admin login logic here
#     pass

# def main():
#     students = []  # List to store student objects
#     admin = Admin("admin", "adminpass")  # Create an admin object
#     election = Election()  # Create an Election object

#     while True:
#         print("\nMenu:")
#         print("1. Student Registration")
#         print("2. Student Login")
#         print("3. Admin Login")
#         print("4. Exit")

#         choice = input("Enter your choice: ")

#         if choice == "1":
#             student_registration()
#         elif choice == "2":
#             student = student_login(students)
#             if student:
#                 # Implement student actions (update details, vote, logout) here
#                 pass
#         elif choice == "3":
#             admin = admin_login(admin)
#             if admin:
#                 # Implement admin actions (add/update/remove nominees, view voting details) here
#                 pass
#         elif choice == "4":
#             break
#         else:
#             print("Invalid choice. Please try again.")

# if __name__ == "__main__":
#     main()



# class Student:
#     def _init_(self, username, password):
#         self.username = username
#         self.password = password
#         self.voted = False

#     def update_details(self, new_password):
#         self.password = new_password

#     def vote(self, nominee):
#         if not self.voted:
#             self.voted = True
#             return nominee
#         else:
#             return None

# class PresidentNominee:
#     def _init_(self, name):
#         self.name = name
#         self.votes = 0

#     def update_name(self, new_name):
#         self.name = new_name

#     def add_vote(self):
#         self.votes += 1

# # Initialize the program
# students = []
# nominees = []
# admin_password = "adminpass"

# def student_registration():
#     username = input("Enter your username: ")
#     password = input("Enter your password: ")
#     students.append(Student(username, password))
#     print("Registration successful!")

# def student_login():
#     username = input("Enter your username: ")
#     password = input("Enter your password: ")
#     for student in students:
#         if student.username == username and student.password == password:
#             return student
#     return None

# def admin_login():
#     password = input("Enter admin password: ")
#     if password == admin_password:
#         return True
#     return False

# def add_president_nominee():
#     if admin_login():
#         name = input("Enter the name of the nominee: ")
#         nominees.append(PresidentNominee(name))
#         print("Nominee added successfully!")

# def update_president_nominee():
#     if admin_login():
#         print("Current Nominees:")
#         for i, nominee in enumerate(nominees):
#             print(f"{i + 1}. {nominee.name}")
#         nominee_index = int(input("Enter the index of the nominee to update: ")) - 1
#         if 0 <= nominee_index < len(nominees):
#             new_name = input("Enter the new name: ")
#             nominees[nominee_index].update_name(new_name)
#             print("Nominee updated successfully!")

# def remove_president_nominee():
#     if admin_login():
#         print("Current Nominees:")
#         for i, nominee in enumerate(nominees):
#             print(f"{i + 1}. {nominee.name}")
#         nominee_index = int(input("Enter the index of the nominee to remove: ")) - 1
#         if 0 <= nominee_index < len(nominees):
#             removed_nominee = nominees.pop(nominee_index)
#             print(f"{removed_nominee.name} has been removed!")

# def view_voting_details():
#     if admin_login():
#         print("Voting Details:")
#         for nominee in nominees:
#             print(f"{nominee.name}: {nominee.votes} votes")

# while True:
#     print("\nWelcome to College President Voting System")
#     print("1. Student Registration")
#     print("2. Student Login")
#     print("3. Admin Login")
#     print("4. Exit")

#     choice = int(input("Enter your choice: "))

#     if choice == 1:
#         student_registration()
#     elif choice == 2:
#         student = student_login()
#         if student:
#             while True:
#                 print("\nStudent Menu")
#                 print("1. Update Details")
#                 print("2. Vote")
#                 print("3. Logout")

#                 student_choice = int(input("Enter your choice: "))

#                 if student_choice == 1:
#                     new_password = input("Enter new password: ")
#                     student.update_details(new_password)
#                     print("Details updated successfully!")
#                 elif student_choice == 2:
#                     if not student.voted:
#                         print("Available Nominees:")
#                         for i, nominee in enumerate(nominees):
#                             print(f"{i + 1}. {nominee.name}")
#                         nominee_index = int(input("Enter the index of the nominee you want to vote for: ")) - 1
#                         if 0 <= nominee_index < len(nominees):
#                             voted_nominee = student.vote(nominees[nominee_index])
#                             if voted_nominee:
#                                 voted_nominee.add_vote()
#                                 print(f"You have voted for {voted_nominee.name}!")
#                             else:
#                                 print("You have already voted.")
#                         else:
#                             print("Invalid nominee index.")
#                     else:
#                         print("You have already voted.")
#                 elif student_choice == 3:
#                     break
#                 else:
#                     print("Invalid choice.")
#     elif choice == 3:
#         if admin_login():
#             while True:
#                 print("\nAdmin Menu")
#                 print("1. Add President Nominee")
#                 print("2. Update President Nominee")
#                 print("3. Remove President Nominee")
#                 print("4. View Voting Details")
#                 print("5. Logout")

#                 admin_choice = int(input("Enter your choice: "))

#                 if admin_choice == 1:
#                     add_president_nominee()
#                 elif admin_choice == 2:
#                     update_president_nominee()
#                 elif admin_choice == 3:
#                     remove_president_nominee()
#                 elif admin_choice == 4:
#                     view_voting_details()
#                 elif admin_choice == 5:
#                     break
#                 else:
#                     print("Invalid choice.")
#     elif choice == 4:
#         print("Thank you for using College President Voting System!")
#         break
#     else:
#         print("Invalid choice.")

# stock
# def calculate_stock_span(prices):
#     n = len(prices)
#     stack = []
#     spans = [0] * n

#     for i in range(n):
#         # Pop elements from the stack while they are smaller than the current price
#         while stack and prices[i] >= prices[stack[-1]]:
#             stack.pop()

#         if not stack:
#             spans[i] = i + 1  # If the stack is empty, the span is the current day
#         else:
#             spans[i] = i - stack[-1]  # Span is the difference between current day and the last greater element

#         stack.append(i)

#     result = []
#     for span in spans:
#         result.append(span * span * span if span > 1 else span)

#     return result

# # Example usage:
# prices = [100, 80, 60, 70, 60, 75, 85]
# output = calculate_stock_span(prices)
# print(output)
