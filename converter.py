import random

playerScore = 0
computerScore = 0
winning = 3

print("...paper...")
print("...rock...")
print("...scissors...")

while playerScore < winning and computerScore < winning:

    player = input("You choose: ").lower()
    computer = random.randint(0, 2)

    if computer == 0:
        computer = "paper"
    elif computer == 1:
        computer = "rock"
    else:
        computer = "scissors"

    print(f"Computer choose: {computer}")
    if player == "quit" or player == "q":
        break
    elif player == computer:
        print("Tie!")
    elif player == "paper":
        if computer == "scissors":
            print("Computer win!")
            computerScore += 1
        elif computer == "rock":
            print("You win!")
            playerScore += 1
    elif player == "rock":
        if computer == "paper":
            print("Computer win!")
            computerScore += 1
        elif computer == "scissors":
            print("You win!")
            playerScore += 1
    elif player == "scissors":
        if computer == "rock":
            print("Computer win!")
            computerScore += 1
        elif computer == "paper":
            print("You win!")
            playerScore += 1
    else:
        print("Something went wrong! Try again: ")

if playerScore == computerScore:
    print("Tie!")
elif playerScore > computerScore:
    print("You are winner!")
else:
    print("OH NO!! Computer won :((")
