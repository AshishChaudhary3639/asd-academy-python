# Single Inheritance
# class Parent:
#     name="Microsoft"

#     def show_parent(self):
#         print("This is a Parent Class")

# class Child(Parent):
#     # name="Microsoft"

#     # def show_parent(self):
#     #     print("This is a Parent Class")

#     def show_child(self):
#         print(f"This is a Child class{self.name}")

# obj2=Child()
# obj2.show_child()
# obj2.show_parent()
# print(obj2.name)
 
#Mutiple Inheritance
# class Father:
#     name="Microsoft"
#     def show_father(self):
#         print("This is a Father Class")

# class Mother:
#     company="HP"
#     def show_mother(self):
#         print("This is a Mother class")

# class Child(Father,Mother):
#     marks=500
#     def show_child(self):
#         print("This is a Child Class")

# obj=Child()
# obj.show_child()
# obj.show_father()
# obj.show_mother()
# print(obj.name)

#Multilevel Inheritance
# class Father: #Parent Class
#     name="Microsoft"
#     def __init__(self):
#         print("Father Class Constructor Is Called")

#     def show_father(self):
#         print("This is a Father Class")

# class Mother(Father): #Derived Class/Child Class
#     company="HP"
#     def __init__(self):
#         super().__init__()
#         print("Mother Class Constructor  Is Called")

#     def show_mother(self):
#         print("This is a Mother class")

# class Child(Mother): #Derived Class
#     marks=500
#     def __init__(self):
#         super().__init__()
#         print("Child Class Constructor Is Called")

#     def show_father(self):  #Function Overridinng
#         print("===This is a Father Class in Child Class===")

#     def show_child(self):
#         print("This is a Child Class")

# obj=Child()
# obj.show_child()
# obj.show_father()
# obj.show_mother()
# print(obj.name)

# print(5+10)
# print("AS"+"IF")
# print([1, 2] + [3, 4]) # [1, 2, 3, 4] (list concat)

# class Employee:
#     name="Microsoft"
#     salary=500000

#     # def show_name(self):
#     #     print(f"Company Name is {self.name}")
#     @classmethod
#     def change_name(cls,name,salary):
#         cls.name=name
#         cls.salary=salary
# # obj=Employee()
# # # obj.show_name()
# # print(obj.name)
# # obj.name="Oracle"
# # print(obj.name)
# print(Employee.name)
# print(Employee.salary)
# Employee.change_name("Oracle",900000)
# print(Employee.name)
# print(Employee.salary)



# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     # Overload the '+' operator
#     def __add__(self, other):
#         return Point(self.x + other.x, self.y + other.y)

#     def __str__(self):
#         return f"({self.x},Asif {self.y})"

# # Create two Point objects
# p1 = Point(3, 4)
# p2 = Point(1, 2)
# # Add them using the overloaded '+' operator
# p3 = p1 + p2
# print("Hello")

# print("p1 + p2 =", p3)

# class Animal:
#     def speak(self):
#         print("Animal makes a sound!")
# # Child class (Dog)
# class Dog(Animal):
#     def speak(self):
#         print("Dog barks!")
# # Child class (Cat)
# class Cat(Animal):
#     def speak(self):
#         print("Cat meows!")
# # Creating objects
# animal=Animal()
# dog = Dog()
# cat = Cat()
# # Polymorphism in action
# dog.speak() # Output: Dog barks!
# cat.speak() # Output: Cat meows
# animal.speak()

class BankAccount:
    company="Microsoft" #Public Attribute
    def __init__ (self, balance):
        self.__balance = balance # private attribute
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance:{self. balance}")
    def get_balance(self):
        return self.__balance # Public method to access private balance
    
# Creating an object of BankAccount
account = BankAccount(1000)
# Accessing balance using public method
print(account.get_balance()) # Output: 1000
# Trying to access the private balance directly will raise an error
account.company="Google"
print(account.company)
print(account.__balance) # This will give an AttributeError
# Using the deposit method to modify balance
# account.deposit(500) # Output: Deposited 500. New balance: 1500