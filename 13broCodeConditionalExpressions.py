# conditional expression = a one-line shortcut for the if-else statement (ternary operator)
#                          print or assign one of two values based on a condition
#                          x if condition (is true) else Y
'''
num = 5

print("Positive" if num > 0 else "Negative")
'''


'''
num = 7
result = "EVEN" if num % 2 == 0 else "ODD"

print(result)
'''


'''
a = 6
b = 7

max_num = a if a > b else b
min_num = a if a < b else b

print(max_num)
print(min_num)
'''


'''
age = 20

status = "Adult" if age > 18 else "Child"

print(status)
'''


'''
temp = 30

weather = "HOT" if temp > 20 else "COLD"

print(weather)
'''



userRole = "Guest"

accessLevel = "Full access" if userRole == "Admin" else "Limited Access"

print(accessLevel)
