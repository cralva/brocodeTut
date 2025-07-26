def say_hello():
    return "Hello"

message = say_hello()
print(message)
print()

def say_hello():
    print("Hello")

message = say_hello()
print(message) #will print 'None' since the function has to return statement

def add(x, y):
    z = x + y
    print(z)

first = add(10,15)
print(first)

print(add(10,5)) #will print none since we dont have a return function

def add(x, y):
    z = x + y
    return z

print(add(10,5)) #will work now since we added a return function