# function = a block of reusable code
# place () after the function name to invoke it

#sing happy bday three times
print('happy bday')
print('you are old')
print('happy bday to you')
print()

print('happy bday')
print('you are old')
print('happy bday to you')
print()

print('happy bday')
print('you are old')
print('happy bday to you')
print()
 

#better way of doing this
def sing(): #syntax is def nameoffunction():
    print('happy bday')
    print('you are old')
    print('happy bday to you')
    print()

sing() #calling the function this way will execute the code within the function
sing()
sing() #will call it three times

#we can send data to a function. using 'arguments' (the stuff that goes into the parentheses)
def sing(name, age): #add a 'parameter' in the parentheses to be able to use an argument when you call the function (added name first and then added age)
    print(f'happy bday {name}')
    print(f'{name} are {age} years old')
    print(f'happy bday to {name}')
    print()

sing("Cris", 27) #tossing the argument in the function to fulfill the parameter
#can use different arugments as long as we call it
#we cant have more arugments than parameters and vice versa. the parameters must be met so we have to add an age argument
sing("Syd", 26)
sing("Ted", 3)
sing("Bella", 0) #order matters. if we switch the arugments/paramenters then it will change

#new function to display an invoice with three parameters: username, amount, due_date)
def display_invoice(name, date, amount):
    name = name.upper()
    print(f'---{name}---')
    print(f'{date}')
    print(f'---${amount}---')

display_invoice("cristian alvarez", "7/8/2025", 5500)
display_invoice("syd alvarez", "07/20/2025", 10000)
display_invoice("ted alvarez", "08/20/2025", 25000)
display_invoice("bella alvarez", "09/25/2025", 100000)

# return = statement used to end a function and send a result back to the caller
def add(x, y):
    z = x + y
    return z

def subtract(x, y):
    z = x - y
    return z

def multiply(x, y):
    z = x * y
    return z

def divide(x, y):
    z = x / y
    return z

print(add(10, 5)) # we have to turn it into an object before using the return function. without the return then we wouldnt be getting anything from it
print(subtract(8, 2)) #imagine that when we're calling the function it beceomes the return value for each of these
print(multiply(20, 10))
print(divide(30, 3))

#create a function that will create a full name
def create_name(first, second, last):
    first = first.capitalize()
    second = second.capitalize()
    last = last.capitalize()
    return first + " " + second + " " + last

full_name = create_name("cristian", "alejandro", "alvarez") #if we run this then nothing will happen. we have to print it
print(full_name) #this will make it work