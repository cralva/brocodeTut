import random #importing this module gives us access to a lot of useful methods that deal with random numbers

#help(random) #print this to get a list of methods that are in the random module

number = random.randint(1, 20) #will print a random integer in the range/// the numbers in the parentheses is the range (ex is a 6 sided dice)//added the variable at the end so the number will have be in the number variable

low = 2
high = 20
number2 = random.randint(low, high) #we can also use pass variables as arguments but they have to be intergers

print(number)
print(number2)

number3 = random.random() #this will pick a random float number between 0-1
print(number3)

options = ("rock", "paper", "scissors")
random_pick = random.choice(options) #this is a random choice method. it will randomly pick one out of the options tuple. we need to pass the tuple in the parameter
print(random_pick)

cards = ["1", "2", "3", "4", "5", "6", "7", "A", "J"]
random.shuffle(cards) #going to shuffle the cards randomly by using this method//we dont need to add it to a variable?
#when the method modifies the data (shuffle modifies cards and does not a return a new value) then it doesnt need a new variable but when it returns new data then it needs a new variable (.choice or randint returns a new value so it does need a variable. they dont modify anything)
print(cards)
