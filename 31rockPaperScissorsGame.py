#rock paper scissors
import random

options = ("rock", "paper", "scissors")
running = True
player = None
computer = ""
wins = 0
losses = 0
ties = 0

while running:
    computer = random.choice(options)
    player = None
    while player not in options:
        player = input('Enter what you would like to play: ')
        print(f'You cant use {player} as an entry! Use rock, paper, or scissors')

    print(f'Player: {player}')
    print(f'Computer: {computer}')

    if player == computer:
        ties += 1
        print("its a tie!")
    elif player == "rock" and computer == "scissors":
        wins += 1
        print("You win!")
    elif player == "scissors" and computer == "paper":
        wins += 1
        print("You win!")
    elif player == "paper" and computer == "rock":
        wins += 1
        print("You win!")
    else:
        losses += 1
        print("You lose!")
    
    replay = input("Would you like to play again (y/n): ").lower()
    if not replay == "y":
        running = False

print(f'Your record was {wins}-{losses}-{ties}')
print("Thank you for playing")