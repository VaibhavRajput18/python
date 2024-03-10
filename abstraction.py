#abstraction
# from abc import ABC, abstractclassmethod
# class rcpit(ABC):
#     @abstractclassmethod
#     def student_details(self):
#         pass


#     @abstractclassmethod
#     def student_assignment(self):
#         pass

#     @abstractclassmethod
#     def student_marks(self):
#         pass

#q-1
# def find_longest_consecutive_subsequence(arr):
#     arr = sorted(arr)
#     current_sequence = [arr[0]]
#     longest_sequence = [arr[0]]

#     for i in range(1, len(arr)):
#         if arr[i] == arr[i - 1] + 1:
#             current_sequence.append(arr[i])
#         else:
#             current_sequence = [arr[i]]

#         if len(current_sequence) > len(longest_sequence):
#             longest_sequence = current_sequence

#     return longest_sequence
# print("Input: ")
# n = int(input("N: "))
# arr = []
# for i in range(n):
#     element = int(input(f" enter element : "))
#     arr.append(element)
# result = find_longest_consecutive_subsequence(arr)

# print("output :", len(result))
# print("Explanation:")

# print("The consecutive numbers here", result, "These", len(result), "numbers from the longest consecutive subsequence.")
    
#=======================================================================================================

#Q-2
# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price

#     def get_price(self):
#         return self.price

#     def display_details(self):
#         pass
# class Electronics(Product):
#     def __init__(self, name, price, brand, warranty):
#         super().__init__(name, price)
#         self.brand = brand
#         self.warranty = warranty

#     def display_details(self):
#         print(f"Product Name: {self.name}")
#         print(f"Price: ${self.price}")
#         print(f"Brand: {self.brand}")
#         print(f"Warranty: {self.warranty} months")
# class Clothing(Product):
#     def __init__(self, name, price, size, color, material):
#         super().__init__(name, price)
#         self.size = size
#         self.color = color
#         self.material = material

#     def display_details(self):
#         print(f"Product Name: {self.name}")
#         print(f"Price: ${self.price}")
#         print(f"Size: {self.size}")
#         print(f"Color: {self.color}")
#         print(f"Material: {self.material}")
# class Books(Product):
#     def __init__(self, name, price, author, genre):
#         super().__init__(name, price)
#         self.author = author
#         self.genre = genre

#     def display_details(self):
#         print(f"Product Name: {self.name}")
#         print(f"Price: ${self.price}")
#         print(f"Author: {self.author}")
#         print(f"Genre: {self.genre}")
# electronics_product = Electronics("Smartphone", 799.99, "Apple", 12)
# electronics_product.display_details()
# print(f"Price: ${electronics_product.get_price()}")
# clothing_product = Clothing("T-shirt", 19.99, "M", "Red", "Cotton")
# clothing_product.display_details()
# print(f"Price: ${clothing_product.get_price()}")
# book_product = Books("The Great Gatsby", 12.99, "F. Scott Fitzgerald", "Classic Fiction")
# book_product.display_details()
# print(f"Price: ${book_product.get_price()}")

#=====================================================================

#Q=3    
