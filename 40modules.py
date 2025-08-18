# module = a file containing code you want to include in your program
#          use 'import' to include a module (built-in or your own)
#          useful to break up a large program reusable separeate files

#print(help("modules")) #this will print out all of the list of all of modules in the standard python library

#print(help("math")) #will list all of the variables and modules found within the 'named' module

import math #this is how we import a module. we need to use 'import' and then the module name
print(math.pi)
import math as m #another way of importing a module. instead of using the name of the module we can just use to the nickname that we chose instead of using the full name
print(m.pi)


#create our own module. create new file

import exfor40

result = exfor40.pi
print(result)

squared_ex = exfor40.square(3)
print(squared_ex)

cubed_ex = exfor40.cube(3)
print(cubed_ex)

circum_ex = exfor40.circumferance(4)
print(circum_ex)

area = exfor40.area(4)
print(area)