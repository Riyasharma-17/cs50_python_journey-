# Meal Time — Python Project

# This program checks the current time and tells whether it’s time for breakfast, lunch, or dinner 🍳🍔🍝

# Meal Times
# 7:00 - 8:00   → breakfast
# 12:00 - 13:00 → lunch
# 18:00 - 19:00 → dinner
# Task

# Create a Python file called meal.py that:

# Takes time input from the user in HH:MM format
# Converts the time into a float value
# Prints:
# "breakfast time"
# "lunch time"
# "dinner time"
# Prints nothing if it’s not meal time

# Example
# Input: 7:30
# Output: breakfast time

# Code


def main():
    time = input("What time is it? ")

    time = convert(time)

    if 7 <= time <= 8:
        print("breakfast time")

    elif 12 <= time <= 13:
        print("lunch time")

    elif 18 <= time <= 19:
        print("dinner time")


def convert(time):
    hours, minutes = time.split(":")

    hours = int(hours)
    minutes = int(minutes)

    return hours + minutes / 60


if __name__ == "__main__":
    main()