# Guessing Game 

# The computer secretly chooses a random number 🎲
# Your job is to guess it correctly.

# Task

# Create a Python file called game.py that:

# Asks the user for a level n
# Generates a random number between 1 and n
# Keeps asking the user to guess
# Prints:
# "Too small!" → if guess is low
# "Too large!" → if guess is high
# "Just right!" → if guess is correct
# Ignores invalid or non-positive inputs
# Example
# Level: 10
# Guess: 3
# Too small!

# Guess: 8
# Too large!

# Guess: 5
# Just right!

# Code
import random

while True:
    try:
        level = int(input("Level :"))

        if level > 0:
            break

    except ValueError:
        pass

    number = random.randint(1,level)

    while True:
        try:
            guess = int(input("Guess: "))

            if guess <=0:
                continue

            if guess < number:
                print("Too small")

            elif guess > number:
                print("Too large!")

            else:
                print("Just right!")
                break 

        except ValueError:
            pass