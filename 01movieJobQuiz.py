# chat gpt task

questions = ("What color is the sky? ",
             "How many legs does a spider have? ",
             "Which animal is known as the king of the jungle? ",
             "What planet do we live on? ",
             "What gas do plants breathe in? ")

options = (("A. Green", "B. Blue", "C. Red", "D. Yellow"),
           ("A. 6", "B. 8", "C. 10", "D. 12"),
           ("A. Tiger", "B. Elephant", "C. Lion", "D. Gorilla"),
           ("A. Mars", "B. Earth", "C. Jupiter", "D. Venus"),
           ("A. Oxygen", "B. Hydrogen", "C. Nitrogen", "D. Carbon Dioxide"))

answers = ("B", "B", "C", "B", "D")

guesses = []

score = 0

questionNum = 0

for question in questions:
    print("--------------------")
    print(question)
    for option in options[questionNum]:
        print(option)

    guess = input("Enter A, B, C, or D: ").upper()
    guesses.append(guess)

    if guess == answers[questionNum]:
        print("Correct")
        score += 1
    else:
        print(f"Incorrect! The correct answer is {answers[questionNum]}!")

    questionNum += 1

print("------------------")
print("RESULTS")
print("------------------")

print("Answers: ", end="")
for answer in answers:
    print(answer, end= " ")

print()

print("Guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")






