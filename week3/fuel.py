# Fuel Gauge 

# This program checks how much fuel is left in a tank ⛽

# The user enters a fraction like:

# 1/4

# which means the tank is 25% full.

# Task

# Create a Python file called fuel.py that:

# Takes a fraction X/Y from the user
# Converts it into a percentage
# Rounds to nearest integer
# Prints:
# E → if fuel is 1% or less
# F → if fuel is 99% or more
# otherwise print percentage

# Also:

# Ask again if input is invalid
# Handle errors like:
# non-integer input
# division by zero
# X > Y

# Example
# Input: 1/2
# Output: 50%
# Input: 99/100
# Output: F

# Code
# fuel.py

while True:

    try:
        fraction = input("Fraction: ")

        x, y = fraction.split("/")

        x = int(x)
        y = int(y)

        if x > y:
            continue

        percentage = round((x / y) * 100)

        if percentage <= 1:
            print("E")

        elif percentage >= 99:
            print("F")

        else:
            print(f"{percentage}%")

        break

    except (ValueError, ZeroDivisionError):
        pass