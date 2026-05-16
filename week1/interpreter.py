# Math Interpreter 

# This program works like a mini calculator 
# The user enters a math expression, and the program calculates the answer.

# Task

# Create a Python file called interpreter.py that:

# Takes a math expression from the user
# Supports:
# + → addition
# - → subtraction
# * → multiplication
# / → division
# Prints the result as a float with 1 decimal place

# Example
# Input: 1 + 1
# Output: 2.0
# Input: 10 / 4
# Output: 2.5

# Code

expression = input("Expression: ")

x, y, z = expression.split()

x = int(x)
z = int(z)

if y == "+":
    print(f"{x + z:.1f}")

elif y == "-":
    print(f"{x - z:.1f}")

elif y == "*":
    print(f"{x * z:.1f}")

elif y == "/":
    print(f"{x / z:.1f}")