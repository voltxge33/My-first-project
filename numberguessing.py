import random
# Random number for guessing
input1 = int(input("Start Range:"))
input2 = int(input("End Range:"))
random_num = str(random.randint(input1, input2))

guesses = 7

# start
print("Guess a number any number!")
answer = input()

while True:
    if answer == random_num:
        print("You did it! Nice!")
        break
    if guesses == 0:
        print("Out of guesses, start over.")
        break
    if answer.isdigit():
        print("Incorrect! You have " + str(guesses) + " left")
        guesses -= 1
        answer = input()
    if answer.isalpha():
        print("That's not right, pick a number next time please.")
        answer = input()







