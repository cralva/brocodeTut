# collection = single "variable" used to store multiple values
#   List = [] ordered and changeable. Duplicates OK
#   Set = {} unordered and immutable, but Add/Remove OK. NO duplicates
#   Tuple = () ordered and unchangeable. Duplicates OK. FASTER


#   List = Flexible and ordered (like a shopping list)

#   Tuple = Fixed and ordered (like coordinates or a birthdate)

#   Set = Unique and unordered (like a collection of different stamps)

'''
fruits = ["apple", "orange", "bannana", "coconut"]

print(fruits[1]) # use [] index operator to print/access a specific element /starts at 0

print(fruits[0:3]) # gives us the range

print(fruits[0:4:2]) # gives us a step

print(fruits[::]) # will assume the beginning and the end
#               works [:4] = will assume its starting at the beginning
#               works [1:] = will assume that its to the end
print(fruits[::-1]) # reverses the order

for fruit in fruits:   #iterate over them with a for loop
    print(fruit)

# print(dir(fruits)) #will print all of the methods with collection
# print(help(fruits)) #will print a description for all of the methods
print(len(fruits)) # will return the length of the collection
print("apple" in fruits) # will return a boolean, True or False, if that element is in the collection

# methods with lists
fruits.append("tangerine") # will add an element to the end of a list
fruits.remove("coconut") #will remove an element
fruits.insert(0, "grapes") #will insert an element at a specific index
fruits.sort() #will sort list in alphabetical order
fruits.reverse() # will reverse the original list (not in alphabetical order)
#            if you want to reverse the list in alphabetical order, then you need to have the sort method above it
fruits.clear() # will clear the elements
fruits.index("apple") # will return the index number that the element is
fruits.count("grapes") # will count how many times "grapes" are in the list

print(fruits)

fruits[0] = "pineapple" # will change the list/ will replace apple with pineapple

for fruit in fruits:
    print(fruit)
'''



'''
fruits = {"apple", "orange", "bannana", "coconut"} #can add a duplicate but it will only be printed once
# print(dir(fruits)) #will print all of the methods with collection
# print(help(fruits)) #will print a description for all of the methods
# print(len(fruits)) # will return the length of the collection
# print("apple" in fruits) # will return a boolean, True or False, if that element is in the collection

# print(fruits[0]) # will return an error since sets are unordered there is no set index for an element

#fruits.add("pineapple") # will add an element
#fruits.remove("apple") # will remove an element
#fruits.pop() # will remove the last value, but it will be different every time since sets are unordered
#fruits.clear() # will clear the set

print(fruits)
'''


fruits = ("apple", "orange", "bannana", "coconut")
# print(dir(fruits)) #will print all of the methods with collection
# print(help(fruits)) #will print a description for all of the methods
# print(len(fruits)) # will return the length of the collection
# print("apple" in fruits) # will return a boolean, True or False, if that element is in the collection

fruits.index("apple") # will find the index of the element
fruits.count("apple") # will count how many times the element is in the tuple

for fruit in fruits:
    print(fruit)
