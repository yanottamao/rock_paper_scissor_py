import random


def choices():
    global comp_choices
    global plyr_choices
    comp_choices = random.randint(1, 3)

    # Helper
    # if comp_choices == 1:
    #     print("Rock")
    # elif comp_choices == 2:
    #     print("Paper")
    # elif comp_choices == 3:
    #     print("Scissor")
    # print(comp_choices)

    print("1. Rock")
    print("2. Paper")
    print("3. Scissor")
    plyr_choices = int(input("Please enter 1/2/3: "))
    print(plyr_choices)
    return comp_choices, plyr_choices


def win_condition():
    if comp_choices == 1 and plyr_choices == 1:
        print("Result: Draw")
    elif comp_choices == 1 and plyr_choices == 2:
        print("Result: Player Wins")
    elif comp_choices == 1 and plyr_choices == 3:
        print("Result: Computer Wins")

    elif comp_choices == 2 and plyr_choices == 1:
        print("Result: Computer Wins")
    elif comp_choices == 2 and plyr_choices == 2:
        print("Result: Draw")
    elif comp_choices == 2 and plyr_choices == 3:
        print("Result: Player Wins")

    elif comp_choices == 3 and plyr_choices == 1:
        print("Result: Player Wins")
    elif comp_choices == 3 and plyr_choices == 2:
        print("Result: Computer Wins")
    elif comp_choices == 3 and plyr_choices == 3:
        print("Result: Draw")


def main():
    print("Hello Rock Paper Scissor")
    choices()
    win_condition()


if __name__ == "__main__":
    main()
