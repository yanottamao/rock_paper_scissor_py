import random


def choices():
    print("Computer turn...")
    global comp_choices
    global plyr_choices
    comp_choices = random.randint(1, 3)
    print("\nPlayer turn...")
    print("Player choice:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissor")
    plyr_choices = int(input("Please enter 1/2/3: "))
    return comp_choices, plyr_choices


def win_condition():
    if comp_choices == 1 and plyr_choices == 1:
        print("\nComputer: Rock")
        print("Player: Rock")
        print("\nResult: Draw")
    elif comp_choices == 1 and plyr_choices == 2:
        print("\nComputer: Rock")
        print("Player: Paper")
        print("\nResult: Player Wins")
    elif comp_choices == 1 and plyr_choices == 3:
        print("\nComputer: Rock")
        print("Player: Scissor")
        print("\nResult: Computer Wins")

    elif comp_choices == 2 and plyr_choices == 1:
        print("\nComputer: Paper")
        print("Player: Rock")
        print("\nResult: Computer Wins")
    elif comp_choices == 2 and plyr_choices == 2:
        print("\nComputer: Paper")
        print("Player: Paper")
        print("\nResult: Draw")
    elif comp_choices == 2 and plyr_choices == 3:
        print("\nComputer: Paper")
        print("Player: Scissor")
        print("\nResult: Player Wins")

    elif comp_choices == 3 and plyr_choices == 1:
        print("\nComputer: Scissor")
        print("Player: Rock")
        print("\nResult: Player Wins")
    elif comp_choices == 3 and plyr_choices == 2:
        print("\nComputer: Scissor")
        print("Player: Paper")
        print("\nResult: Computer Wins")
    elif comp_choices == 3 and plyr_choices == 3:
        print("\nComputer: Scissor")
        print("Player: Scissor")
        print("\nResult: Draw")


def main():
    print("\nRock Paper Scissor Game\n")
    choices()
    win_condition()


if __name__ == "__main__":
    main()
