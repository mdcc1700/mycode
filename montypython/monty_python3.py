#!/usr/bin/python3
"""Alta3 Research | RZFeeser
   CHALLENGE 01 & 02 - Solutions to both challenges."""

round = 0
answer = " "

# augment our while condition to test if "brian" or "shrubbery" was the input
# you could reduce the complexity of this conditional with some "break" statements
while round < 3 and (answer != "Brian" and answer != "Shrubbery"):
    round += 1     # increase the round counter by 1
    answer = input('Finish the movie title, "Monty Python\'s The Life of ______": ')
    answer = answer.capitalize() # this line inserted to line 8 will make all
                                 # user input starts with an uppercase
    if answer == "Brian": # logic to check if user gave correct answer
        print("Correct!")
    elif answer == "Shrubbery":
        print("You gave the super secret answer!")
    elif round == 3:    # logic to ensure round has not yet reached 3
        print("Sorry, the answer was Brian.")
    else:                 # if answer was wrong
        print("Sorry. Try again!")

