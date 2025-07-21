# variable = a container for a value (string, integer, float, boolean)
#            a variable behaves as if it was the value it contains
from tkinter.messagebox import YESNO

# Strings
first_name = "Bro"
food = "Pizza"
email = "bro123@fake.com"

print(first_name)

print(f"Hello {first_name}!")
print(f"You like {food}")
print(f"your email is {email}")

# Integers
age = 25 #cannot be in quotes since only strings are in quotes
quantity = 3
numOfStudents = 30

print(f"You are {age} years old")
print(f"You are buying {quantity} of your favorite food {food}")
print(f"Your class has {numOfStudents} students!")

# Floats (decimals)

price = 10.99
gpa = 3.2
distance = 5.5

print(f"The price is ${price}")
print(f"Your gpa is {gpa}")
print(f"You ran {distance}KM")

# booleans (either True or False)

is_student = True
graduated = False
forSale = True

print(f"Are you a student?: {is_student}")

#               booleans are typically used for if and loops
if is_student:
    print("You are a student!")
else:
    print("You are not a student")

if graduated:
    print("Good job")
else:
    print("You did not graduate!")

# first assignment
first_name = "Cristian"
age = 27
weight = 190.7
isMale = True
