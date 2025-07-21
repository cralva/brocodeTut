# dictionary = a collection of {key:value} pairs
#              ordered and changeable. no duplicates

capitals = {"USA": "Washington D.C",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}

# print(dir(capitals)) #shows all methods
# print(help(capitals)) #explains all methods

# print(capitals.get("Russia")) #gets the value of the key. will return Moscow
# print(capitals.get("Japan")) # will return "None"

# if capitals.get("Japan"):
#     print("That capital exists")
# else:
#     print("That capital does not exist") #will print this since japan is not a key in our dictionary and will print "None"

# capitals.update({"Germany": "Berlin"}) #adds
#
# capitals.update({"USA": "Detroit"}) #updates the dictionary
#
#
# capitals.pop("China") #will remove the key and value that is in the argument
# capitals.popitem() #will remove the last key and value of the dictionary
#
# capitals.clear() #will clear the entire dictionary
#
# capitals.keys() #will give you the keys of the dictionary

keys = capitals.keys() #will return all the keys in the dictionary
print(keys)

for key in capitals.keys(): #will iterate keys since they are "objects"?
    print(key)

values = capitals.values() #will return all the values in the dictionary
print(values)

for value in capitals.values(): #will iterate keys since they are "objects"?
    print(value)

items = capitals.items() #will return a 2d list of the key and value
print(items)

for key, value in capitals.items():
    print(f"{key}: {value}")



