#Read data from a file
# file1=open("sample.txt","r")
# # data=file1.read()
# data=file1.readline()
# # data=file1.readlines()
# print(data)
# file1.close()

#Writing Data on a file
# file2=open("sample.txt","a")
# file2.write("\nThis is my first program on files\n")
# # file2.write("Harshul is learning Python programming\t")
# # file2.write("I am working\n")
# file2.write("I am appending the file")
# file2.close()

#working with keyword
# with open("mohit.txt","r") as file2:
#     data=file2.read()
# print(data)

# with open("sample.txt","r") as jasmail:
#     harshul=jasmail.read()
# print(harshul)

# with open("umang.txt","a") as ronit:
#     # ronit.write("This is the file of Umang")
#     ronit.write("I am working on Python")
# import os
# os.remove("umang.txt")

# with open("myfile.txt","r") as file12:
#     data=file12.read()
# print(data)
# if "Python" in data:
#     print("Python is present")
# else:
#     print("Python is not present")


# with open("student.txt","w") as file:
#     num=5
#     for x in range(1,11):
#         file.write(f"{num}x{x}={num*x}\n")

with open("student.txt","r") as file1:
    data1=file1.read()

with open("student2.txt","w") as file2:
        file2.write(data1)

# if data1==data2:
#     print("Both files are same")
# else:
#     print("Files are different")