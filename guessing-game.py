import random

computer = random.randint(1, 10)


while 1:

    player = int(input("Guessing a number between 1 and 10: "))

    if player > computer:
        print("Too high! Try again!")
    elif player < computer:
        print("Too low! Try again!")
    else:
        print("You guessed it! You won!")

        confirmAgain = input("Do you want to keep playing? (y/n) ")
        if confirmAgain.lower() == "n":
            print("Thank you <3")
            break
        else:
            computer = random.randint(1, 10)
