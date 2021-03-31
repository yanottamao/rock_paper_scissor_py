import random

# print("Hello Rock Paper Scissor")
# comp_choices = random.randint(1, 9)
# if comp_choices == 1 or comp_choices == 6 or comp_choices == 7:
#     print("Rock")
# elif comp_choices == 2 or comp_choices == 4 or comp_choices == 9:
#     print("Paper")
# elif comp_choices == 3 or comp_choices == 5 or comp_choices == 8:
#     print("Scissor")
# print(comp_choices)

print("Hello Rock Paper Scissor")
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

# if plyr_choices == 1 or plyr_choices == 2 or plyr_choices == 3:
#     print("Please enter valid choice")

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
