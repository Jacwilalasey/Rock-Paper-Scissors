from random import randint

t = ["Rock", "Paper", "Scissors"]

PC = t[randint(0, 2)]

player = False

print("\n")
print("------------------------")
print("Game initialising")
print("------------------------")

while player == False:
    player = input("\nRock, Paper, Scissors? ")
    if player == PC:
        print("Tie, try again!")
    elif player == "Rock":
        if PC == "Paper":
            print("You lose!", PC, "covers", player)
        else:
            print("You win!", player, "smashes", PC)
    elif player == "Paper":
        if PC == "Scissors":
            print("You lose!", PC, "cuts", player)
        else:
            print("you win!", player, "covers", PC)
    elif player == "Scissors":
        if PC == "Rock":
            print("You lose!", PC, "smashes", player)
        else:
            print("You win!", player, "cuts", PC)
    else:
        print("That's not a valid input, check your spelling!")

    player = False
    PC = t[randint(0,2)]