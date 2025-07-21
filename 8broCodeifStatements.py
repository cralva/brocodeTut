# if = Do some code only IF some condition is True
#       Else do something else

age = int(input("Enter your age: "))

'''
if age >= 18:
    print("You are now signed up!")
else:  #last resort
    print("You must be 18 or older to sign up!")
'''
'''
#elif
if age >= 18:
    print("You are now signed up!")
elif age < 0:               
    print("You have been born yet")
elif age >= 100:            #the order matters. wont give the right output. needs to go higher
    print("You are too old to sign up")
else:  #last resort
    print("You must be 18 or older to sign up!")
'''

if age >= 100:            #the order matters. wont give the right output. needs to go higher
    print("You are too old to sign up")
elif age >= 18:
    print("You are now signed up!")
elif age < 0:
    print("You have been born yet")
elif age >= 100:
    print("You are too old to sign up")
else:  #last resort
    print("You must be 18 or older to sign up!")

response = input("Would you like food? (Y/N): ")

if response == "Y":
    print("Good, dinner is ready.")
else:
    print("No dinner for you then")

name = input("Enter your name: ")

if name == "":
    print("You did not type in your name!")
else:
    print(f"Hello {name}!")

#if with booleans

for_sale = True

if for_sale:
    print("This item is for sale")
else:
    print("This item is not for sale")

online = False

if online:
    print("The user is online")
else:
    print("The user is offline")