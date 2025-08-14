# *args           = allows you to pass multiple non-key arguments/ will pack all of the arguments into a tuple. this is a positional
# **kwargs        = allows you to pass multiple keyword-arguments/ will pack all of the arguments into a dictionary. This is a keyword
#                  * unpacking operator
#                 1. positional 2. default 3. keyword 4. ARBITRARY


def add_first(a, b):
    return a + b

print(add_first(1, 2,)) #will work
# print(add(1, 2, 5)) #won't work because our function only has two parameters. we need to add another parameter



def add_second(*args): #this is so there is no set limit on the amount of parameters that we have
    print(type(args))

add_second(1, 2, 5) #we get tuple because that is what we are calling for in the line above



def add_third(*args): #the 'args' can be any name. it won't affect the function. the only thing that is necessary is the *
    total = 0
    for arg in args:
        total += arg
    return total

print(add_third(1, 2, 3, 4,))



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
              apt="100", #this was added in later
              city="Detroit", 
              state="MI", 
              zip="54321")

def shipping_label(*args, **kwargs): #positional arguments need to go first. it will not work otherwise. will show example. if we do **kwards, *args then it will not work
    for arg in args:
        print(arg, end=" ") #this will print out dr spongebob squarepants in a straight line
    print()
    for value in kwargs.values():
        print(value, end=" ") #this will print out the address in one line

shipping_label("Dr.", "Spongebob", "Squarepants", "3rd", #positional args,
               street="123 Fake St", #keyword args
               apt="100",
               city="Detroit",
               state="Michigan",
               zip="54321")

print()


#option 2 for function. this is so we have a different line for our address kwarg
def new_shipping(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()

    if "pobox" in kwargs and "apt" in kwargs:
        print(f"{kwargs.get('street')}, {kwargs.get('pobox')}, {kwargs.get('apt')}") #we had to move this to the top because order matters. if we had an if for apt then then would have ran regardless if there was an elif statement that included both. this needs to be at the top
    elif "apt" in kwargs:
        print(f"{kwargs.get('street')}, {kwargs.get('apt')}") #the kwargs.get('apt') was added late to show the example of adding a late argument to code
    elif "pobox" in kwargs:
        print(f"{kwargs.get('street')}, {kwargs.get('pobox')}")
    else:
        print(f"{kwargs.get('street')}") #this was added so we don't have the issue of getting none as a returned value
    
    print(f"{kwargs.get('city')}, {kwargs.get('state')}, {kwargs.get('zip')}")



new_shipping("Dr.", "Spongebob", "Squarepants", "3rd", #positional args,
               street="123 Fake St", #keyword args
               apt="100", #if we remove this then the kwargs.get('apt') will return none. Thats why we added an if statement to the code. we wont get none back if there is no apt number
               city="Detroit",
               state="Michigan",
               zip="54321",
               pobox="PO 1001") #showing how to add a new arugment for the if else statements