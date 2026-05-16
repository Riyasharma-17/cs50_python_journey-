# Bank 

# A bank gives money based on how the user greets them 💰

# Task

# Create a Python file called bank.py that:

# Takes a greeting from the user
# Prints:
# $0 → if greeting starts with "hello"
# $20 → if greeting starts with "h" but not "hello"
# $100 → for anything else
# Ignore uppercase/lowercase and extra spaces

# Example
# Input: hello
# Output: $0
# Input: hey
# Output: $20
# Input: good morning
# Output: $100

# Code

greeting = input("Greet the manager ")
greeting = greeting.lower().strip()

if greeting.startswith("hello"):
    print("$0")
elif greeting.startswith("h"):
    print("$20")
else:
    print("$100")