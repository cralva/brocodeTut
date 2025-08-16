# List comprehension = A concise way to create lists in python
#                      Compact and easier to read than traditional loops
#                     [expression for value in iterable if condition]


#before list comprehension
doubles = []
for x in range(1,11):
    doubles.append(x * 2)
print(doubles)

#after using list comprehension
doublesLE = [x * 2 for x in range(1, 11)] #expression for value in iterable if condition] this is the format that we used but we are ignore the if condition
print(doublesLE)

#tripling every number using list comprehensions
triples = [y * 3 for y in range(1, 11)]
print(triples)

#square each number
squares = [z * z for z in range(1, 11)]
print(squares)

#working with strings
fruits = ["apple", "orange", "bannana", "coconut"]
#lets making our fruits list uppercase
uppercase_fruits = [fruit.upper() for fruit in fruits] #start with for value in iterable section first. easier to organize and work from there
print(uppercase_fruits)

#lets take the first letter of each of the fruits string
fruits_char = [fruit[0] for fruit in fruits] #fruit[0] is the expression. this is what we want each iterable to do. we want it to return the first letter of the fruit
print(fruits_char)

#working with conditions
numbers = [1, -2, 3, -4, 5, -6]
#use lc to create a new list where all of the numbers are positive
positive_nums = [num for num in numbers if num >= 0] # we still need an expression so if we are not modifying then use the value. using the condition this time though
print(positive_nums)

#use lc to find negative numbers
negative_nums = [num for num in numbers if num < 0]
print(negative_nums)

#check to see if there are any even nums
even_nums = [num for num in numbers if num % 2 == 0]
print(even_nums)

#check for odds
odd_nums = [num for num in numbers if num % 2 == 1]
print(odd_nums)

#new exercise
grades = [85, 42, 79, 90, 56, 61, 30]
passing_grades = [grade for grade in grades if grade >= 60] #the expression is what we are returning. so we will return any grades that are 60 or above
print(passing_grades)