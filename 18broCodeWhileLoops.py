# while loop = execute some code WHILE some condition remains true

#name = input("Enter your name: ")

'''
if name == "":
    print("You did not enter anything")
else:
    print(f"Hello {name}")
'''

#instead of using if and only getting asked once we can use
#while and keep asking
'''
while name == "": #if True then will print and reprompt. if its false then it will leave and print bottom print statement
    print("You did not enter anything")
    name = input("Enter your name: ") #need to reprompt or it will result in an infinite loop

print(f"Hello {name}") #will print this once the above condition is false
'''

'''
age = int(input("Enter your age: "))

while age < 0:
    print("Age cannot be negative")
    age = int(input("Enter your age: "))

print(f"You are {age} years old!")
'''



'''
food = input("Enter a food you like (q to quit): ")

while not food == "q":
    print(f"You like {food}")
    food = input("Enter a food you like (q to quit): ")

print("bye")
'''



num = int(input("Enter a number between 1 - 10: "))

while num < 1 or num > 10:
    print(f"{num} is not valid")
    num = int(input("Enter a number between 1 - 10: "))

print(f"Your number is {num}")
