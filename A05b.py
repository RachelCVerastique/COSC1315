# ------------------------------------------------------
# Programmer:    Rachel Verastique
# Course:        COSC 1315Section 001
# Semester:      Spring 2023
# Assignment #:  A05b
# Due Date:      March 8, 2023
# ------------------------------------------------------
import random

# Constants
INVALID = 3
COMPUTER_WINS = 1
USER_WINS = 2
ITS_A_TIE = 0
ROCK = 1
PAPER = 2
SCISSORS = 3


# main function
def main():
    keepPlaying = 1

    # while loop for the option to play again
    while keepPlaying == 1:

        result = ITS_A_TIE

        while result == ITS_A_TIE:
            comp = random.randint(1, 3)

            user = int(input("Make your move... Enter 1 for 'Rock', 2 for 'Paper', 3 for 'Scissors':"))

            print(f"Computer choice: {choiceString(comp)}")
            print(f"You chose: {choiceString(user)}")

            result = rockPaperScissors(user, comp)

            if result == ITS_A_TIE:
                print("ITS A TIE! TRY AGAIN!!")
            elif result == COMPUTER_WINS:
                print("I WIN!")
            elif result == USER_WINS:
                print("YOU WIN!")
            else:
                print("INVALID ENTRY, NO WINNER!")

        keepPlaying = int(input("Would you like to play again?"
                                "(1 - yes, 0 - no)"))

    print("\nThis program was coded by Rachel Verastique.")
    print("End of program.")


def choiceString(choice):
    if choice == ROCK:
        return "Rock"
    elif choice == PAPER:
        return "Paper"
    elif choice == SCISSORS:
        return "Scissors"
    else:
        return "Invalid Entry, Try Again."


def rockPaperScissors(userChoice, compChoice):
    if compChoice == userChoice:
        return ITS_A_TIE

    if compChoice == ROCK:
        if userChoice == PAPER:
            return USER_WINS
        elif userChoice == SCISSORS:
            return COMPUTER_WINS
        else:
            return INVALID
    elif compChoice == PAPER:
        if userChoice == ROCK:
            return COMPUTER_WINS
        elif userChoice == SCISSORS:
            return USER_WINS
        else:
            return INVALID
    else:  # if comp chooses scissors
        if userChoice == ROCK:
            return USER_WINS
        elif userChoice == PAPER:
            return COMPUTER_WINS
        else:
            return INVALID


main()
