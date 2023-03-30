import random

print("...rock...")
print("...paper...")
print("...scissors...")

user1 = input("(enter Player 1's choice): ").lower()
computer = random.randint(0, 2)

# 0: rock; #1: paper; #2: scissors

if computer == 0:
    computer = "rock"
    print(f"computer choose: {computer}")
    if user1 == "paper":
        print("player win!")
    elif user1 == "scissors":
        print("computer win!")
elif computer == 1:
    computer = "paper"
    print(f"computer choose: {computer}")
    if user1 == "scissors":
        print("player win!")
    elif user1 == "rock":
        print("computer win!")
elif computer == 2:
    computer = "scissors"
    print(f"computer choose: {computer}")
    if user1 == "rock":
        print("player win!")
    elif user1 == "paper":
        print("computer win!")
else:
    print("Something went wrong")

if user1 == computer:
    print("draw!")
