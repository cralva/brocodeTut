#number guessing game
import random

lowest_number = 1
highest_number = 100
answer = random.randint(lowest_number, highest_number)
guesses = 0
is_running = True

print("Python Number Guessing Game")
print(f"Select a number between {lowest_number} and {highest_number}")

while is_running: #since this will be an infinite loop intially we need to trash the terminal each time we make changes to ensure that the program ends

    guess = input("Please guess a number 1 - 100: ")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < lowest_number or guess > highest_number:
            print("That number is out of range")
            print(f"Please select a number between {lowest_number} and {highest_number}")
        elif guess < answer:
            print("Too low. Try again")
        elif guess > answer:
            print("Too high. Guess again")
        else:
            print(f'Correct! The answer was {answer}')
            print(f"It took you {guesses} tries to get the correct answer")
            is_running = False #this is the statement that will break us out of the loop. Without this this is will run forever

    else:
        print("Invalid guess")
        print(f"Please select a number between {lowest_number} and {highest_number}")
