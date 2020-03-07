# Modify the program below to use a while loop to
# allow as many guesses as necessary.
#
# The program should let the player know whether to
# guess higher or lower, and should print a message
# when the guess is correct. A correct guess will
# terminate the program.
#
# As an optional extra, allow the player to quit by entering
# 0 (zero) for their guess.
import random
highest = 20
answer = random.randint(1, highest)
# print(answer)
print("Please enter a number between 1 and {}: ".format(highest))
guess = 0
while answer != guess:
    guess = int(input())
    if guess < answer:
        print("Input a higher number")
    elif guess > answer:
        print("Input a lower number")
    else:
        print("congratulate! you win")
