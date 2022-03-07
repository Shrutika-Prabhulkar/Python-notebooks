#Guess the number
import random
#  generate random num between 0-100
computer_guess = random.randint(0,100)

user_guess = -1
while user_guess != computer_guess:
    #Prompt the user to enter random num between 0-100
    user_guess = eval(input("Enter random number "))

    # compare user guess with computer guess
    if user_guess  > computer_guess:
        print("Guess is too high")
    elif user_guess == computer_guess:
        print("Correct")
    else:
        print("Guess is too low ")       