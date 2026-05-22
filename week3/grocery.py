# Grocery List

# This program helps make a grocery list 🛒

# The user enters grocery items one by one.
# When the user finishes (Ctrl + D), the program:

# Counts how many times each item was entered
# Sorts items alphabetically
# Prints everything in uppercase
# Task

# Create a Python file called grocery.py that:

# Takes grocery items line by line
# Ignores uppercase/lowercase differences
# Counts repeated items
# Stops when user presses Ctrl + D
# Prints:
# count of each item
# item name in uppercase

# Example
# Input:
# apple
# banana
# apple
# milk
# banana

# Output:

# 2 APPLE
# 2 BANANA
# 1 MILK

# Code
# grocery.py

grocery = {}

try:
    while True:

        item = input().upper()

        if item in grocery:
            grocery[item] += 1

        else:
            grocery[item] = 1

except EOFError:

    for item in sorted(grocery):
        print(grocery[item], item)