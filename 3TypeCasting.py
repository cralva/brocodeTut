# Typecasting = the process of converting a variable from one data type to another
#               str(), int(), float(), bool()

name = "Cristian Alvarez"
age = 27
gpa = 2.9
isStudent = True

type(name)  #no output. we need to print it so it gets executed in the console

print(type(name))
print(type(age))

gpa = int(gpa)
print(gpa)

age = str(age) #could also just change data type in the print without
print(age) #making a new variable = print(str(age))

name = bool(name)

print(name) #will return True, if name is blank then it will be false
