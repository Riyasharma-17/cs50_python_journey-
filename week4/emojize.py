# Emojize 

# Typing emoji codes is easier than finding real emojis sometimes 😄

# This program converts emoji codes like:

# :thumbs_up:

# into real emojis:

# 👍
# Task

# Create a Python file called emojize.py that:

# Takes text from the user
# Converts emoji codes or aliases into real emojis
# Prints the updated text

# Example
# Input: I love Python :smile:
# Output: I love Python 😄

# Code

import emoji

x = input("Enter any sentence related to emoji: ")

print(emoji.emojize(x))
