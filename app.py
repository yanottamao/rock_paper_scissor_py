import random


def choices():
    comp_choices = random.randint(1, 3)
    if comp_choices == 1:
        print("Rock")
    elif comp_choices == 2:
        print("Paper")
    elif comp_choices == 3:
    print("Scissor")
    print(comp_choices)


print("1. Rock")
print("2. Paper")
print("3. Scissor")
plyr_choices = int(input("Please enter 1/2/3: "))
print(plyr_choices)


def win_condition():


if comp_choices == 1 and plyr_choices == 1:
    print("Draw")
elif comp_choices == 1 and plyr_choices == 2:
    print("Player Wins")
elif comp_choices == 1 and plyr_choices == 3:
    print("Computer Wins")

elif comp_choices == 2 and plyr_choices == 1:
    print("Computer Wins")
elif comp_choices == 2 and plyr_choices == 2:
    print("Draw")
elif comp_choices == 2 and plyr_choices == 3:
    print("Player Wins")

elif comp_choices == 3 and plyr_choices == 1:
    print("Player Wins")
elif comp_choices == 3 and plyr_choices == 2:
    print("Computer Wins")
elif comp_choices == 3 and plyr_choices == 3:
    print("Draw")


def main():


print("Hello Rock Paper Scissor")
