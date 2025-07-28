#Read a file
# f=open("sample.txt","r")
# # data=f.read()
# # data=f.readline(50)
# # data=f.readlines()
# # print(f)
# print(data)
# f.close()

#Writing data on file
# f=open("student.txt","a")
# f.write("\nWe are learning Python course")
# f.close()

# with open("sample.txt","r")as f1:
#     data=f1.read()
#     print(data)

# with open("student.txt","w") as f2:
#     f2.write("We are using the with statement")

# with open("myfile.txt","r")as f:
#     data=f.read()

# if "Python" in data:
#     print("Python is present")
# else:
#     print("Python is not present")

# with open("mutiplication.txt","a") as f:
#     num=int(input("Enter the Number:"))
#     for i in range(1,11):
#         f.write(f"{num}*{i}={num*i}\n")

with open("multiplication.txt","r") as f1:
    data=f1.read()
with open("copy_multiplication.txt","w") as f2:
    f2.write(data)