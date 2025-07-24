#Function Call and Function Definition
#Function of Addition
def asif(a,b,c=20):
    d=a+b+c
    return d

def subtraction(a,b):
    s=a-b
    return s

# add=asif(10,10,30)
# print(add)
# print("Workinjg with fuctions")
# addition(9,10)
# s=subtraction(10,5)
# print(s)
# print(subtraction(100,100))

# def name(n="Rahul"):
#     print(n)
# name()
# name("Abhishek")

# def even_or_odd(chandhu):
#     result="Odd"
#     if chandhu%2==0:
#         # print("Number is Even")
#         result="Even"
#         return result

#     else:
#         return result
#         # print("Number is Odd")

# num=int(input("Enter the Number"))
# # print(even_or_odd(num))
# print(even_or_odd(num))
# if result==1:
#     print("Even")
# else:
#     print("Odd")
# addition=lambda x,y:x+y
# print(addition(5,9))
# square=lambda asif:asif**2
# print(square(9,2))
cube=lambda y:y**3
print(cube(5))