# Camel Case 

# Some programming languages use camelCase for variable names like:

# firstName
# preferredFirstName

# Python prefers snake_case, where words are separated using _ and all letters are lowercase:

# first_name
# preferred_first_name
# Task

# Create a Python file called camel.py that:

# Takes a variable name in camelCase
# Converts it into snake_case
# Prints the result

# Example
# Input: preferredFirstName
# Output: preferred_first_name

# Code
# camel.py

camel = input("camelCase: ")

snake = ""

for letter in camel:

    if letter.isupper():
        snake += "_" + letter.lower()

    else:
        snake += letter

print("snake_case:", snake)