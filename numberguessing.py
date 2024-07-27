import random as ranpy
# Random number for guessing
input1 = int(input("Start Range:"))
input2 = int(input("End Range:"))
random_num = ranpy.randint(input1, input2)

guesses = 7

# start
print("Guess a number any number!")
answer = int(input())
while answer != random_num and guesses > 0:

    print("Incorrect! You have " + str(guesses) + " left")
    answer = int(input())
    guesses = guesses-1
if answer == random_num:
    print("You did it! Nice!")
if guesses == 0:
    print("Out of guesses, start over.")




