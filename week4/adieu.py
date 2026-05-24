# Adieu, Adieu 

# This program says goodbye to multiple people 👋

# The user enters names one by one.
# When the user presses Ctrl + D, the program prints all names in proper English format using commas and "and".

# Task

# Create a Python file called adieu.py that:

# Takes names line by line
# Stops when user presses Ctrl + D
# Prints:
# Adieu, adieu, to name(s)

# using correct grammar.

# Example
# Input:
# Liesl
# Friedrich
# Louisa

# Output:

# Adieu, adieu, to Liesl, Friedrich, and Louisa

# Code
# adieu.py

names = []

try:
    while True:
        name = input("Name: ")
        names.append(name)

except EOFError:

    if len(names) == 1:
        print(f"Adieu, adieu, to {names[0]}")

    elif len(names) == 2:
        print(f"Adieu, adieu, to {names[0]} and {names[1]}")

    else:
        print(f"Adieu, adieu, to {', '.join(names[:-1])}, and {names[-1]}")