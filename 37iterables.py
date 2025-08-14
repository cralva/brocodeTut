# Iterables = An object/collection that can return its elements one at a time, allowing it to be iterated over in a loop

numbers = [1, 2, 3, 4, 5]
for number in numbers: #number becomes the variable in the list: number = 1, number = 2, number = 3, etc and contiues to iterate until the end of the list. We can name the variable anything that we want
    print(number)

for number in reversed(numbers): #using the reversed() function means that this iteration will go backwards
    print(number, end="-") #we can use end keyword argument to alter how the print function is handled/ by default its a new space but we can change that and use a dash instead (we use use anything to put after each iteration)


numbers2 = (6, 7, 8, 9, 10) #can even iterate over tuples 
for number in numbers2:
    print(number)


fruits = {"apple", "orange", "banana", "coconut"}
for fruit in fruits: #using a set for this iterable
    print(fruits)

# for fruit in reversed(fruits): #this will not work since we cannot reverse sets
#     print(fruits)


name = "Cristian Alvarez" #we can iterate over strings as well
for character in name: 
    print(character)
for character in name: 
    print(character, end=" ")

print()#will give us a new line just to make the terminal look organized

my_dictionary = {"A": 1, "B":2, "C":3} 
for key in my_dictionary:#by default, the iteration will return the keys and not the values
    print(key)
for value in my_dictionary.values(): #the .values() method whill get us the values
    print(value)
for key, value in my_dictionary.items(): #this will get us the key and the value
    print(key, value)
    print(f"{key} = {value}") #we can format it to make it look better
