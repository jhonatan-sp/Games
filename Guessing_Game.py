# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random

def play():
    print("*************************")
    print("***Welcome to Guessing Game!***")
    print("*************************")

secret_number = random.randrange(1, 101)
total_attempts = 0
points = 1000

print("Choose difficulty level")
print("(1) Easy (2) Medium (3) Hard")

level = int(input("Define level: "))
if(level == 1):
    total_attempts = 20
elif(level == 2):
    total_attempts = 10
else:
    total_attempts = 5

for attempt in range(1, total_attempts + 1):
    print("Attempt {} of {}".format(attempt, total_attempts))
    guess = input("Pick a number from 1 to 100: ")
    print("You typed ", guess)
    guess = int(guess)

    if(guess < 1 or guess > 100):
        print("You must pick a number from 1 to 100")
        continue

    right  = guess == secret_number
    higher = guess > secret_number
    lower  = guess < secret_number

    if(right):
        print("You got it and scored {} points!".format(points))
        break
    else:
        if(higher):
            print("Your guess was higher than the secret number.")
        elif(lower):
            print("Your guess was lower than the secret number.")
        missing_points = abs(secret_number - guess)
        points = points - missing_points

print("End game")

if(__name__ == "__main__"):
  play()

