# class Student:
#     name="Rohit" #Class Attributes
#     grade="12th"
#     marks=200

#     def display(self):  #Methods
#         # print(self)
#         print(f"My Name is {self.name}")
#         print(f"My class is {self.grade}")
    
#     @staticmethod  #Decorator
#     def get_info():
#         print(f"This is a Static Method")

# obj1=Student()  #Object
# # print(obj1.name)
# # print(obj1.marks)
# # obj1.display()
# obj1.name="Chandhu"
# obj1.display()
# obj1.get_info()
# obj2=Student()
# obj2.grade="11th"
# obj2.display()
# obj2.get_info()
# parth.marks=500
# print(parth.marks)
# print(Student.marks)
# parth.display()
# parth.get_info()
# Student.get_info(parth)
# Student.display()
# Student.display(parth)
# mohit=Student()
# mohit.display()
# mohit.name="Mohit"  #Object Attributes
# mohit.city="Mumbai"
# mohit.display()
# mohit.get_info()

class Employee:
    company="Microsoft"

    def __init__(self,city,salary):  #Constructor   Dunder Methods
        print("Object is created")
        self.salary=salary
        self.city=city


    def display(self):  #Methods/Functions
        print(f"My company name is {self.company}")
        print(f"My city is {self.city} and my salary is {self.salary}")
asif=Employee("Srinagar",50000)
ayush=Employee("Mumbai",550000)
ayush.company="Google"
ayush.display()
asif.display()
# sawan=Employee("Bangalore",65000)
# ayush.display()
# rahul=Employee()
# asif=Employee()

class Calculator:
    name='Calculator'

    def __init__(self,num):
        self.num=num

    def square(self):
        print(f"My programe name is {self.name}")
        print(f"The square of number is {self.num**2}")

    def cube(self):
        print(f"My programe name is {self.name}")
        print(f"The cube of number is {self.num**3}")

calcy=Calculator(5)
calcy.square()
calcy.cube()
calcy2=Calculator(8)
calcy2.name="Binary Calculator"
calcy2.cube()

# suraj=Calculator(7)
# suraj.cube()
# suraj.square()