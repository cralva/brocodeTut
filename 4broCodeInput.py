# input() = a function that prompts the suer to enter data
#           returns the entered data as a string

name = input("What is your name? ")
age = int(input("How old are you? ")) #can cast when asking for the input

#dont need to do this -> age = int(age) #need to cast since age is a str
age = age + 1

print(f"Hello {name}!")
print("Happy birthday")
print(f"You are {age} years old!")