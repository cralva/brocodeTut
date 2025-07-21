friends = 10

# friends = friends + 1
# friends += 1 #same thing as ^ (augemented assignment operator)

# friends = friends - 2
# friends -= 2

# friends = friends * 3
# friends *= 3

# friends = friends / 2
# friends /= 2

# friends = friends ** 2
# friends **= 2

# remainder = friends % 3 #output the remainder . answer is 1
#friends %= 3

'''
x = 3.14
y = -4
z = 5

result = round(x) #rounds to the nearest whole number
result = abs(y)  #outputs absolute value
result = pow(z, 4)  #outputs exponenet. first is the value and the second is the power
result = max(x, y, z) #outputs the highest number
result = min(x, y, z) #outputs the lowest number
print(result)
'''

'''
import math   #math module

x = 9

print(math.pi) # will print pie
print(math.e)   # will print the exponential constant
result = math.sqrt(x) #prints the square root
result = math.ceil(x)  #will round up
result = math.floor(x) #will round down
print(result)

'''

'''
import math

radius = float(input("Enter the radius of a circle: "))

circum = 2 * math.pi * radius #was able to use math.pi for pi

# print(f"The circumference is {circum}")
print(f"The circumference is {round(circum, 2)}") # rounding to the second decimal


radius = float(input("Enter the radius of a circle: "))

area = math.pi * pow(radius, 2)

#print(f"The area of the cirlce is: {area}cm^2")
print(f"The area of the circle is: {round(area, 2)}")
'''

import math  #formula to calculate the hypothenuse of a right angled triangle

a = float(input("Enter side A: "))
b = float(input("Enter side B: "))

c = math.sqrt(pow(a, 2) + pow(b, 2))

print(f"Side C = {c}")

