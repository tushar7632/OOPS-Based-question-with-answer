# 1. Write a Python program to create a class representing a Circle.
# Include methods to calculate its area and perimeter.

# # # Import the math module to access mathematical functions like pi
# import math

# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#     def calculate_circle_area(self):
#         return math.pi * self.radius**2
    
#     def calculate_circle_perimeter(self):
#         return 2 * math.pi * self.radius


# radius = float(input("Input the radius of the circle: "))

# circle = Circle(radius)

# area = circle.calculate_circle_area()
# perimeter = circle.calculate_circle_perimeter()


# print("Area of the circle:", area)
# print("Perimeter of the circle:", perimeter)

# # 2. Write a Python program to create a person class.
# # Include attributes like name, country and date of birth.
# # Implement a method to determine the person's age.

# # Import the date class from the datetime module to work with dates
# from datetime import date


# class Person:

#     def __init__(self, name, country, date_of_birth):
#         self.name = name
#         self.country = country
#         self.date_of_birth = date_of_birth
    
#     def calculate_age(self):
#         today = date.today()
#         age = today.year - self.date_of_birth.year
#         if today < date(today.year, self.date_of_birth.month, self.date_of_birth.day):
#             age -= 1
#         return age

# person1 = Person("Ferdi Odilia", "France", date(1962, 7, 12))
# person2 = Person("Shweta Maddox", "Canada", date(1982, 10, 20))
# person3 = Person("Elizaveta Tilman", "USA", date(2000, 1, 1))

# print("Person 1:")
# print("Name:", person1.name)
# print("Country:", person1.country)
# print("Date of Birth:", person1.date_of_birth)
# print("Age:", person1.calculate_age())

# print("\nPerson 2:")
# print("Name:", person2.name)
# print("Country:", person2.country)
# print("Date of Birth:", person2.date_of_birth)
# print("Age:", person2.calculate_age())

# print("\nPerson 3:")
# print("Name:", person3.name)
# print("Country:", person3.country)
# print("Date of Birth:", person3.date_of_birth)
# print("Age:", person3.calculate_age())

# # Define a class called Calculator to perform basic arithmetic operations
# class Calculator:
#     def add(self, x, y):
#         return x + y
#     def subtract(self, x, y):
#         return x - y
#     def multiply(self, x, y):
#         return x * y

#     def divide(self, x, y):
#         if y != 0:
#             return x / y
#         else:
#             return ("Cannot divide by zero.")

# calculator = Calculator()

# result = calculator.add(7, 5)
# print("7 + 5 =", result)

# result = calculator.subtract(34, 21)
# print("34 - 21 =", result)

# result = calculator.multiply(54, 2)
# print("54 * 2 =", result)

# result = calculator.divide(144, 2)
# print("144 / 2 =", result)

# result = calculator.divide(45, 0)
# print("45 / 0 =", result)

# 4. Write a Python program to create a class that represents a shape.
# Include methods to calculate its area and perimeter.
# Implement subclasses for different shapes like circle, triangle, 
# and square.


# import math

# class Shape:
#     def calculate_area(self):
#         pass


#     def calculate_perimeter(self):
#         pass

# class Circle(Shape):

#     def __init__(self, radius):
#         self.radius = radius

#     def calculate_area(self):
#         return math.pi * self.radius**2

#     def calculate_perimeter(self):
#         return 2 * math.pi * self.radius


# class Rectangle(Shape):

#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def calculate_area(self):
#         return self.length * self.width

#     def calculate_perimeter(self):
#         return 2 * (self.length + self.width)

# class Triangle(Shape):

#     def __init__(self, base, height, side1, side2, side3):
#         self.base = base
#         self.height = height
#         self.side1 = side1
#         self.side2 = side2
#         self.side3 = side3


#     def calculate_area(self):
#         return 0.5 * self.base * self.height


#     def calculate_perimeter(self):
#         return self.side1 + self.side2 + self.side3

# r = 7
# circle = Circle(r)
# circle_area = circle.calculate_area()
# circle_perimeter = circle.calculate_perimeter()

# print("Radius of the circle:", r)
# print("Circle Area:", circle_area)
# print("Circle Perimeter:", circle_perimeter)

# l = 5
# w = 7
# rectangle = Rectangle(l, w)
# rectangle_area = rectangle.calculate_area()
# rectangle_perimeter = rectangle.calculate_perimeter()

# print("\nRectangle: Length =", l, " Width =", w)
# print("Rectangle Area:", rectangle_area)
# print("Rectangle Perimeter:", rectangle_perimeter)

# base = 5
# height = 4
# s1 = 4
# s2 = 3
# s3 = 5

# print("\nTriangle: Base =", base, " Height =", height, " side1 =", s1, " side2 =", s2, " side3 =", s3)
# triangle = Triangle(base, height, s1, s2, s3)
# triangle_area = triangle.calculate_area()
# triangle_perimeter = triangle.calculate_perimeter()
# print("Triangle Area:", triangle_area)
# print("Triangle Perimeter:", triangle_perimeter)

# 5. Write a Python program to create a class representing a binary
# search tree.Include methods for inserting and searching for 
# elements in the binary tree.

# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None
        
#     def __str__(self):
#         return str(self.value)

# class BinarySearchTree:
#     def __init__(self):
#         self.root = None

#     def insert(self, value):
#         if self.root is None:
#             self.root = Node(value)
#         else:
#             self._insert_recursive(self.root, value)

#     def _insert_recursive(self, node, value):
#         if value < node.value:
#             if node.left is None:
#                 node.left = Node(value)
#             else:
#                 self._insert_recursive(node.left, value)
#         elif value > node.value:
#             if node.right is None:
#                 node.right = Node(value)
#             else:
#                 self._insert_recursive(node.right, value)

#     def search(self, value):
#         return self._search_recursive(self.root, value)

#     def _search_recursive(self, node, value):
#         if node is None or node.value == value:
#             return node
#         if value < node.value:
#             return self._search_recursive(node.left, value)
#         else:
#             return self._search_recursive(node.right, value)

# bst = BinarySearchTree()
# bst.insert(5)
# bst.insert(3)
# bst.insert(7)
# bst.insert(2)
# bst.insert(4)
# bst.insert(6)
# bst.insert(8)

# print("Searching for elements:")
# print(bst.search(4))
# print(bst.search(9))

# 6. Write a Python program to create a class representing a stack
# data structure. Include methods for pushing and popping elements.

# class Stack:
#     def __init__(self):
#         self.items = []

#     def push(self, item):
#         self.items.append(item)

#     def pop(self):
#         if not self.is_empty():
#             return self.items.pop()
#         else:
#             return "Cannot pop from an empty stack."

#     def is_empty(self):
#         return len(self.items) == 0

#     def size(self):
#         return len(self.items)

#     def peek(self):
#         if not self.is_empty():
#             return self.items[-1]
#         else:
#             return "Empty stack."

# stack = Stack()

# stack.push(0)
# stack.push(1)
# stack.push(2)
# stack.push(3)
# stack.push(4)

# print("Stack size:", stack.size())
# print("Top element:", stack.peek())

# popped_item = stack.pop()
# print("\nPopped item:", popped_item)
# print("\nStack size:", stack.size())
# print("Top element:", stack.peek())

# stack1 = Stack()

# print("\nStack size:", stack1.size())
# popped_item = stack1.pop()
# print("\nPopped item:", popped_item) 

# 7. Write a Python program to create a class representing a linked 
# list data structure. Include methods for displaying linked list 
# data, inserting and deleting nodes.

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def display(self):
#         current = self.head
#         while current:
#             print(current.data, end=" ")
#             current = current.next
#         print()

#     def insert(self, data):
#         new_node = Node(data)
#         if not self.head:
#             self.head = new_node
#         else:
#             current = self.head
#             while current.next:
#                 current = current.next
#             current.next = new_node

#     def delete(self, data):
#         if not self.head:
#             return

#         if self.head.data == data:
#             self.head = self.head.next
#             return

#         current = self.head
#         prev = None
#         while current and current.data != data:
#             prev = current
#             current = current.next

#         if current:
#             prev.next = current.next

# linked_list = LinkedList()

# linked_list.insert(1)
# linked_list.insert(2)
# linked_list.insert(3)
# linked_list.insert(4)

# print("Initial Linked List:")
# linked_list.display()

# linked_list.insert(5)
# print("After inserting a new node (5):")
# linked_list.display()

# linked_list.delete(2)
# print("After deleting an existing node (2):")
# linked_list.display()

# 8. Write a Python program to create a class representing a shopping cart. Include methods
# for adding and removing items, and calculating the total price.

# class ShoppingCart:
#     def __init__(self):
#         self.items = []
#     def add_item(self, item_name, qty):
#         item = (item_name, qty)
#         self.items.append(item)
#     def remove_item(self, item_name):
#         for item in self.items:
#             if item[0] == item_name:
#                 self.items.remove(item)
#                 break
#     def calculate_total(self):
#         total = 0
#         for item in self.items:
#             total += item[1]
#         return total

# cart = ShoppingCart()

# cart.add_item("Papaya", 100)
# cart.add_item("Guava", 200)
# cart.add_item("Orange", 150)

# print("Current Items in Cart:")
# for item in cart.items:
#     print(item[0], "-", item[1])

# total_qty = cart.calculate_total()
# print("Total Quantity:", total_qty)

# cart.remove_item("Orange")
# print("\nUpdated Items in Cart after removing Orange:")
# for item in cart.items:
#     print(item[0], "-", item[1])

# total_qty = cart.calculate_total()
# print("Total Quantity:", total_qty)

# 9. Write a Python program to create a class representing a stack data structure. Include methods for pushing,
# popping and displaying elements.


# class Stack:
#     def __init__(self):
#         self.items = []

#     def push(self, item):
#         self.items.append(item)

#     def pop(self):
#         if not self.is_empty():
#             return self.items.pop()
#         else:
#             raise IndexError("Cannot pop from an empty stack.")

#     def is_empty(self):
#         return len(self.items) == 0

#     def display(self):
#         print("Stack items:", self.items)

# stack = Stack()
# stack.push(10)
# stack.push(20)
# stack.push(30)
# stack.push(40)
# stack.push(50)
# stack.display()
# popped_item = stack.pop()
# popped_item = stack.pop()
# popped_item = stack.pop()
# print("Popped item:", popped_item)
# popped_item = stack.pop()
# print("Popped item:", popped_item)

# stack.display()

# 10. Write a Python program to create a class representing a queue data structure.
# Include methods for enqueueing and dequeueing elements.
# Define a class called Queue to implement a queue data structure

# class Queue:
#     def __init__(self):
#         self.items = []
#     def enqueue(self, item):
#         self.items.append(item)
#     def dequeue(self):
#         if not self.is_empty():
#             return self.items.pop(0)
#         else:
#             raise IndexError("Cannot dequeue from an empty queue.")

#     def is_empty(self):
#         return len(self.items) == 0

# queue = Queue()

# queue.enqueue(10)
# queue.enqueue(20)
# queue.enqueue(30)
# queue.enqueue(40)
# queue.enqueue(50)

# print("Current Queue:", queue.items)

# dequeued_item = queue.dequeue()
# print("Dequeued item:", dequeued_item)
# dequeued_item = queue.dequeue()
# print("Dequeued item:", dequeued_item)

# print("Updated Queue:", queue.items) 

# # Define a class called ShoppingCart to represent a shopping cart
# class ShoppingCart:
#     # Initialize the shopping cart with an empty list of items
#     def __init__(self):
#         self.items = []
#     # Add an item with a name and quantity to the shopping cart
#     def add_item(self, item_name, qty):
#         item = (item_name, qty)
#         self.items.append(item)
#     # Remove an item with a specific name from the shopping cart
#     def remove_item(self, item_name):
#         for item in self.items:
#             if item[0] == item_name:
#                 self.items.remove(item)
#                 break
#     # Calculate and return the total quantity of items in the shopping cart
#     def calculate_total(self):
#         total = 0
#         for item in self.items:
#             total += item[1]
#         return total
# # Example usage
# # Create an instance of the ShoppingCart class
# cart = ShoppingCart()
# # Add items to the shopping cart
# cart.add_item("Papaya", 100)
# cart.add_item("Guava", 200)
# cart.add_item("Orange", 150)

# # Display the current items in the cart and calculate the total quantity
# print("Current Items in Cart:")
# for item in cart.items:
#     print(item[0], "-", item[1])

# total_qty = cart.calculate_total()
# print("Total Quantity:", total_qty)

# # Remove an item from the cart, display the updated items, and recalculate the total quantity
# cart.remove_item("Orange")
# print("\nUpdated Items in Cart after removing Orange:")
# for item in cart.items:
#     print(item[0], "-", item[1])

# total_qty = cart.calculate_total()
# print("Total Quantity:", total_qty) 

# 11. Write a Python program to create a class representing a bank. Include methods for managing 
# customer accounts and transactions.

# Define a class called Bank to implement a simple banking system
class Bank:
    # Initialize the bank with an empty dictionary to store customer accounts and balances
    def __init__(self):
        self.customers = {}

    # Create a new account with a given account number and an optional initial balance (default to 0)
    def create_account(self, account_number, initial_balance=0):
        if account_number in self.customers:
            print("Account number already exists.")
        else:
            self.customers[account_number] = initial_balance
            print("Account created successfully.")

    # Make a deposit to the account with the given account number
    def make_deposit(self, account_number, amount):
        if account_number in self.customers:
            self.customers[account_number] += amount
            print("Deposit successful.")
        else:
            print("Account number does not exist.")

    # Make a withdrawal from the account with the given account number
    def make_withdrawal(self, account_number, amount):
        if account_number in self.customers:
            if self.customers[account_number] >= amount:
                self.customers[account_number] -= amount
                print("Withdrawal successful.")
            else:
                print("Insufficient funds.")
        else:
            print("Account number does not exist.")

    # Check and print the balance of the account with the given account number
    def check_balance(self, account_number):
        if account_number in self.customers:
            balance = self.customers[account_number]
            print(f"Account balance: {balance}")
        else:
            print("Account number does not exist.")

# Example usage
# Create an instance of the Bank class
bank = Bank()

# Create customer accounts and perform account operations
acno1= "SB-123"
damt1 = 1000
print("New a/c No.: ",acno1,"Deposit Amount:",damt1)
bank.create_account(acno1, damt1)

acno2= "SB-124"
damt2 = 1500
print("New a/c No.: ",acno2,"Deposit Amount:",damt2)
bank.create_account(acno2, damt2)

wamt1 = 600
print("\nDeposit Rs.",wamt1,"to A/c No.",acno1)
bank.make_deposit(acno1, wamt1)

wamt2 = 350
print("Withdraw Rs.",wamt2,"From A/c No.",acno2)
bank.make_withdrawal(acno2, wamt2)

print("A/c. No.",acno1)
bank.check_balance(acno1)

print("A/c. No.",acno2)
bank.check_balance(acno2)

wamt3 = 1200
print("Withdraw Rs.",wamt3,"From A/c No.",acno2)
bank.make_withdrawal(acno2, wamt3)

acno3 = "SB-134"
print("A/c. No.",acno3)
bank.check_balance(acno3)  # Non-existent account number 