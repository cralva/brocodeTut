# *args           = allows you to pass multiple non-key arguments/ will pack all of the arguments into a tuple
# **kwargs        = allows you to pass multiple keyword-arguments/ will pack all of the arguments into a dictionary
#                  * unpacking operator
#                 1. positional 2. default 3. keyword 4. ARBITRARY


def add(a, b):
    return a + b

print(add(1, 2,)) #will work
# print(add(1, 2, 5)) #won't work because our function only has two parameters. we need to add another parameter

def add(*args): #this is so there is no set limit on the amount of parameters that we have
    print(type(args))

add(1, 2, 5) #we get tuple because that is what we are calling for in the line above

def add(*args): #the 'args' can be any name. it won't affect the function. the only thing that is necessary is the *
    total = 0
    for arg in args:
        total += arg
    return total

print(add(1, 2, 3, 4,))

def display_name(*args):
    for arg in args:
        print(arg, end=" ")

display_name("Sir", "Cris", "Alvarez")
print()
##kwargs

def print_address(**kwargs):
    print(type(kwargs)) #will print that it is a dictionary since that is what it is
    for value in kwargs.values(): #will print the values
        print(value)
    for key in kwargs.keys(): #will print the keys
        print(key)
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_address(street="123 Fake St", 
              city="Detroit", 
              state="MI", 
              zip="54321")