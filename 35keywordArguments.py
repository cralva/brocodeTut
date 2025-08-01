# keyword argument = an arugment preceded by an identifier
#                    helps with readability
#                    order or arguments doesn't matter
#                    1. positional 2. default 3. KEYWORD 4. arbitrary

def hello(greeting, title, first, last):
    print(f"{greeting} {title} {first} {last}")

hello("Hello", "Mr.", "Spongebob", "squarepants") #Position does matter so if we switch we will see it
hello("Hello", "Spongebob.", "squarepants", "Mr.") #Mr. will be shown last

#using keywork arguments
hello("Hello", title="Mr.", first="Spongebob", last="squarepants") #order doesnt matter with the keywords. BUT POSITIONAL arguments have to come first then keywords after. Will be syntx if keyword arguments are first

for x in range(1, 11): 
    print(x) #this will print a new line after each iteration

for x in range(1, 11): 
    print(x, end=" ") # "end" is an example of a keyword arugment

print("one", "two", "three", "four", "five")
print("one", "two", "three", "four", "five", sep="-") #another keyword argument

def phone_num(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"

num = phone_num(country=1, area=260, first=458, last=1310)
print(num)

