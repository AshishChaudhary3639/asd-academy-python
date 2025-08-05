import pdb

def add(a, b):
    pdb.set_trace()
    print("I am inside the function")
    result = a + b
      # Program will pause here
    return result

x = 10
y = 3
print("Setting the breakpoint")
# pdb.set_trace()
print(add(x, y))  # When you run this, it will stop at the breakpoint
print("Hello is getting Printed")
print("This is the last line")