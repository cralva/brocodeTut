# Space cadet quiz
#testing some stuff

questions = ("What is the smallest planet in our solar system?",
             "Who was the first astronaut to walk on the moon?",
             "What was the name of the Russian spaceship that tried to beat us to space?",
             "What happened to Apollo 13?",
             "What is the USA space organization called?")

options = (("A. Pluto", "B. Mars", "C. Jupiter", "D. Earth"),
           ("A. Muhammad Ali", "B. Floyd Mayweather", "C. Drew Brees", "D. Neil Armstrong"),
           ("A. Vodka", "B. Count Dracula", "C. Sputnik", "D. Vlad"),
           ("A. It landed on the moon", "B. It exploded", "C. It went to Las Vegas, Baby!", "D. Went to sleep"),
           ("A. USASA", "B. US Space Nation", "C. USS", "D. NASA"))

answers = ("A", "D", "C", "B", "D")
guesses = []
score = 0
questionNum = 0

for question in questions:
  print("-------------------")
  print(question)
  for option in options[questionNum]:
    print(option)

  guess = input("Enter A, B, C, or D: ").upper()
  guesses.append(guess)
  if guess == answers[questionNum]:
    score += 1
    print(f"You answered {guess} and that is correct!")
  else:
    print(f"You are wrong. The correct answer is {answers[questionNum]}")

  questionNum += 1

print("----------------")
print("RESULTS")
print("----------------")

print("Answers: ", end="")
for answer in answers:
  print(answer, end=" ")

print()

print("Guesses: ", end="")
for guess in guesses:
  print(guess, end=" ")

score = int(score) / len(questions) * 100
print(f"Your final score is: {score}")













