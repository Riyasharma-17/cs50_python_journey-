# Little Professor

# This program is a small math quiz game 🧠➕
# The computer asks 10 addition questions, and the user tries to answer them correctly.

# Levels
# Level 1 → single-digit numbers (0–9)
# Level 2 → two-digit numbers (10–99)
# Level 3 → three-digit numbers (100–999)
# Task

# Create a Python file called professor.py that:

# Asks the user for a level (1, 2, or 3)
# Generates 10 random addition problems
# Gives the user 3 tries for each question
# Prints "EEE" for wrong answers
# Shows the correct answer after 3 failed attempts
# Prints final score out of 10

# Example
# Level: 1
# 4 + 1 = 5
# 8 + 3 = 12
# EEE
# 8 + 3 = 11
# Score: 9

# Code
# professor.py

import random


def main():

    level = get_level()
    score = 0

    for _ in range(10):

        x = generate_integer(level)
        y = generate_integer(level)

        answer = x + y
        tries = 0

        while tries < 3:

            try:
                guess = int(input(f"{x} + {y} = "))

                if guess == answer:
                    score += 1
                    break

                else:
                    print("EEE")
                    tries += 1

            except ValueError:
                print("EEE")
                tries += 1

        if tries == 3:
            print(f"{x} + {y} = {answer}")

    print(f"Score: {score}")


def get_level():

    while True:

        try:
            level = int(input("Level: "))

            if level in [1, 2, 3]:
                return level

        except ValueError:
            pass


def generate_integer(level):

    if level == 1:
        return random.randint(0, 9)

    elif level == 2:
        return random.randint(10, 99)

    elif level == 3:
        return random.randint(100, 999)

    else:
        raise ValueError


if __name__ == "__main__":
    main()