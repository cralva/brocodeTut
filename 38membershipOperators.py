# Membership Operators = used to test whether a value or variable is found in a sequence (string, list, tuple, set, or dictionary)
#                   1. in
#                   2. not in

word = "APPLE"

letter = input("Guess a letter in the secret word: ")

if letter in word:
    print(f"There is a {letter} in the word")
else:
    print(f"{letter} was not found")


if letter not in word: #basically same thing except the print statements gets flipped
    print(f"{letter} was not found")
else:
    print(f"There is a {letter} in the word")




students = {"Spongebob", "Patrick", "Sandy"}

student = input("Enter the name of a student: ")

if student in students:
    print(f"{student} is a student")
else:
    print(f"{student} was not found")

if student not in students:
    print(f"{student} was not found") #flipping the original
else:
    print(f"{student} is a student")


grades = {"Sandy":"A", 
          "Squidward":"B", 
          "Spongebob":"C", 
          "Patrick":"D"}


studentGuess = input("Enter the name of a student: ")

if studentGuess in grades: #this is defaulting to looking for keys, if we want values then we need to specify further
    print(f"{studentGuess}'s grade is {grades[studentGuess]}") #using the grades[] index to get the value for the specific student key
else:
    print(f"{studentGuess} is not found at this time")



email = "ca@pinfence.com"

if "@" in email and "." in email:
    print("Valid email")
else:
    print("invalid email")