# Q) Deep Thought 

# In a famous sci-fi story, the answer to “Life, the Universe and Everything” is 42 🌌

# Task

# Create a Python file called deep.py that:

# Takes input from the user
# Prints Yes if the user enters:
# 42
# forty-two
# forty two
# Ignore uppercase/lowercase differences
# Otherwise print No

# Example
# Input: forty-two
# Output: Yes

# Code


answer = input("What is the answer to the Great Question? ")

answer = answer.lower().strip()

if answer == "42" or answer == "forty-two" or answer == "forty two":
    print("Yes")
else:
    print("No")